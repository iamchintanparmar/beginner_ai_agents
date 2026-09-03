# 📊 AI Data Analysis Agent

An AI data analysis agent built using the Agno agent framework and OpenAI's GPT-4o model. This agent helps users analyze their data — CSV and Excel files — through natural language queries, powered by OpenAI's language models and DuckDB for efficient data processing, making data analysis accessible to users regardless of their SQL expertise.


Created and developed by **[Chintan Parmar](https://github.com/iamchintanparmar)**.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![AI Agents](https://img.shields.io/badge/AI-Agents-8b6bff)
![License](https://img.shields.io/badge/License-MIT-green)

## Features

- 📤 **File Upload Support**:
  - Upload CSV and Excel files
  - Automatic data type detection and schema inference
  - Support for multiple file formats

- 💬 **Natural Language Queries**:
  - Convert natural language questions into SQL queries
  - Get instant answers about your data
  - No SQL knowledge required

- 🔍 **Advanced Analysis**:
  - Perform complex data aggregations
  - Filter and sort data
  - Generate statistical summaries
  - Create data visualizations

- 🎯 **Interactive UI**:
  - User-friendly Streamlit interface
  - Real-time query processing
  - Clear result presentation

## How to Run

1. **Setup Environment**
   ```bash
   # Clone the repository
   git clone https://github.com/iamchintanparmar/beginner_ai_agents.git
   cd begineer_ai_agents/data_analysis_agent

   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Configure API Keys**
   - Get an OpenAI API key from the [OpenAI Platform](https://platform.openai.com)

3. **Run the Application**
   ```bash
   streamlit run data_analyst.py
   ```

## Usage

1. Launch the application using the command above.
2. Provide your OpenAI API key in the sidebar of the Streamlit app.
3. Upload your CSV or Excel file through the Streamlit interface.
4. Ask questions about your data in natural language.
5. View the results and generated visualizations.

## Troubleshooting

| Issue | Possible Cause | Fix |
|---|---|---|
| App won't start | Missing dependencies | Re-run `pip install -r requirements.txt` |
| Query fails / no results | Invalid or missing OpenAI API key | Re-check the key entered in the sidebar |
| File won't upload | Unsupported format or corrupted file | Confirm the file is a valid `.csv` or `.xlsx` |

## Tech Stack

- **Frontend**: Streamlit
- **Agent Framework**: Agno
- **AI Model**: OpenAI GPT-4o
- **Data Processing**: DuckDB

## Author

**Chintan Parmar** — Full-Stack Developer & Creative Technologist

- GitHub: [@iamchintanparmar](https://github.com/iamchintanparmar)
- Portfolio: [iamchintanparmar.github.io](https://iamchintanparmar.github.io)

## License

MIT

