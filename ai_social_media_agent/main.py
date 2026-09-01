import os
import streamlit as st
from anthropic import Anthropic

st.set_page_config(page_title="AI Social Media Agent", page_icon="📱")
st.title("📱 AI Social Media Agent")
st.caption("Powered by Claude — turn any content into platform-ready posts")

api_key = st.sidebar.text_input(
    "Anthropic API Key",
    type="password",
    value=os.environ.get("ANTHROPIC_API_KEY", ""),
)

platforms = st.sidebar.multiselect(
    "Platforms",
    ["X / Twitter", "LinkedIn", "Instagram", "Facebook", "TikTok"],
    default=["X / Twitter", "LinkedIn"],
)
tone = st.sidebar.selectbox("Tone", ["Professional", "Casual", "Witty", "Inspirational", "Bold"])
include_hashtags = st.sidebar.checkbox("Include hashtags", value=True)

source_content = st.text_area("Paste the content, article, or idea to repurpose", height=250)

if st.button("Generate Posts", type="primary"):
    if not api_key:
        st.error("Please provide your Anthropic API key in the sidebar.")
    elif not source_content.strip():
        st.error("Paste some content first.")
    elif not platforms:
        st.error("Select at least one platform.")
    else:
        with st.spinner("Writing your posts..."):
            client = Anthropic(api_key=api_key)

            hashtag_instruction = "Include 3-5 relevant hashtags per post." if include_hashtags else "Do not include hashtags."

            prompt = f"""You are a social media copywriter repurposing content across platforms.

Source content:
---
{source_content}
---

Tone: {tone}
Platforms: {", ".join(platforms)}
{hashtag_instruction}

Write one post per selected platform, respecting each platform's typical length and style conventions. Use a '### Platform Name' header before each post."""

            response = client.messages.create(
                model="claude-sonnet-5",
                max_tokens=1500,
                messages=[{"role": "user", "content": prompt}],
            )
            result = response.content[0].text

        st.markdown("---")
        st.markdown(result)
