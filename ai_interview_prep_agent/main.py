import os
import streamlit as st
from anthropic import Anthropic
from pypdf import PdfReader

st.set_page_config(page_title="AI Interview Prep Agent", page_icon="🎤")
st.title("🎤 AI Interview Prep Agent")
st.caption("Powered by Claude — practice interview questions tailored to the role")

api_key = st.sidebar.text_input(
    "Anthropic API Key",
    type="password",
    value=os.environ.get("ANTHROPIC_API_KEY", ""),
)

num_questions = st.sidebar.slider("Number of questions", 3, 10, 5)
difficulty = st.sidebar.selectbox("Difficulty", ["Entry-level", "Mid-level", "Senior", "Executive"])

job_title = st.text_input("Job title", placeholder="e.g. Senior Product Manager")
job_description = st.text_area("Job description (optional)", height=150)
resume_file = st.file_uploader("Upload your resume for tailored questions (optional, PDF)", type=["pdf"])

if st.button("Generate Interview Questions", type="primary"):
    if not api_key:
        st.error("Please provide your Anthropic API key in the sidebar.")
    elif not job_title.strip():
        st.error("Please enter a job title.")
    else:
        with st.spinner("Preparing your mock interview..."):
            resume_text = ""
            if resume_file:
                reader = PdfReader(resume_file)
                resume_text = "\n".join(page.extract_text() or "" for page in reader.pages)

            client = Anthropic(api_key=api_key)

            prompt = f"""You are an experienced hiring manager preparing a mock interview.

Job Title: {job_title}
Difficulty: {difficulty}
Job Description: {job_description or "Not provided"}
Candidate Resume: {resume_text or "Not provided"}

Generate {num_questions} realistic interview questions for this role, mixing behavioral and technical/role-specific questions as appropriate. For each question, include a short note on what a strong answer should cover.

Format as markdown with numbered questions."""

            response = client.messages.create(
                model="claude-sonnet-5",
                max_tokens=1500,
                messages=[{"role": "user", "content": prompt}],
            )
            result = response.content[0].text

        st.markdown("---")
        st.markdown(result)
