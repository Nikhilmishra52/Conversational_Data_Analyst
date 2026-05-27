Data Analyst Agent
===================

Overview
--------
A Python scaffold for a LangGraph/LangChain-powered data analyst agent with role-specialized agents (analyst, engineer, synthesizer, orchestrator) and a FastAPI-ready backend.

Project Structure
-----------------
- `Backend/agents/`: role agents (analyst, engineer, synthesizer, orchestrator)
- `Backend/graphs/`: LangGraph definitions and compilers
- `Backend/states/`: shared state objects for graph execution
- `Backend/tools/`: tool implementations (data load/query/plot/etc.)
- `Backend/main.py`: backend entrypoint (FastAPI/CLI wiring placeholder)
- `Frontend/`: optional UI client placeholder
- `requirements.txt`: Python dependencies (langgraph, langchain, fastapi)

Getting Started
---------------
1) Create and activate a virtualenv:
   - Windows (PowerShell): `python -m venv .venv; .venv\\Scripts\\Activate.ps1`
   - macOS/Linux: `python -m venv .venv && source .venv/bin/activate`
2) Install dependencies: `pip install -r requirements.txt`
3) Copy env template: `cp .env.example .env` (or create) and set required keys (model/API configs).
4) Run backend (placeholder): `python Backend/main.py` (swap to `uvicorn Backend.main:app --reload` once FastAPI is added).

Environment
-----------
- `.env` holds secrets and is git-ignored; `.env.example` should list required variables with safe defaults.

