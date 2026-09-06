## 🎵 ModelsLab Music Generator

This is a Streamlit-based application that allows users to generate music using the ModelsLab API and OpenAI's GPT-4 model. Users can input a prompt describing the type of music they want to generate, and the application will generate a music track in MP3 format based on the given prompt.

## Features

- **Generate Music**: Enter a detailed prompt for music generation (genre, instruments, mood, etc.), and the app will generate a music track.
- **MP3 Output**: The generated music will be in MP3 format, available for listening or download.
- **User-Friendly Interface**: Simple and clean Streamlit UI for ease of use.
- **API Key Integration**: Requires both OpenAI and ModelsLab API keys to function. API keys are entered in the sidebar for authentication.

## Setup

### Requirements

1. **API Keys**:
   - **OpenAI API Key**: Sign up at [OpenAI](https://platform.openai.com/api-keys) to obtain your API key.
   - **ModelsLab API Key**: Sign up at [ModelsLab](https://modelslab.com/dashboard/api-keys) to get your API key.

2. **Python 3.8+**: Ensure you have Python 3.8 or higher installed.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/coboat/Chintan-s-ai-Agents.git
   cd Chintan-s-ai-Agents/beginner_ai_agents/music_generator_agent
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

1. Start the Streamlit app:
   ```bash
   streamlit run music_generator_agent.py
   ```

2. In the app interface:
   - Enter a music generation prompt.
   - Click "Generate Music".
   - Play the music & download it.

## Usage Notes

- Be as descriptive as possible in your prompt (genre, instruments, mood, tempo) for better results.
- Generated audio files are not stored permanently — download them if you want to keep a copy.

## Troubleshooting

| Issue | Possible Cause | Fix |
|---|---|---|
| App won't start | Missing dependencies | Re-run `pip install -r requirements.txt` |
| No music generated | Invalid or missing ModelsLab API key | Re-check the key entered in the sidebar |
| Prompt processing fails | Invalid or missing OpenAI API key | Re-check the key entered in the sidebar |

## Tech Stack

- **Frontend**: Streamlit
- **Music Generation**: ModelsLab API
- **Prompt Processing**: OpenAI GPT-4