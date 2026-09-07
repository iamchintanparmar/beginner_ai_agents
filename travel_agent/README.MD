## 🛫 AI Travel Agent

This Streamlit app is an AI-powered travel agent that generates personalized travel itineraries using OpenAI GPT-4o. It automates the process of researching, planning, and organizing your dream vacation, allowing you to explore exciting destinations with ease.

## Features

- Research and discover exciting travel destinations, activities, and accommodations.
- Customize your itinerary based on the number of days you want to travel.
- Utilize the power of GPT-4o to generate intelligent and personalized travel plans.
- Download your itinerary as a calendar (.ics) file to import into Google Calendar, Apple Calendar, or other calendar apps.

## How to Get Started

1. Clone the repository:
   ```bash
   git clone https://github.com/coboat/Chintan-s-ai-Agents.git
   cd Chintan-s-ai-Agents/beginner_ai_agents/travel_agent
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Get your OpenAI API key:
   - Sign up for an [OpenAI account](https://platform.openai.com/) (or the LLM provider of your choice) and obtain your API key.

4. Get your SerpAPI key:
   - Sign up for a [SerpAPI account](https://serpapi.com/) and obtain your API key.

5. Run the Streamlit app:
   ```bash
   streamlit run travel_agent.py
   ```

   For local LLM usage (with Ollama):
   ```bash
   streamlit run local_travel_agent.py
   ```

## How It Works

The AI Travel Agent has two main components:

- **Researcher**: Generates search terms based on the user's destination and travel duration, and searches the web for relevant activities and accommodations using SerpAPI.
- **Planner**: Takes the research results and user preferences to generate a personalized draft itinerary that includes suggested activities, dining options, and accommodations.

## Using the Calendar Download Feature

After generating your travel itinerary:

1. Click the "Download Itinerary as Calendar (.ics)" button that appears next to the "Generate Itinerary" button.
2. Save the .ics file to your computer.
3. Import the file into your preferred calendar application (Google Calendar, Apple Calendar, Outlook, etc.).
4. Each day of your itinerary will appear as an all-day event in your calendar.
5. The complete details for each day's activities are included in the event description.

This feature makes it easy to keep track of your travel plans and have your itinerary available on all your devices, even offline.

## Local vs Cloud Version

- **travel_agent.py**: Uses OpenAI's GPT-4o for high-quality itineraries (requires OpenAI API key).
- **local_travel_agent.py**: Uses Ollama for local LLM inference without sending data to external APIs (requires Ollama to be installed and running).

## Troubleshooting

| Issue | Possible Cause | Fix |
|---|---|---|
| App won't start | Missing dependencies | Re-run `pip install -r requirements.txt` |
| No itinerary generated | Invalid or missing OpenAI API key | Re-check the key entered in the sidebar/environment |
| No search results | Invalid or missing SerpAPI key | Re-check the key entered in the sidebar/environment |
| Local version fails | Ollama not installed or not running | Install Ollama and confirm it's running before launching the app |

## Tech Stack

- **Frontend**: Streamlit
- **AI Model**: OpenAI GPT-4o (or Ollama for local inference)
- **Web Search**: SerpAPI