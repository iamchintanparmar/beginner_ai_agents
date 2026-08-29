## 💻 ➡️ 🔍 Code Review Agent

This is a Streamlit-based application that performs an automated, PR-style review of any code snippet or file. The app uses Anthropic's Claude model to flag bugs, security issues, style problems, and performance improvements, with an optional mode to return a corrected version of the code.

## Features

- **Code Input**: Paste code directly or upload a source file in any language.
- **Severity-Ranked Findings**: Groups issues into Critical, Warning, and Suggestion sections.
- **Reasoning Included**: Explains why each finding matters, not just what to change.
- **Auto-Fix Mode**: Optionally returns a corrected version of the full code snippet.
- **API Key Integration**: Requires an Anthropic API key, entered securely via the sidebar.

## How It Works

1. You paste code or upload a source file.
2. The code, along with an optional language hint, is sent to Claude with a structured review prompt.
3. Claude returns findings grouped by severity, plus a corrected version if auto-fix mode is enabled.
4. Results are rendered directly in the app.

## Setup

### Requirements

1. **API Key**:
   - **Anthropic API Key**: Sign up at [console.anthropic.com](https://console.anthropic.com/) to obtain your API key.
2. **Python 3.8+**: Ensure you have Python 3.8 or higher installed.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/iamchintanparmar/beginner_ai_agents/ai_code_review_agent.git
   cd ai_code_review_agent
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
   - Optionally specify the language and enable auto-fix mode.
   - Paste code or upload a source file.
   - Click "Review Code".

## Usage Notes

- Language detection is automatic if not specified, but naming it improves accuracy.
- Very large files may be truncated by the model's context limit.
- Nothing is stored — re-paste or re-upload code each session.

## Troubleshooting

| Issue | Possible Cause | Fix |
|---|---|---|
| Review fails | Invalid or missing Anthropic API key | Re-check the key entered in the sidebar |
| Findings seem generic | Language not specified | Set the language field in the sidebar |
| Corrected code missing | Auto-fix mode not enabled | Check "Also return a corrected version" before reviewing |
| App won't start | Missing dependencies | Re-run `pip install -r requirements.txt` |

## Tech Stack

- **Frontend**: Streamlit
- **Review Engine**: Anthropic Claude


## Author
 
**Chintan Parmar** — Full-Stack Developer & Creative Technologist
 
- GitHub: [@iamchintanparmar](https://github.com/iamchintanparmar)
- Portfolio: [iamchintanparmar.github.io](https://iamchintanparmar.github.io)
## License
 
MIT
 
