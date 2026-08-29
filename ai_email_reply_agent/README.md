# ✉️ AI Email Reply Agent

A simple Streamlit app that drafts email replies in seconds, powered by Claude.
Paste in the email you're replying to, pick a tone and length, and get one or
more ready-to-send draft replies.

Created and developed by **[Chintan Parmar](https://github.com/iamchintanparmar)**.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Claude](https://img.shields.io/badge/Claude-Anthropic-CC785C)
![License](https://img.shields.io/badge/License-MIT-green)

<!-- Optional: add a screenshot of the app here -->
<!-- ![App screenshot](./screenshot.png) -->

## Features

- 📋 Paste any email and get a drafted reply in your chosen tone
- 🎚️ Adjustable **tone** — Professional, Friendly, Formal, Casual, Assertive
- 📏 Adjustable **length** — Short, Medium, Detailed
- 🔀 Generate up to **3 reply variants** at once to choose from
- ✍️ Optionally add key points you want the reply to include
- 🔑 Bring your own Anthropic API key (entered securely in the sidebar)

## Getting started

### 1. Clone the repo

```bash
git clone https://github.com/iamchintanparmar/beginner-ai-agents/ai_email_reply_agent.git
cd ai_email_reply_agent
```

### 2. Install dependencies

```bash
pip install streamlit anthropic
```

Or, if you're using a `requirements.txt`:

```
streamlit
anthropic
```

```bash
pip install -r requirements.txt
```

### 3. Set your Anthropic API key (optional but recommended)

You can either enter your API key directly in the app's sidebar each time,
or set it once as an environment variable so it's pre-filled automatically:

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

Get an API key from the [Anthropic Console](https://console.anthropic.com/).

### 4. Run the app

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

## How to use

1. Paste the email you're replying to into the main text box.
2. (Optional) Add any key points you want the reply to cover.
3. Choose a **tone** and **length** from the sidebar.
4. Choose how many reply **variants** you want (1–3).
5. Click **Draft Replies** — Claude will generate your reply option(s) in
   Markdown, ready to copy into your inbox.

## Tech stack

| Layer | Technology |
| --- | --- |
| UI | [Streamlit](https://streamlit.io/) |
| AI | [Claude](https://www.anthropic.com/) via the [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python) |
| Model | `claude-sonnet-5` |

## Author

**Chintan Parmar** — Full-Stack Developer & Creative Technologist

- GitHub: [@iamchintanparmar](https://github.com/iamchintanparmar)
- Portfolio: [iamchintanparmar.github.io](https://iamchintanparmar.github.io)

## License

MIT
