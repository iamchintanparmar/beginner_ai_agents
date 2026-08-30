## 📄 ➡️ ✅ Resume Optimizer Agent

This is a Streamlit-based application that scores how well your resume matches a job description and rewrites weak bullet points. The app uses Anthropic's Claude model to read your resume (PDF or DOCX) alongside a job posting and returns a match score, gap analysis, and improved bullet points.

## Features

- **Resume Parsing**: Extracts text from uploaded PDF or DOCX resumes.
- **Match Scoring**: Scores your resume against a job description on a 0–100 scale using Claude.
- **Gap Analysis**: Surfaces missing keywords and skills the job description calls for.
- **Bullet Rewrites**: Rewrites weak resume bullets to be more impactful and ATS-friendly.
- **API Key Integration**: Requires an Anthropic API key, entered securely via the sidebar.

## How It Works

1. The app extracts raw text from your uploaded resume file.
2. Your resume text and the job description are sent to Claude with a structured review prompt.
3. Claude returns a match score, top strengths, top gaps, and rewritten bullet points.
4. Results are rendered directly in the app.

## Setup

### Requirements

1. **API Key**:
   - **Anthropic API Key**: Sign up at [console.anthropic.com](https://console.anthropic.com/) to obtain your API key.
2. **Python 3.8+**: Ensure you have Python 3.8 or higher installed.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/coboat/Chintan-s-ai-Agents.git
   cd Chintan-s-ai-Agents/beginner_ai_agents/ai_resume_optimizer_agent
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
   - Upload your resume (PDF or DOCX).
   - Paste in the job description.
   - Click "Analyze Match".

## Usage Notes

- Only PDF and DOCX resumes are supported for upload.
- Scanned/image-based PDFs may not extract text correctly.
- Nothing is stored — re-upload your resume each session.

## Troubleshooting

| Issue | Possible Cause | Fix |
|---|---|---|
| No text extracted | Scanned or image-based PDF | Use a text-based PDF or DOCX instead |
| Analysis fails | Invalid or missing Anthropic API key | Re-check the key entered in the sidebar |
| Empty/short result | Job description too short | Paste the full job posting for better results |
| App won't start | Missing dependencies | Re-run `pip install -r requirements.txt` |

## Tech Stack

- **Frontend**: Streamlit
- **File Parsing**: pypdf, python-docx
- **Analysis**: Anthropic Claude
