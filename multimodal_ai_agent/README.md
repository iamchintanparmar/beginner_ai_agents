## 🧬 Multimodal AI Agent

A Streamlit application that combines video analysis and web search capabilities using Google's Gemini 2.5 model. This agent can analyze uploaded videos and answer questions by combining visual understanding with web search.

Created and developed by **[Chintan Parmar](https://github.com/iamchintanparmar)**.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![AI Agents](https://img.shields.io/badge/AI-Agents-8b6bff)
![License](https://img.shields.io/badge/License-MIT-green)


### Features

- Video analysis using Gemini 2.5 Flash/Pro
- Web research integration via DuckDuckGo
- Support for multiple video formats (MP4, MOV, AVI)
- Real-time video processing
- Combined visual and textual analysis

### How to Get Started

1. Clone the repository:
   ```bash
   git clone https://github.com/iamchintanparmar/beginner_ai_agents.git
   cd beginner_ai_agents/multimodal_ai_agent
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Get your Google Gemini API key:
   - Sign up for a [Google AI Studio account](https://aistudio.google.com/apikey) and obtain your API key.

4. Set up your Gemini API key as an environment variable:
   ```bash
   GOOGLE_API_KEY=your_api_key_here
   ```

5. Run the Streamlit app:
   ```bash
   streamlit run multimodal_agent.py
   ```

## Usage

1. Launch the application using the command above.
2. Upload a video file (MP4, MOV, or AVI).
3. Ask a question about the video's content.
4. The agent analyzes the video and, if needed, pulls in additional context via web search.
5. View the combined visual and textual answer.

## Troubleshooting

| Issue | Possible Cause | Fix |
|---|---|---|
| App won't start | Missing dependencies | Re-run `pip install -r requirements.txt` |
| No response | Invalid or missing `GOOGLE_API_KEY` | Re-check the environment variable is set correctly |
| Video won't upload | Unsupported format | Confirm the file is `.mp4`, `.mov`, or `.avi` |
| Slow processing | Large video file size | Try a shorter or lower-resolution clip |

## Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini 2.5 Flash/Pro
- **Web Search**: DuckDuckGo

## Author

**Chintan Parmar** — Full-Stack Developer & Creative Technologist

- GitHub: [@iamchintanparmar](https://github.com/iamchintanparmar)
- Portfolio: [iamchintanparmar.github.io](https://iamchintanparmar.github.io)

## License

MIT
