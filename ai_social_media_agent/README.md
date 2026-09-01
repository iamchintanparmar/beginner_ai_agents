## 📝 ➡️ 📱 Social Media Agent

This is a Streamlit-based application that repurposes any piece of content into platform-ready social media posts. The app uses Anthropic's Claude model to rewrite your source content for X/Twitter, LinkedIn, Instagram, Facebook, or TikTok, respecting each platform's length and style conventions.

## Features

- **Multi-Platform Output**: Generates posts for X/Twitter, LinkedIn, Instagram, Facebook, and TikTok in one pass.
- **Tone Control**: Choose Professional, Casual, Witty, Inspirational, or Bold.
- **Hashtag Toggle**: Optionally include relevant hashtags per post.
- **Platform-Aware Formatting**: Respects each platform's typical length and style.
- **API Key Integration**: Requires an Anthropic API key, entered securely via the sidebar.

## How It Works

1. You paste in source content — an article, idea, or draft.
2. You select target platforms, tone, and whether to include hashtags.
3. All inputs are combined into a prompt sent to Claude.
4. Claude returns one tailored post per selected platform, rendered in the app.

## Setup

### Requirements

1. **API Key**:
   - **Anthropic API Key**: Sign up at [console.anthropic.com](https://console.anthropic.com/) to obtain your API key.
2. **Python 3.8+**: Ensure you have Python 3.8 or higher installed.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/coboat/Chintan-s-ai-Agents.git
   cd Chintan-s-ai-Agents/beginner_ai_agents/ai_social_media_agent
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
   - Select platforms, tone, and hashtag preference.
   - Paste the content you want to repurpose.
   - Click "Generate Posts".

## Usage Notes

- At least one platform must be selected before generating.
- Longer source content generally produces richer posts.
- Nothing is stored — re-paste the content each session.

## Troubleshooting

| Issue | Possible Cause | Fix |
|---|---|---|
| Generation fails | Invalid or missing Anthropic API key | Re-check the key entered in the sidebar |
| No posts generated | No platform selected | Select at least one platform in the sidebar |
| Posts too long/short | Platform convention mismatch | Regenerate — occasionally re-run for a tighter fit |
| App won't start | Missing dependencies | Re-run `pip install -r requirements.txt` |

## Tech Stack

- **Frontend**: Streamlit
- **Generation**: Anthropic Claude
