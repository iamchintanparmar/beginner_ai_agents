import os
import streamlit as st
from anthropic import Anthropic

st.set_page_config(page_title="AI Meeting Notes Agent", page_icon="🗒️")
st.title("🗒️ AI Meeting Notes Agent")
st.caption("Powered by Claude — turn raw transcripts into clean notes and action items")

api_key = st.sidebar.text_input(
    "Anthropic API Key",
    type="password",
    value=os.environ.get("ANTHROPIC_API_KEY", ""),
)

detail_level = st.sidebar.selectbox("Detail level", ["Brief", "Standard", "Comprehensive"])

transcript_file = st.file_uploader("Upload a transcript file (.txt)", type=["txt"])
transcript_text = st.text_area("Or paste the transcript here", height=300)

if st.button("Generate Notes", type="primary"):
    transcript = ""
    if transcript_file:
        transcript = transcript_file.read().decode("utf-8", errors="ignore")
    elif transcript_text.strip():
        transcript = transcript_text

    if not api_key:
        st.error("Please provide your Anthropic API key in the sidebar.")
    elif not transcript.strip():
        st.error("Upload or paste a transcript first.")
    else:
        with st.spinner("Summarizing the meeting..."):
            client = Anthropic(api_key=api_key)

            prompt = f"""You are an executive assistant summarizing a meeting transcript.

Transcript:
---
{transcript}
---

Detail level: {detail_level}

Produce markdown output with these sections:
## Summary
## Key Decisions
## Action Items (with owner if mentioned)
## Open Questions"""

            response = client.messages.create(
                model="claude-sonnet-5",
                max_tokens=2000,
                messages=[{"role": "user", "content": prompt}],
            )
            result = response.content[0].text

        st.markdown("---")
        st.markdown(result)
