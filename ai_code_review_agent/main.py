import os
import streamlit as st
from anthropic import Anthropic

st.set_page_config(page_title="AI Code Review Agent", page_icon="🧑‍💻")
st.title("🧑‍💻 AI Code Review Agent")
st.caption("Powered by Claude — automated PR-style code review")

api_key = st.sidebar.text_input(
    "Anthropic API Key",
    type="password",
    value=os.environ.get("ANTHROPIC_API_KEY", ""),
)

language = st.sidebar.text_input("Language (optional, helps accuracy)", placeholder="e.g. Python, JavaScript")
fix_mode = st.sidebar.checkbox("Also return a corrected version of the code")

uploaded_file = st.file_uploader("Upload a source file (optional)")
code_input = st.text_area("Or paste code here", height=350)

if st.button("Review Code", type="primary"):
    code = ""
    if uploaded_file:
        code = uploaded_file.read().decode("utf-8", errors="ignore")
    elif code_input.strip():
        code = code_input

    if not api_key:
        st.error("Please provide your Anthropic API key in the sidebar.")
    elif not code.strip():
        st.error("Paste some code or upload a file first.")
    else:
        with st.spinner("Reviewing your code..."):
            client = Anthropic(api_key=api_key)

            fix_instruction = (
                "\n\nAfter the review, also include a section '## Corrected Code' with a fixed "
                "version of the full snippet in a code block."
                if fix_mode else ""
            )

            prompt = f"""You are a senior software engineer performing a thorough code review.

Language: {language or "auto-detect"}

Code:
```
{code}
```

Review the code and organize findings into three markdown sections:
## 🔴 Critical (bugs, security issues, correctness problems)
## 🟡 Warnings (bad practices, potential edge cases)
## 🔵 Suggestions (style, readability, performance)

For each finding, briefly explain why it matters, not just what to change. If a section has no issues, say so.{fix_instruction}"""

            response = client.messages.create(
                model="claude-sonnet-5",
                max_tokens=2000,
                messages=[{"role": "user", "content": prompt}],
            )
            result = response.content[0].text

        st.markdown("---")
        st.markdown(result)
