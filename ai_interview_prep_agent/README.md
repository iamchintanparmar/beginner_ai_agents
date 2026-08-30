## 💼 ➡️ 🎤 Interview Prep Agent

This is a Streamlit-based application that generates a tailored mock interview for any job title. The app uses Anthropic's Claude model, optionally combined with your resume and a job description, to produce realistic behavioral and role-specific questions along with notes on what a strong answer should cover.

Created and developed by **[Chintan Parmar](https://github.com/iamchintanparmar)**.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![AI Agents](https://img.shields.io/badge/AI-Agents-8b6bff)
![License](https://img.shields.io/badge/License-MIT-green)



## Features

- **Tailored Questions**: Generates interview questions specific to a job title and difficulty level.
- **Resume-Aware**: Optionally reads an uploaded PDF resume to personalize questions further.
- **Job Description Matching**: Optionally incorporates a job posting for more targeted questions.
- **Answer Guidance**: Each question includes notes on what a strong answer should cover.
- **API Key Integration**: Requires an Anthropic API key, entered securely via the sidebar.

## How It Works

1. You enter a job title, and optionally a job description and/or resume.
2. If a resume is uploaded, its text is extracted from the PDF.
3. All inputs are combined into a prompt sent to Claude.
4. Claude returns a set of numbered interview questions with guidance, rendered in the app.

## Setup

### Requirements

1. **API Key**:
   - **Anthropic API Key**: Sign up at [console.anthropic.com](https://console.anthropic.com/) to obtain your API key.
2. **Python 3.8+**: Ensure you have Python 3.8 or higher installed.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/iamchintanparmar/beginner_ai_agents/ai_interview_prep_agent.git
   cd ai_interview_prep_agent
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
   - Set the number of questions and difficulty level.
   - Enter a job title, and optionally a job description and/or resume.
   - Click "Generate Interview Questions".

## Usage Notes

- Only PDF resumes are supported for upload.
- Questions are generated fresh each time — re-run for a different set.
- Nothing is stored — re-upload your resume each session.

## Troubleshooting

| Issue | Possible Cause | Fix |
|---|---|---|
| Generation fails | Invalid or missing Anthropic API key | Re-check the key entered in the sidebar |
| Resume ignored | Scanned or image-based PDF | Use a text-based PDF resume |
| Questions too generic | No job description provided | Add a job description for more targeted questions |
| App won't start | Missing dependencies | Re-run `pip install -r requirements.txt` |

## Tech Stack

- **Frontend**: Streamlit
- **File Parsing**: pypdf
- **Generation**: Anthropic Claude

## Author

**Chintan Parmar** — Full-Stack Developer & Creative Technologist

- GitHub: [@iamchintanparmar](https://github.com/iamchintanparmar)
- Portfolio: [iamchintanparmar.github.io](https://iamchintanparmar.github.io)

## License

MIT
