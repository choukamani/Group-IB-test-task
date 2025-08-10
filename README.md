

# Weather Agent Project

An intelligent weather agent based on a local LLM using LangChain and Ollama. It answers weather questions by querying APIs via an MCP proxy server. The project is modular: backend API, intelligent agent, and Streamlit web interface.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Agent](#agent)
- [User Interface](#user-interface)
- [Configuration](#configuration)
- [Dependencies](#dependencies)

---

## Overview

This project provides a weather question-answering system powered by a local LLM (Ollama) and LangChain. It fetches weather data via external APIs, processes user queries, and displays results in a web interface.

We use an open-source model on Ollama (e.g., `llama2`, `mistral`, etc.), but you can use any other open-source model compatible with Ollama. Just download and activate it via Ollama.

---

## Project Structure

```
weather_agent_project/
│
├── agent/
│   ├── agent.py           # Main agent logic (LangChain, tools)
│   ├── model_loader.py    # Loads LLM models (Ollama)
│   ├── tools.py           # Custom tools for the agent
│
├── mcp_server/
│   ├── main.py            # FastAPI server with endpoints
│   ├── requirements.txt   # Server dependencies
│   └── weather_api.py     # Weather API integration
│
├── ui/
│   └── app.py             # Streamlit interface
│
├── requirements.txt       # Global dependencies
├── README.md              # Documentation
└── .env                   # Configuration
```

---

## Installation

1. **Clone the repository:**
	```bash
	git clone <repo_url>
	cd weather_agent_project
	```

2. **Install Python dependencies:**
	```bash
	pip install -r requirements.txt
	```

3. **Install MCP server dependencies:**
	```bash
	cd mcp_server
	pip install -r requirements.txt
	cd ..
	```

4. **Install and run Ollama:**
	- Download Ollama from [ollama.com](https://ollama.com/).
	- Install an open-source model (e.g., `ollama pull llama2`).
	- Start the Ollama server locally.
	- To change the model, use `ollama pull <model_name>` and select it in the config.

5. **Configure environment variables:**
	- Create a `.env` file at the project root.
	- Add API keys and configuration (see below).

---

## Usage

### 1. Start the MCP server

```bash
cd mcp_server
uvicorn main:app --reload
```

The server exposes endpoints for coordinates and weather data.

### 2. Launch the Streamlit interface

Run the following command from the project root:

```bash
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
- **Open-source models**: Ability to use different open-source models available on Ollama (`llama2`, `mistral`, `gemma`, etc.).

---

## User Interface

- **Streamlit**: Interactive web interface.
- **Features**:
	- Input box for questions
	- Display of agent responses
	- Error handling and status messages

---

## Dependencies

- Python 3.10+
- [LangChain](https://python.langchain.com/)
- [Ollama](https://ollama.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)
- Other dependencies in `requirements.txt` and `mcp_server/requirements.txt`

---


