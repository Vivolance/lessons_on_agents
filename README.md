# AI Agents Kaggle

This project demonstrates a simple AI agent using Google ADK (Agent Development Kit) with the Gemini model and Google Search tool. The agent is designed to answer general questions and leverage Google Search for up-to-date information.

## Features
- Uses Google Gemini 2.5 LLM via Google ADK
- Integrates Google Search as a tool for current information
- Configurable retry logic for robust API calls
- Runs in-memory for fast prototyping


## Setup
1. **Clone the repository**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Or use Poetry if configured:
   ```bash
   poetry install
   ```
3. **Set up environment variables**:
   - Create a `.env` file with your Google API credentials as required by Google ADK.

## Usage
Run the agent from the command line:
```bash
python main.py
```
Or run the agent directly:
```bash
python agents/agent.py
```

## How It Works
- The agent is defined in `agents/agent.py` using the Gemini model and Google Search tool.
- The agent is run with an `InMemoryRunner` for step-by-step reasoning.
- Example query: "What are some important concepts to master in Finance?"

## Customization
- Modify the agent's instruction, model, or tools in `agents/agent.py`.
- Add more tools or change the model as needed.

## Requirements
- Python 3.11+
- Google ADK
- google-genai
- python-dotenv
- IPython (for display)