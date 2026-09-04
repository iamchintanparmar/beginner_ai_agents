# 🛡️ Life Insurance Coverage Advisor Agent

A Streamlit application that helps users estimate the amount of term life insurance they may need and surfaces currently available policy options. The app is powered by the **Agno** agent framework, uses **OpenAI GPT-5** as the LLM, the **E2B** sandbox for deterministic coverage calculations, and **Firecrawl** for live web research.

Created and developed by **[Chintan Parmar](https://github.com/iamchintanparmar)**.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![AI Agents](https://img.shields.io/badge/AI-Agents-8b6bff)
![License](https://img.shields.io/badge/License-MIT-green)

## Highlights

- Minimal intake form (age, income, dependents, debt, assets, existing cover, horizon, location).
- The agent runs Python code inside an E2B sandbox to calculate coverage with a discounted cash-flow style income replacement model.
- Firecrawl search is used to gather the latest term-life products for the user's geography and coverage needs.
- Returns a concise coverage estimate, calculation breakdown, and up to three product suggestions with source links.

## Prerequisites

You will need API keys for each external service:

| Service | Purpose | Where to get it |
| --- | --- | --- |
| OpenAI (GPT-5-mini) | Core reasoning model | https://platform.openai.com/api-keys |
| Firecrawl | Web search + crawl tooling | https://www.firecrawl.dev/app/api-keys |
| E2B | Secure code execution sandbox | https://e2b.dev |

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/iamchintanparmar/beginner_ai_agents.git
   cd beginner_ai_agents/life_insurance_advisor_agent
   ```

2. Create and activate a virtual environment (optional but recommended).

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run insurance_advisor_agent.py
   ```

## Using the App

1. Enter your OpenAI, Firecrawl, and E2B API keys in the sidebar (keys are kept in the local Streamlit session).
2. Provide the requested financial information and choose an income replacement horizon.
3. Click **Generate Coverage & Options** to launch the Agno agent workflow.
4. Review the recommended coverage, rationale, and suggested insurers. Raw agent output is available in an expander for debugging.

## Troubleshooting

| Issue | Possible Cause | Fix |
|---|---|---|
| App won't start | Missing dependencies | Re-run `pip install -r requirements.txt` |
| Coverage calculation fails | Invalid or missing E2B API key | Re-check the key entered in the sidebar |
| No product suggestions returned | Invalid Firecrawl key, or no matching results for the region | Re-check the key, or try a broader location |
| Agent gives no response | Invalid or missing OpenAI API key | Re-check the key entered in the sidebar |

## Tech Stack

- **Frontend**: Streamlit
- **Agent Framework**: Agno
- **AI Model**: OpenAI GPT-5
- **Code Execution / Sandboxing**: E2B
- **Web Research**: Firecrawl

## Disclaimer

This project is for educational and prototyping purposes only and does **not** provide licensed financial advice. Always validate the output with a qualified professional and confirm details directly with insurance providers.


## Author

**Chintan Parmar** — Full-Stack Developer & Creative Technologist

- GitHub: [@iamchintanparmar](https://github.com/iamchintanparmar)
- Portfolio: [iamchintanparmar.github.io](https://iamchintanparmar.github.io)

## License

MIT
