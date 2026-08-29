import os
import streamlit as st
from anthropic import Anthropic

st.set_page_config(page_title= "Chintan",page_icon="🧑‍💻")
st.title("🧑‍💻 AI Code Review Agent")
st.caption("Powered by Claude — automated PR-style code review")


api_key = st.sidebar.text_input(
    "Anthropic Api key",
    type = "password",
    value=os.environ.get("ANTHROPIC_API_KEY", ""),
)

