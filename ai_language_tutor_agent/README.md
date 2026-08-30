## 🗣️ ➡️ 🎓 Language Tutor Agent

This is a Streamlit-based application that lets you practice conversational skills in any language. The app uses Anthropic's Claude model to role-play a chosen scenario with you, correcting mistakes and introducing new vocabulary after each exchange.

Created and developed by **[Chintan Parmar](https://github.com/iamchintanparmar)**.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![AI Agents](https://img.shields.io/badge/AI-Agents-8b6bff)
![License](https://img.shields.io/badge/License-MIT-green)


## Features

- **Live Roleplay**: Holds a real conversation in your target language within a chosen scenario.
- **Level-Aware**: Adjusts vocabulary and sentence complexity to Beginner, Intermediate, or Advanced.
- **Corrections**: Flags mistakes from your last message after each reply.
- **Vocabulary Building**: Surfaces 2-3 new useful words or phrases per exchange.
- **API Key Integration**: Requires an Anthropic API key, entered securely via the sidebar.

## How It Works

1. You set a target language, your level, and a conversation scenario.
2. You chat with the tutor using the chat input box.
3. Claude replies in character, mostly in the target language, then adds an English section with corrections and new vocabulary.
4. The conversation history persists until you start a new one.

## Setup

### Requirements

1. **API Key**:
   - **Anthropic API Key**: Sign up at [console.anthropic.com](https://console.anthropic.com/) to obtain your API key.
2. **Python 3.8+**: Ensure you have Python 3.8 or higher installed.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/iamchintanparmar/beginner_ai_agents/ai_language_tutor_agent.git
   cd ai_language_tutor_agent
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
   - Set your target language, level, and scenario.
   - Type a reply in the chat box to begin.
   - Click "Start New Conversation" to reset at any time.

## Usage Notes

- Conversation history is kept only for the current session — it resets when the app restarts.
- Changing the scenario or level mid-conversation won't retroactively update past messages.
- Corrections apply to your most recent message only.

## Troubleshooting

| Issue | Possible Cause | Fix |
|---|---|---|
| Reply fails | Invalid or missing Anthropic API key | Re-check the key entered in the sidebar |
| Tutor breaks character | Very long conversation history | Click "Start New Conversation" to reset |
| Corrections missing | No mistakes detected in your message | This is expected when your message is already correct |
| App won't start | Missing dependencies | Re-run `pip install -r requirements.txt` |

## Tech Stack

- **Frontend**: Streamlit
- **Conversation**: Anthropic Claude


## Author

**Chintan Parmar** — Full-Stack Developer & Creative Technologist

- GitHub: [@iamchintanparmar](https://github.com/iamchintanparmar)
- Portfolio: [iamchintanparmar.github.io](https://iamchintanparmar.github.io)

## License

MIT
