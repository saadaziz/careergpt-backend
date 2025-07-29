# CHANGELOG

## **\[Unreleased] – Initial FastAPI Setup on DomainRacer**

### **Added**

* **FastAPI Migration**

  * Replaced Flask prototype with FastAPI for async support and modular design.
  * Minimal structure: `app/main.py`, `passenger_wsgi.py`, and `requirements.txt`.

* **ASGI → WSGI Compatibility**

  * Implemented custom wrapper using Starlette’s `TestClient` to make FastAPI work on DomainRacer’s WSGI-only environment.
  * Set cPanel startup file to `passenger_wsgi.py` and entry point to `application`.

* **Logging System**

  * Configured logging to write directly to `stderr` (Passenger log).
  * Added `/logs` HTML endpoint:

    * Displays real-time logs from `stderr.log`.
    * Auto-refresh every 5 seconds.
    * Styled for terminal-like readability (green-on-black).
  * Removed redundant `startup.log`.

* **Deployment Configuration**

  * Verified cPanel environment variables (`OPENAI_API_KEY`).
  * Fixed corrupted export syntax (`export = sk-...`) issue.
  * Ensured directory structure compatibility:

    ```
    careergpt_dev/
      app/
        main.py
      passenger_wsgi.py
      requirements.txt
    ```

### **Changed**

* Cleaned up logging output (no duplicate files).
* Simplified debugging by exposing `/logs` for browser-based monitoring.
* Adjusted cPanel config to ensure correct file paths and entry points.

### **Issues Fixed**

* **ASGI/WSGI Mismatch Error**

  * Original: `TypeError: __call__() missing 1 required positional argument: 'send'`
  * Cause: FastAPI (ASGI) was loaded directly by WSGI.
  * Fix: Custom wrapper bridging ASGI app to WSGI using Starlette `TestClient`.

* **Invalid Environment Variable**

  * Original: `export: '=' not a valid identifier`
  * Cause: Misconfigured OPENAI\_API\_KEY variable in cPanel.
  * Fix: Removed malformed variable and re-added correctly.

---

### **Next Steps**

1. Implement `/demo` POST endpoint for UI → backend integration (Phase 1).
2. Add simple security (origin check or token) for `/demo` calls (Phase 2).
3. Integrate Body of Knowledge (ChromaDB + embeddings).
4. Enhance `/logs`:

   * Reverse order (newest first).
   * Optional password/IP restriction.
5. Document deployment workflow and update `README.md` for GitHub.

---

## **Ready for First GitHub Commit**

### **Files to Commit**

* `app/main.py`
* `passenger_wsgi.py`
* `requirements.txt`
* `CHANGELOG.md`
* `.gitignore` (recommend ignoring `__pycache__/` and `.env`)

