# The Everyday Style Edit — Streamlit Chatbot

A Gemini-powered fashion stylist chatbot based on the supplied Everyday Style Edit knowledge manual.

## 1. Requirements
- Python 3.9 or newer
- A Gemini API key from Google AI Studio

## 2. Install
Open a terminal in this project folder and run:

```bash
python -m venv .venv
```

Activate the environment:

**Windows**
```bash
.venv\Scripts\activate
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 3. Configure the API key
Open `.streamlit/secrets.toml` and replace `YOUR_GEMINI_API_KEY` with your own Gemini API key:

```toml
GEMINI_API_KEY = "paste-your-real-api-key-here"
GEMINI_MODEL = "gemini-2.5-flash"
```

Do not share the key, commit this file to Git, or paste it into public code.

## 4. Run the app

```bash
streamlit run app.py
```

Streamlit will open the chatbot in your browser.

## 5. Deploying
For Streamlit Community Cloud, add the same values under the app's **Settings → Secrets**. Do not rely on uploading a real `secrets.toml` file to a public repository.

## Files
- `app.py` — Streamlit interface and Gemini chatbot logic
- `requirements.txt` — Python dependencies
- `.streamlit/secrets.toml` — local API-key configuration template
- `.gitignore` — excludes secrets and local environment files
