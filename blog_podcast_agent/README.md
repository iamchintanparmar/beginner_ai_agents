## 📰 ➡️ 🎙️ Blog to Podcast Agent

This is a Streamlit-based application that allows users to convert any blog post into a podcast. The app uses OpenAI's GPT-4 model for summarization, Firecrawl for scraping blog content, and ElevenLabs API for generating audio. Users simply input a blog URL, and the app will generate a podcast episode based on the blog.

## Features

- **Blog Scraping**: Scrapes the full content of any public blog URL using the Firecrawl API.
- **Summary Generation**: Creates an engaging and concise summary of the blog (within 2000 characters) using OpenAI GPT-4.
- **Podcast Generation**: Converts the summary into an audio podcast using the ElevenLabs voice API.
- **API Key Integration**: Requires OpenAI, Firecrawl, and ElevenLabs API keys to function, entered securely via the sidebar.
- **Playback and Download**: Listen to the generated podcast directly in the app, or download the audio file for later use.

## How It Works

1. The app scrapes the target blog URL using Firecrawl to extract the full text content.
2. GPT-4 condenses that content into a short, engaging summary suitable for narration.
3. The summary is sent to ElevenLabs, which converts it into natural-sounding speech.
4. The resulting audio file is returned to the app for playback or download.

## Setup

### Requirements

1. **API Keys**:
   - **OpenAI API Key**: Sign up at OpenAI to obtain your API key.
   - **ElevenLabs API Key**: Get your ElevenLabs API key from ElevenLabs.
   - **Firecrawl API Key**: Get your Firecrawl API key from Firecrawl.
2. **Python 3.8+**: Ensure you have Python 3.8 or higher installed.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/coboat/Chintan-s-ai-Agents.git
   cd Chintan-s-ai-Agents/beginner_ai_agents/blog_podcast_agent
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

1. Start the Streamlit app:
   ```bash
   streamlit run blog_podcast_agent.py
   ```

2. In the app interface:
   - Enter your OpenAI, ElevenLabs, and Firecrawl API keys in the sidebar.
   - Input the blog URL you want to convert.
   - Click "🎙️ Generate Podcast".
   - Listen to the generated podcast or download it.

## Usage Notes

- Only publicly accessible blog URLs can be scraped; pages behind a login or paywall are not supported.
- Summaries are capped at 2000 characters to keep the generated audio to a reasonable length.
- Generated audio files are not stored permanently — download them if you want to keep a copy.

## Troubleshooting

| Issue | Possible Cause | Fix |
|---|---|---|
| Scraping fails | Invalid or private blog URL | Confirm the URL is public and correctly formatted |
| Summary generation fails | Invalid or missing OpenAI API key | Re-check the key entered in the sidebar |
| No audio generated | Invalid ElevenLabs API key or quota exceeded | Verify the key and check your ElevenLabs usage limits |
| App won't start | Missing dependencies | Re-run `pip install -r requirements.txt` |

## Tech Stack

- **Frontend**: Streamlit
- **Scraping**: Firecrawl API
- **Summarization**: OpenAI GPT-4
- **Text-to-Speech**: ElevenLabs API
