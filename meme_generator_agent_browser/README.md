# 🥸 AI Meme Generator Agent - Browser Use

The AI Meme Generator Agent is a powerful browser automation tool that creates memes using AI agents. This app combines multi-LLM capabilities with automated browser interactions to generate memes based on text prompts through direct website manipulation.


Created and developed by **[Chintan Parmar](https://github.com/iamchintanparmar)**.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![AI Agents](https://img.shields.io/badge/AI-Agents-8b6bff)
![License](https://img.shields.io/badge/License-MIT-green)


## Features

- **Multi-LLM Support**
- Claude 3.5 Sonnet (Anthropic)
- GPT-4o (OpenAI)
- DeepSeek V3 (DeepSeek)
- Automatic model switching with API key validation

- **Browser Automation**:
- Direct interaction with imgflip.com meme templates
- Automated search for relevant meme formats
- Dynamic text insertion for top/bottom captions
- Image link extraction from generated memes

- **Smart Generation Workflow**:
- Action verb extraction from prompts
- Metaphorical template matching
- Multi-step quality validation
- Automatic retry mechanism for failed generations

- **User-Friendly Interface**:
- Model configuration sidebar
- API key management
- Direct meme preview with clickable links
- Responsive error handling

## Prerequisites

API keys required:
- **Anthropic** (for Claude)
- **DeepSeek**
- **OpenAI** (for GPT-4o)

## How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/iamchintanparmar/beginner_ai_agents.git
   cd beginner_ai_agents/meme_generator_agent_browser
   ```

2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Install `playwright` if needed:
   ```bash
   python -m playwright install --with-deps
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run meme_generator_agent.py
   ```

## Usage

1. Launch the application using the command above.
2. Enter your Anthropic, OpenAI, and/or DeepSeek API keys in the sidebar.
3. Select which model you want to use.
4. Enter a text prompt describing the meme you want.
5. The agent searches imgflip.com, picks a matching template, and inserts your captions.
6. View the generated meme and its link in the app.

## Troubleshooting

| Issue | Possible Cause | Fix |
|---|---|---|
| App won't start | Missing dependencies | Re-run `pip install -r requirements.txt` |
| Browser automation fails | Playwright not installed | Run `python -m playwright install --with-deps` |
| No meme generated | Invalid or missing API key for selected model | Re-check the key entered in the sidebar |
| Generation retries repeatedly | No matching template found for the prompt | Try a more specific or common meme concept |

## Tech Stack

- **Frontend**: Streamlit
- **Browser Automation**: Playwright
- **AI Models**: Claude 3.5 Sonnet, GPT-4o, DeepSeek V3


## Author

**Chintan Parmar** — Full-Stack Developer & Creative Technologist

- GitHub: [@iamchintanparmar](https://github.com/iamchintanparmar)
- Portfolio: [iamchintanparmar.github.io](https://iamchintanparmar.github.io)

## License

MIT
