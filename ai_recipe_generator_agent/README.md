## 🥕 ➡️ 🍳 Recipe Generator Agent

This is a Streamlit-based application that turns your ingredients into a full recipe. The app uses Anthropic's Claude model, including its vision capability, to read a photo of your ingredients or a typed list and generate a complete recipe with quantities, steps, and cook time.



Created and developed by **[Chintan Parmar](https://github.com/iamchintanparmar)**.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![AI Agents](https://img.shields.io/badge/AI-Agents-8b6bff)
![License](https://img.shields.io/badge/License-MIT-green)

## Features

- **Ingredient Recognition**: Reads ingredients directly from an uploaded photo using Claude's vision.
- **Manual Input**: Accepts a typed, comma-separated ingredient list as an alternative to a photo.
- **Dietary Filters**: Supports vegetarian, vegan, gluten-free, keto, and dairy-free preferences.
- **Cuisine Styling**: Optionally targets a specific cuisine (Italian, Thai, Mexican, etc.).
- **API Key Integration**: Requires an Anthropic API key, entered securely via the sidebar.

## How It Works

1. You upload a photo of your ingredients or type them in manually.
2. If a photo is provided, Claude identifies the ingredients visible in it.
3. The ingredient list, dietary preference, and cuisine style are combined into a prompt.
4. Claude generates a structured recipe, which is rendered in the app.

## Setup

### Requirements

1. **API Key**:
   - **Anthropic API Key**: Sign up at [console.anthropic.com](https://console.anthropic.com/) to obtain your API key.
2. **Python 3.8+**: Ensure you have Python 3.8 or higher installed.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/iamchintanparmar/beginner_ai_agents/ai_recipe_generator_agents.git
   cd ai_recipe_generator_agent
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
   - Set a dietary preference and cuisine style (optional).
   - Upload a photo of your ingredients, or type them in manually.
   - Click "Generate Recipe".

## Usage Notes

- Only one of photo or manual input is used per generation — photo takes priority if both are provided.
- Common pantry staples (salt, oil, pepper) are assumed to be available.
- Nothing is stored — re-upload or re-type ingredients each session.

## Troubleshooting

| Issue | Possible Cause | Fix |
|---|---|---|
| Ingredients misread from photo | Blurry or cluttered image | Use a clearer, well-lit photo or switch to manual input |
| Generation fails | Invalid or missing Anthropic API key | Re-check the key entered in the sidebar |
| Recipe ignores dietary preference | Preference not clearly conflicting with ingredients | Try a more specific preference or regenerate |
| App won't start | Missing dependencies | Re-run `pip install -r requirements.txt` |

## Tech Stack

- **Frontend**: Streamlit
- **Vision + Generation**: Anthropic Claude

## Author

**Chintan Parmar** — Full-Stack Developer & Creative Technologist

- GitHub: [@iamchintanparmar](https://github.com/iamchintanparmar)
- Portfolio: [iamchintanparmar.github.io](https://iamchintanparmar.github.io)

## License

MIT
