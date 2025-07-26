import logging
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

# Configure logging to stderr (Passenger captures this automatically)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI()

@app.get("/")
def root():
    logging.info("Root endpoint called successfully")
    return {"status": "ok", "message": "CareerGPT FastAPI running"}

@app.get("/logs", response_class=HTMLResponse)
def view_logs():
    log_path = os.path.join(os.path.dirname(__file__), "../stderr.log")
    try:
        with open(log_path, "r") as f:
            content = f.read()
    except FileNotFoundError:
        content = "Log file not found."

    # Simple HTML rendering
    return f"""
    <html>
        <head>
            <title>CareerGPT Logs</title>
            <meta http-equiv="refresh" content="5">
            <style>
                body {{ font-family: monospace; white-space: pre-wrap; background:#111; color:#0f0; padding:10px; }}
            </style>
        </head>
        <body>{content}</body>
    </html>
    """
