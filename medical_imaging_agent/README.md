# 🩻 Medical Imaging Diagnosis Agent

A Medical Imaging Diagnosis Agent built on Agno, powered by Gemini 2.0 Flash, that provides AI-assisted analysis of medical images and scans. The agent acts as a medical imaging diagnosis expert to analyze various types of medical images and videos, providing detailed diagnostic insights and explanations.

## Features

- **Comprehensive Image Analysis**
- Image Type Identification (X-ray, MRI, CT scan, ultrasound)
- Anatomical Region Detection
- Key Findings and Observations
- Potential Abnormalities Detection
- Image Quality Assessment
- Research and Reference

## How to Run

1. **Setup Environment**
   ```bash
   # Clone the repository
   git clone https://github.com/coboat/Chintan-s-ai-Agents.git
   cd Chintan-s-ai-Agents/beginner_ai_agents/medical_imaging_agent

   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Configure API Keys**
   - Get a Google API key from [Google AI Studio](https://aistudio.google.com)

3. **Run the Application**
   ```bash
   streamlit run medical_imaging.py
   ```

## Analysis Components

- **Image Type and Region**
- Identifies imaging modality
- Specifies anatomical region

- **Key Findings**
- Systematic listing of observations
- Detailed appearance descriptions
- Abnormality highlighting

- **Diagnostic Assessment**
- Potential diagnoses ranking
- Differential diagnoses
- Severity assessment

- **Patient-Friendly Explanations**
- Simplified terminology
- Detailed first-principles explanations
- Visual reference points

## Notes

- Uses Gemini 2.0 Flash for analysis.
- Requires a stable internet connection.
- Free-tier usage: up to 1,500 free requests per day via Google's free API tier (subject to change — check Google AI Studio for current limits).
- For educational and development purposes only.
- Not a replacement for professional medical diagnosis.

## Troubleshooting

| Issue | Possible Cause | Fix |
|---|---|---|
| App won't start | Missing dependencies | Re-run `pip install -r requirements.txt` |
| No analysis returned | Invalid or missing Google API key | Re-check the key entered in the sidebar |
| Analysis fails on image | Unsupported file type or corrupted image | Confirm the file is a valid, readable image format |
| Daily quota exceeded | Free-tier request limit reached | Wait for quota reset or upgrade your Google API plan |

## Tech Stack

- **Frontend**: Streamlit
- **Agent Framework**: Agno
- **AI Model**: Gemini 2.0 Flash

## Disclaimer

This tool is for educational and informational purposes only. All analyses should be reviewed by qualified healthcare professionals. Do not make medical decisions based solely on this analysis.