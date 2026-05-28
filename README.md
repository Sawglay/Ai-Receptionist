# AI Receptionist 

An enterprise-grade, autonomous AI Receptionist designed to handle customer inquiries, manage appointment bookings, and integrate seamlessly with company CRMs. Built with FastAPI, LangGraph, and OpenAI.

[![CI/CD Pipeline](https://github.com/yourusername/ai-receptionist/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/yourusername/ai-receptionist/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features
- **Stateful Conversational AI:** Handles complex, multi-turn dialogues without losing context.
- **Autonomous Tool Execution:** Automatically schedules appointments via Google Calendar API using LLM Function Calling.
- **RAG Integration:** Answers specific business FAQs by querying a vector database knowledge base.
- **Production Ready:** Built-in asynchronous logging, structured error handling, and fully containerized with Docker.


## Quick Start

### Prerequisites
- Python 3.10+
- Docker (Optional)
- OpenAI API Key

### Installation

1. **Clone the repository:**
   ```bash
   git clone


2. **Set up Environment Variables:**
   ```bash
   Bash
   cp .env.example .env
   # Open .env and add your OPENAI_API_KEY and other configuration data

4. **Run via Docker (Recommended):**

   ```bash
   Bash
   docker build -t ai-receptionist .
   docker run -p 8000:8000 --env-file .env ai-receptionist

**Running Tests**

   
Bash
pytest tests/





5. **API Documentation**
Once running, navigate to http://localhost:8000/docs to view the interactive Swagger API documentation.

---

## 6. Pro-Tips for Git Hygiene

1. **Commit Messages:** Use Conventional Commits (e.g., `feat: add google calendar tool integration`, `fix: handle openai rate limit exception`, `docs: update readme architecture diagram`).
2. **Branches:** Don't push everything straight to `main`. Create feature branches (`feature/voice-pipeline`, `feature/llm-agent`) and merge them via Pull Requests. It shows you know how to work in a development team.

Are you planning to make this primarily a **voice-based** receptionist (over the phone/WebSockets)
