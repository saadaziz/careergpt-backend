import logging
from flask import Flask, request, jsonify
import os
import yaml
from datetime import datetime
import tailer
from flask import send_file

CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "app_config.yaml"))

# Point to stderr.log (usually one level up or as set by your host)
STDERR_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "stderr.log"))
# If your stderr log is elsewhere, update STDERR_PATH accordingly.

# Logging setup - only to stderr!
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler()  # only stderr
    ]
)

app = Flask(__name__, static_folder='static')

def log_event(message, data=None, level=logging.INFO):
    if data is not None:
        logging.log(level, f"{message} | data={data}")
    else:
        logging.log(level, message)

def load_config():
    try:
        with open(CONFIG_PATH, "r") as f:
            config = yaml.safe_load(f) or {}
            log_event("Config loaded", config, logging.DEBUG)
            return config
    except Exception as e:
        log_event("Failed to load config", str(e), logging.ERROR)
        return {}

def save_config(new_config):
    try:
        with open(CONFIG_PATH, "w") as f:
            yaml.safe_dump(new_config, f, default_flow_style=False)
        log_event("Config saved", new_config)
        return True, None
    except Exception as e:
        log_event("Failed to save config", str(e), logging.ERROR)
        return False, str(e)

@app.before_request
def log_request():
    log_event("Incoming request", {
        "endpoint": request.path,
        "method": request.method,
        "remote_addr": request.remote_addr,
        "args": request.args.to_dict(),
        "json": request.get_json(silent=True)
    })

@app.after_request
def log_response(response):
    try:
        data = response.get_json()
    except Exception:
        data = response.data.decode() if hasattr(response.data, "decode") else str(response.data)
    log_event("Outgoing response", {
        "endpoint": request.path,
        "status": response.status,
        "data": data
    })
    return response

@app.route("/", methods=["GET"])
def root():
    log_event("Health check endpoint hit")
    return jsonify({
        "message": "Flask app running on cPanel via Passenger",
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json(force=True)
        log_event("Analyze request received", data)
        config = load_config()
        result = {
            "received": data,
            "config_snapshot": config,
            "status": "success"
        }
        log_event("Analyze processed", result)
        return jsonify(result)
    except Exception as e:
        log_event("Analyze error", str(e), logging.ERROR)
        return jsonify({"error": str(e), "status": "failed"}), 400

@app.route("/config", methods=["GET", "POST"])
def config_endpoint():
    if request.method == "GET":
        config = load_config()
        return jsonify({"config": config})
    elif request.method == "POST":
        try:
            new_config = request.get_json(force=True)
            log_event("Config update attempt", new_config)
            if not isinstance(new_config, dict):
                raise ValueError("Config payload must be a JSON object")
            ok, err = save_config(new_config)
            if not ok:
                return jsonify({"error": err, "status": "failed"}), 500
            return jsonify({"message": "Config updated", "status": "success"})
        except Exception as e:
            log_event("Config update error", str(e), logging.ERROR)
            return jsonify({"error": str(e), "status": "failed"}), 400

@app.route("/logs", methods=["GET"])
def get_logs():
    num_lines = int(request.args.get("lines", 100))
    try:
        # Now reads from stderr.log
        with open(STDERR_PATH, "r") as f:
            last_lines = tailer.tail(f, num_lines)
        return jsonify({
            "log": last_lines,
            "status": "ok"
        })
    except Exception as e:
        log_event("stderr file read error", str(e), logging.ERROR)
        return jsonify({"error": str(e), "status": "failed"}), 500

@app.route("/logs/download", methods=["GET"])
def download_logs():
    try:
        return send_file(STDERR_PATH, mimetype="text/plain", as_attachment=True, download_name="stderr.log")
    except Exception as e:
        log_event("stderr file download error", str(e), logging.ERROR)
        return jsonify({"error": str(e), "status": "failed"}), 500

@app.route("/logs/purge", methods=["POST"])
def purge_logs():
    try:
        open(STDERR_PATH, "w").close()  # Truncate the file
        log_event("stderr file purged by user action")
        return jsonify({"message": "Logs purged.", "status": "ok"})
    except Exception as e:
        log_event("stderr file purge error", str(e), logging.ERROR)
        return jsonify({"error": str(e), "status": "failed"}), 500


if __name__ == "__main__":
    app.run(debug=True)
