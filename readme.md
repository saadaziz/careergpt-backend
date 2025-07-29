# CareerGPT Backend

CareerGPT is a **Flask-based backend** designed for robust, cloud-friendly deployment (cPanel/Passenger) and real-time logging/monitoring. It analyzes job titles using OpenAI and is built for future growth with security and body of knowledge integration.

---

## Features

- Flask backend running on cPanel (WSGI-compatible).
- Root endpoint (`/`) for health checks.
- `/analyze` endpoint for job data analysis.
- `/config` endpoint to view and update runtime YAML config.
- `/logs` endpoint for **real-time viewing** (auto-refresh and download supported).
- Centralized logging to `stderr` (no local log file needed).

---

## Roadmap

**Phase 1**
- `GET /` — Health/status with logging
- `POST /analyze` — Analyze input and show config snapshot
- `GET /config` — View YAML config (live)
- `POST /config` — Update YAML config (with logging/validation)
- `/logs` — Real-time log view (download only if permissions allow; purge not recommended for stderr logs)

```cmd
For example:
curl -X POST "https://aurorahours.com/careergpt-backend/analyze" -H "Content-Type: application/json" -d "{\"job_title\": \"Software Engineer\", \"location\": \"Remote\"}"

```
**Phase 2**
- Security: origin checks or API tokens
- User profiles and JWT authentication

**Phase 3**
- Body of Knowledge: ChromaDB + embeddings
- Admin dashboard for logs and analytics

---

## Project Structure

```
careergpt-backend/
├── app/
│   ├── main.py           # Flask app (routes, config, logging)
│   └── static/
│       └── logs.html     # Web UI for logs
├── passenger_wsgi.py     # WSGI entrypoint for cPanel
├── requirements.txt      # Dependencies
├── CHANGELOG.md          # Dev history
├── README.md             # This file
└── stderr.log            # stderr output (created by server, gitignored)
```

---

## Setup Instructions

### Local Development

1. **Clone the repo:**
    ```bash
    git clone https://github.com/<your-username>/careergpt-backend.git
    cd careergpt-backend
    ```

2. **Create virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run locally:**
    ```bash
    FLASK_APP=app/main.py flask run
    ```

---

### Deployment (cPanel / Passenger)

1. **Upload all files** to the app root (e.g., `/home/<username>/careergpt-backend/`)
2. **Create a Python App** in cPanel:
    - Python version: 3.9+
    - Application root: `careergpt-backend`
    - Startup file: `passenger_wsgi.py`
    - Entry point: `application`
3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt --user
    ```
4. **Set environment variables** (like `OPENAI_API_KEY`) in cPanel.
5. **Restart app** and test:
    - Health: `https://aurorahours.com/careergpt-backend/`
    - Logs: `https://aurorahours.com/careergpt-backend/logs`

---

## Development Notes

- All logs are written to **stderr** (managed by cPanel/Passenger; not a file in the repo)
- `/logs` supports tailing real-time logs (default: last 100 lines)
- Download works if Flask can read the actual `stderr.log` file
- **Purging logs is not supported** (for server reliability)
- Next steps: authentication, ChromaDB/BoK, admin analytics

---

## Changelog

See [CHANGELOG.md](./CHANGELOG.md) for detailed dev history.

---

## First-time Commit

```bash
git init
git add .
git commit -m "Initial Flask setup: WSGI, stderr logging, and logs UI"
git remote add origin https://github.com/<your-username>/careergpt-backend.git
git branch -M main
git push -u origin main
```

---

## Next Steps

- [ ] Confirm `/logs` endpoint works in production (test download if needed)
- [ ] Add `/demo` endpoint for UI/backend integration
- [ ] Document `/demo` API spec here

