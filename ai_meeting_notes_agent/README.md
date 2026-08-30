## 🎙️ ➡️ 🗒️ Meeting Notes Agent

This is a Streamlit-based application that converts a raw meeting transcript into clean, structured notes. The app uses Anthropic's Claude model to extract a summary, key decisions, action items, and open questions from any pasted or uploaded transcript.


Created and developed by **[Chintan Parmar](https://github.com/iamchintanparmar)**.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![AI Agents](https://img.shields.io/badge/AI-Agents-8b6bff)
![License](https://img.shields.io/badge/License-MIT-green)


## Features

- **Transcript Input**: Paste a transcript directly or upload a `.txt` file.
- **Structured Output**: Produces Summary, Key Decisions, Action Items, and Open Questions sections.
- **Owner Detection**: Attributes action items to the person mentioned, when identifiable.
- **Detail Control**: Choose Brief, Standard, or Comprehensive output.
- **API Key Integration**: Requires an Anthropic API key, entered securely via the sidebar.

## How It Works

1. You paste in a transcript or upload a `.txt` file.
2. The transcript and detail level are combined into a structured summarization prompt.
3. Claude extracts the summary, decisions, action items, and open questions.
4. Results are rendered directly in the app.

## Setup

### Requirements

1. **API Key**:
   - **Anthropic API Key**: Sign up at [console.anthropic.com](https://console.anthropic.com/) to obtain your API key.
2. **Python 3.8+**: Ensure you have Python 3.8 or higher installed.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/iamchintanparmar/beginner_ai_agents/ai_meeting_notes_agent.git
   cd ai_meeting_notes_agent
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

1. Start the Streamlit app:
   ```bash
   streamlit run main.py
   ```

2. In the app interface:
   - Enter your Anthropic API key in the sidebar.
   - Set the desired detail level.
   - Upload a transcript file or paste it in directly.
   - Click "Generate Notes".

## Usage Notes

- Only `.txt` transcript files are supported for upload.
- Very long transcripts may be truncated by the model's context limit.
- Nothing is stored — re-upload or re-paste the transcript each session.

## Troubleshooting

| Issue | Possible Cause | Fix |
|---|---|---|
| Generation fails | Invalid or missing Anthropic API key | Re-check the key entered in the sidebar |
| Action items missing owners | Speakers not clearly labeled in transcript | Include speaker names in the transcript text |
| Notes too sparse | Detail level set to Brief | Switch to Standard or Comprehensive |
| App won't start | Missing dependencies | Re-run `pip install -r requirements.txt` |

## Tech Stack

- **Frontend**: Streamlit
- **Summarization**: Anthropic Claude

## Author

**Chintan Parmar** — Full-Stack Developer & Creative Technologist

- GitHub: [@iamchintanparmar](https://github.com/iamchintanparmar)
- Portfolio: [iamchintanparmar.github.io](https://iamchintanparmar.github.io)

## License

MIT
