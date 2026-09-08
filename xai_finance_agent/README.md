## 📊 AI Finance Agent with xAI Grok

This application creates a financial analysis agent powered by xAI's Grok model, combining real-time stock data with web search capabilities. It provides structured financial insights through an interactive playground interface.

## Features

- Powered by xAI's Grok-4 Fast model
- Real-time stock data analysis via YFinance
- Web search capabilities through DuckDuckGo
- Formatted output with tables for financial data
- Interactive playground interface

## How to Get Started

1. Clone the repository:
   ```bash
   git clone https://github.com/coboat/Chintan-s-ai-Agents.git
   cd Chintan-s-ai-Agents/beginner_ai_agents/xai_finance_agent
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Get your xAI API key:
   - Sign up for an [xAI API account](https://console.x.ai/)
   - Set your `XAI_API_KEY` environment variable:
     ```bash
     export XAI_API_KEY='your-api-key-here'
     ```

4. Run the AI agent:
   ```bash
   python xai_finance_agent.py
   ```

5. Open your web browser and navigate to the URL provided in the console output to interact with the AI financial agent through the playground interface.

## Connecting Your AgentOS

To manage, monitor, and interact with your financial agent through the AgentOS Control Plane (from your browser), you need to connect your running AgentOS instance:

- Visit the official documentation: [Connecting Your OS](https://docs.agno.com/agent-os/connecting-your-os)
- Follow the steps in the guide to register your local AgentOS and establish the connection.

## Troubleshooting

| Issue | Possible Cause | Fix |
|---|---|---|
| App won't start | Missing dependencies | Re-run `pip install -r requirements.txt` |
| No response | Invalid or missing `XAI_API_KEY` | Re-check the environment variable is set correctly |
| No stock data returned | Invalid ticker symbol or YFinance rate limiting | Confirm the ticker is correct and retry |
| Playground won't connect | AgentOS not registered | Follow the "Connecting Your AgentOS" steps above |

## Tech Stack

- **AI Model**: xAI Grok-4 Fast
- **Stock Data**: YFinance
- **Web Search**: DuckDuckGo
- **Agent Platform**: AgentOS