# Website Scraper & Summarizer

This module provides a **lightweight web scraping utility** that fetches, cleans, and summarizes website content using OpenAI’s API. It’s designed for integration into projects like **CareerGPT**, where analyzing public profiles or blogs can add context to career insights.

---

## Features

- **Automatic .env detection**  
  Securely loads your OpenAI API key from a `.env` file (auto-detects location).

- **Web scraping with headers**  
  Mimics a browser user-agent to bypass basic bot protections.

- **HTML cleaning**  
  Removes scripts, styles, and irrelevant tags to extract readable text.

- **Markdown previews**  
  Quick previews for Jupyter notebooks or CLI demos.

- **Ready for AI integration**  
  Prepares data for summarization or analysis using GPT models.

---

## Code Overview

### 1. Environment Setup
```python
from dotenv import load_dotenv, find_dotenv
env_path = find_dotenv()
load_dotenv(env_path, override=True)
```

### 2. OpenAI Initialization
```python
from openai import OpenAI
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

### 3. Request Headers
```python
DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/117.0.0.0 Safari/537.36"
    )
}
```

### 4. `Website` Class
**Purpose**: Fetches and cleans webpage content.

Key methods:
- **`__init__`**: Downloads the page, strips irrelevant elements, extracts text.  
- **`preview(lines=5)`**: Displays first lines in Markdown for quick inspection.

### 5. Example Usage
```python
if __name__ == "__main__":
    site = Website("https://saadaziz.com")
    print(f"Title: {site.title}\n")
    print(site.text[:500])  # Preview raw text
    site.preview(8)         # Markdown preview (Jupyter only)
```

---

## Integration Ideas

- **CareerGPT enhancement**: Pull public blog/portfolio info into job risk analysis.  
- **Portfolio summaries**: Auto-generate “About Me” summaries for user websites.  
- **AI demos**: Show off GPT-powered summarization on any URL (public data only).

---

## Requirements

- `requests`
- `beautifulsoup4`
- `python-dotenv`
- `openai`

Install with:
```bash
pip install -r requirements.txt
```
