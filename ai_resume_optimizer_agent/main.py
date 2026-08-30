import os
import streamlit as st
from anthropic import Anthropic
from pypdf import PdfReader
from docx import Document

st.set_page_config(page_title="AI Resume Optimizer Agent", page_icon="📄")
st.title("📄 AI Resume Optimizer Agent")
st.caption("Powered by Claude — match your resume to any job description")

api_key = st.sidebar.text_input(
    "Anthropic API Key",
    type="password",
    value=os.environ.get("ANTHROPIC_API_KEY", ""),
)

def extract_text(uploaded_file):
    if uploaded_file.name.lower().endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    elif uploaded_file.name.lower().endswith(".docx"):
        doc = Document(uploaded_file)
        return "\n".join(p.text for p in doc.paragraphs)
    return uploaded_file.read().decode("utf-8", errors="ignore")

resume_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
job_description = st.text_area("Paste the job description", height=250)

if st.button("Analyze Match", type="primary"):
    if not api_key:
        st.error("Please provide your Anthropic API key in the sidebar.")
    elif not resume_file or not job_description.strip():
        st.error("Please upload a resume and paste a job description.")
    else:
        with st.spinner("Analyzing your resume against the job description..."):
            resume_text = extract_text(resume_file)
            client = Anthropic(api_key=api_key)

            prompt = f"""You are an expert resume reviewer and ATS optimization specialist.

Resume:
---
{resume_text}
---

Job Description:
---
{job_description}
---

Provide:
1. A match score out of 100 with a one-line justification.
2. Top 3 strengths that align well with the role.
3. Top 3 gaps or missing keywords/skills compared to the job description.
4. 3-5 rewritten resume bullet points (pick the weakest existing ones) that are more impactful, quantified, and ATS-friendly.

Format your response in clear markdown with headers."""

            response = client.messages.create(
                model="claude-sonnet-5",
                max_tokens=1500,
                messages=[{"role": "user", "content": prompt}],
            )
            result = response.content[0].text

        st.markdown("---")
        st.markdown(result)
