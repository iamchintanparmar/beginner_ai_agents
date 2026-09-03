# 📊 AI Data Visualization Agent

A Streamlit application that acts as your personal data visualization expert, powered by LLMs. Simply upload your dataset and ask questions in natural language — the AI agent will analyze your data, generate appropriate visualizations, and provide insights through a combination of charts, statistics, and explanations.

## Features

#### Natural Language Data Analysis
- Ask questions about your data in plain English
- Get instant visualizations and statistical analysis
- Receive explanations of findings and insights
- Interactive follow-up questioning

#### Intelligent Visualization Selection
- Automatic choice of appropriate chart types
- Dynamic visualization generation
- Statistical visualization support
- Custom plot formatting and styling

#### Multi-Model AI Support
- Meta-Llama 3.1 405B for complex analysis
- DeepSeek V3 for detailed insights
- Qwen 2.5 7B for quick analysis
- Meta-Llama 3.3 70B for advanced queries

## How to Run

Follow the steps below to set up and run the application:

- Get a free Together AI API key here: https://api.together.ai/signin
- Get a free E2B API key here: https://e2b.dev/ (docs: https://e2b.dev/docs/legacy/getting-started/api-key)

1. **Clone the Repository**
   ```bash
   git clone https://github.com/coboat/Chintan-s-ai-Agents.git
   cd Chintan-s-ai-Agents/beginner_ai_agents/data_visualisation_agent
   ```

2. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**
   ```bash
   streamlit run data_visualisation_agent.py
   ```

## Usage

1. Launch the application using the command above.
2. Provide your Together AI and E2B API keys in the sidebar.
3. Upload your dataset (CSV or similar).
4. Ask questions about your data in natural language.
5. View the generated charts, statistics, and explanations.

## Troubleshooting

| Issue | Possible Cause | Fix |
|---|---|---|
| App won't start | Missing dependencies | Re-run `pip install -r requirements.txt` |
| No response / analysis fails | Invalid or missing Together AI / E2B API key | Re-check the keys entered in the sidebar |
| Visualization not generated | Unsupported or malformed dataset | Confirm the file is a valid, well-formatted CSV |

## Tech Stack

- **Frontend**: Streamlit
- **AI Models**: Meta-Llama 3.1 405B, DeepSeek V3, Qwen 2.5 7B, Meta-Llama 3.3 70B (via Together AI)
- **Code Execution / Sandboxing**: E2B