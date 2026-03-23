# multi-agent-platform

A production-oriented multi-agent orchestration platform for LLM workflows built with LangGraph, FastAPI, and Jenkins CI/CD.

## Overview
This project demonstrates how to build and deploy a multi-agent system for LLM applications using graph-based orchestration, tool calling, and memory-aware workflows.

## Features
- Multi-agent orchestration with LangGraph
- Tool calling and workflow routing
- FastAPI-based backend service
- Dockerized deployment
- Jenkins CI/CD for automated testing and deployment

## Tech Stack
- Python
- LangGraph
- LangChain
- FastAPI
- Docker
- Jenkins

## Architecture
The system consists of multiple cooperating agents connected through a workflow graph. Each agent is responsible for a specific task such as planning, information retrieval, or execution.

## Project Structure
- `src/agents/` agent implementations
- `src/workflows/` orchestration graph
- `src/tools/` external tools and integrations
- `tests/` workflow tests

## Run Locally
```bash
git clone https://github.com/hossain-sanowar/multi-agent-platform
cd multi-agent-platform
pip install -r requirements.txt
uvicorn src.main:app --reload
```
# Docker
```bash
docker build -t multi-agent-platform .
docker run -p 8000:8000 multi-agent-platform
```
# CI/CD

Jenkins is used for automated testing and deployment workflows.

# Use Case

Built as a reference implementation for production-style agentic AI systems with modular orchestration and API deployment.

# Author

Md Sanowar Hossain
