# Weather Agent Project

A modular weather question-answering system using LangChain, Ollama, FastAPI, and Streamlit. It answers weather questions by querying APIs via an MCP proxy server. The project is split into three main parts: backend API (MCP server), intelligent agent, and Streamlit web interface.

## Table of Contents
- Overview
- Project Structure
- Installation
- Usage
- API Endpoints
- Agent
- User Interface
- Dependencies

---

## Overview
This project provides a weather question-answering system powered by a local LLM (Ollama) and LangChain. It fetches weather data via external APIs, processes user queries, and displays results in a web interface.

---

## Project Structure
```
group-ib-test-task/
│
├── agent/
│   ├── agent.py           # Main agent logic (LangChain, tools)
│   ├── model_loader.py    # Loads LLM models (Ollama)
│   ├── tools.py           # Custom tools for the agent
│   └── __pycache__/
│
├── mcp_server/
│   ├── main.py            # FastAPI server with endpoints
│   ├── requirements.txt   # Server dependencies
│   ├── weather_api.py     # Weather API integration
│   └── __pycache__/
│
├── ui/
│   └── app.py             # Streamlit interface
│
├── requirements.txt       # Global dependencies (Streamlit, LangChain)
├── README.md              # Documentation
```

---

## Installation

1. **Clone the repository:**
   ```powershell
   git clone <repo_url>
   cd group-ib-test-task
   ```

2. **Install Python dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Install MCP server dependencies:**
   ```powershell
   cd mcp_server
   pip install -r requirements.txt
   cd ..
   ```

4. **Install and run Ollama:**
   - Download Ollama from [ollama.com](https://ollama.com/).
   - Install an open-source model (e.g., `ollama pull mistral`).
   - Start the Ollama server locally.
   - To change the model, use `ollama pull <model_name>` and update `model_loader.py`.

5. **Configure environment variables:**
   - By default, MCP server runs at `http://localhost:8000`. If you change it, set `MCP_SERVER_URL` in your environment.

---

## Usage

### 1. Start the MCP server
```powershell
cd mcp_server
uvicorn main:app --reload
```

### 2. Launch the Streamlit interface
Run the following command from the project root:
```powershell
streamlit run ui/app.py
```
Access the web interface at `http://localhost:8501`.

### 3. Interact with the agent
- Enter a weather question in the UI.
- The agent uses LangChain and Ollama to process the query and fetch data via the MCP server.

---

## API Endpoints
The MCP server provides:
- `GET /coordinates?city=<city_name>`  
    Returns latitude and longitude for a given city.
- `GET /weather?lat=<latitude>&lon=<longitude>`  
    Returns weather data for the specified coordinates.

---

## Agent
- **LangChain**: Orchestrates LLM reasoning and tools.
- **Ollama**: Local backend for running open-source LLMs for natural language processing.
- **Custom tools**: Integration with MCP endpoints to fetch weather and coordinates.
- **Open-source models**: Ability to use different open-source models available on Ollama (`mistral`, `llama2`, etc.).

---

## User Interface
- **Streamlit**: Interactive web interface.
- **Features**:
    - Input box for weather questions
    - Display of agent responses
    - Error handling and status messages

---

## Dependencies
- Python 3.10+
- [LangChain](https://python.langchain.com/)
- [Ollama](https://ollama.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)
- [httpx](https://www.python-httpx.org/)
- [uvicorn](https://www.uvicorn.org/)
- Other dependencies in `requirements.txt` and `mcp_server/requirements.txt`


