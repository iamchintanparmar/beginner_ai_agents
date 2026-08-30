import os
import streamlit as st
from anthropic import Anthropic

st.set_page_config(page_title="AI Language Tutor Agent", page_icon="🗣️")
st.title("🗣️ AI Language Tutor Agent")
st.caption("Powered by Claude — practice conversation in any language")

api_key = st.sidebar.text_input(
    "Anthropic API Key",
    type="password",
    value=os.environ.get("ANTHROPIC_API_KEY", ""),
)

language = st.sidebar.text_input("Language to practice", value="Spanish")
level = st.sidebar.selectbox("Your level", ["Beginner", "Intermediate", "Advanced"])
scenario = st.sidebar.text_input("Conversation scenario", value="Ordering food at a restaurant")

if "language_tutor_messages" not in st.session_state:
    st.session_state.language_tutor_messages = []

if st.sidebar.button("Start New Conversation"):
    st.session_state.language_tutor_messages = []

for msg in st.session_state.language_tutor_messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input(f"Reply in {language}...")

if user_input:
    if not api_key:
        st.error("Please provide your Anthropic API key in the sidebar.")
    else:
        st.session_state.language_tutor_messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        client = Anthropic(api_key=api_key)

        system_prompt = f"""You are a friendly {language} conversation tutor for a {level} learner.
Scenario: {scenario}

Stay in character for the roleplay and reply mostly in {language}, keeping sentences appropriate for a {level} learner.
After your in-character reply, add a short '---' separated section in English with:
- Corrections: point out any mistakes in the learner's last message
- New vocabulary: 2-3 useful words/phrases from this exchange"""

        with st.chat_message("assistant"):
            with st.spinner("..."):
                response = client.messages.create(
                    model="claude-sonnet-5",
                    max_tokens=800,
                    system=system_prompt,
                    messages=st.session_state.language_tutor_messages,
                )
                reply = response.content[0].text
                st.markdown(reply)

        st.session_state.language_tutor_messages.append({"role": "assistant", "content": reply})
