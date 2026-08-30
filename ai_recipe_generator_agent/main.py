import os
import base64
import streamlit as st
from anthropic import Anthropic

st.set_page_config(page_title="AI Recipe Generator Agent", page_icon="🍳")
st.title("🍳 AI Recipe Generator Agent")
st.caption("Powered by Claude — turn your ingredients into a recipe")

api_key = st.sidebar.text_input(
    "Anthropic API Key",
    type="password",
    value=os.environ.get("ANTHROPIC_API_KEY", ""),
)

diet = st.sidebar.selectbox(
    "Dietary preference",
    ["No restriction", "Vegetarian", "Vegan", "Gluten-free", "Keto", "Dairy-free"],
)
cuisine = st.sidebar.text_input("Cuisine style (optional)", placeholder="e.g. Italian, Thai, Mexican")

st.subheader("Ingredients")
image_file = st.file_uploader("Upload a photo of your ingredients (optional)", type=["png", "jpg", "jpeg"])
manual_ingredients = st.text_area("Or type your ingredients (comma-separated)")

if st.button("Generate Recipe", type="primary"):
    if not api_key:
        st.error("Please provide your Anthropic API key in the sidebar.")
    elif not image_file and not manual_ingredients.strip():
        st.error("Upload a photo or type in some ingredients first.")
    else:
        with st.spinner("Cooking up a recipe..."):
            client = Anthropic(api_key=api_key)

            content = []
            prompt_text = (
                f"Create a complete recipe using these ingredients (you may assume common "
                f"pantry staples like salt, oil, pepper are available). "
                f"Dietary preference: {diet}. "
                f"Cuisine style: {cuisine or 'any'}.\n\n"
                "Format the response in markdown with: Recipe Name, Prep/Cook Time, "
                "Ingredients (with quantities), and numbered Steps."
            )

            if image_file:
                img_bytes = image_file.read()
                b64_image = base64.b64encode(img_bytes).decode("utf-8")
                media_type = image_file.type or "image/jpeg"
                content.append({
                    "type": "image",
                    "source": {"type": "base64", "media_type": media_type, "data": b64_image},
                })
                content.append({"type": "text", "text": "Identify the ingredients visible in this photo, then " + prompt_text})
            else:
                content.append({"type": "text", "text": f"Ingredients: {manual_ingredients}\n\n{prompt_text}"})

            response = client.messages.create(
                model="claude-sonnet-5",
                max_tokens=1500,
                messages=[{"role": "user", "content": content}],
            )
            result = response.content[0].text

        st.markdown("---")
        st.markdown(result)
