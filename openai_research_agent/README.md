# 🔎 OpenAI Researcher Agent

A multi-agent research application built with OpenAI's Agents SDK and Streamlit. This application enables users to conduct comprehensive research on any topic by leveraging multiple specialized AI agents.


Created and developed by **[Chintan Parmar](https://github.com/iamchintanparmar)**.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![AI Agents](https://img.shields.io/badge/AI-Agents-8b6bff)
![License](https://img.shields.io/badge/License-MIT-green)


## Features

- **Multi-Agent Architecture**:
  - **Triage Agent**: Plans the research approach and coordinates the workflow.
  - **Research Agent**: Searches the web and gathers relevant information.
  - **Editor Agent**: Compiles collected facts into a comprehensive report.

- **Automatic Fact Collection**: Captures important facts from research with source attribution.
- **Structured Report Generation**: Creates well-organized reports with titles, outlines, and source citations.
- **Interactive UI**: Built with Streamlit for easy research topic input and results viewing.
- **Tracing and Monitoring**: Integrated tracing for the entire research workflow.

## How to Get Started

1. Clone the repository:
   ```bash
   git clone https://github.com/iamchintanparmar/beginner_ai_agents.git
   cd beginner_ai_agents/openai_research_agent
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Get your OpenAI API key:
   - Sign up for an [OpenAI account](https://platform.openai.com/) and obtain your API key.
   - Set your `OPENAI_API_KEY` environment variable:
     ```bash
     export OPENAI_API_KEY='your-api-key-here'
     ```

4. Run the team of AI agents:
   ```bash
   streamlit run research_agent.py
   ```

   Then open your browser and navigate to the URL shown in the terminal (typically `http://localhost:8501`).

## Research Process

1. Enter a research topic in the sidebar, or select one of the provided examples.
2. Click "Start Research" to begin the process.
3. View the research process in real-time on the "Research Process" tab.
4. Once complete, switch to the "Report" tab to view and download the generated report.

## Troubleshooting

| Issue | Possible Cause | Fix |
|---|---|---|
| App won't start | Missing dependencies | Re-run `pip install -r requirements.txt` |
| No report generated | Invalid or missing `OPENAI_API_KEY` | Re-check the environment variable is set correctly |
| Research stalls | Network issue during web search | Retry, or try a narrower research topic |

## Tech Stack

- **Frontend**: Streamlit
- **Agent Framework**: OpenAI Agents SDK
- **AI Model**: OpenAI GPT

## Author

**Chintan Parmar** — Full-Stack Developer & Creative Technologist

- GitHub: [@iamchintanparmar](https://github.com/iamchintanparmar)
- Portfolio: [iamchintanparmar.github.io](https://iamchintanparmar.github.io)

## License

MIT
