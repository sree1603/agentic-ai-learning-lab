# Natural Language SQL Assistant

A conversational SQL assistant that allows users to interact with a SQLite database using natural-language questions.

Built as a practical implementation while learning **LangChain, LLM integration, AI agents, and tool calling**.

## Overview

The application uses Google Gemini through LangChain to understand user questions, generate SQL queries, execute them against a SQLite database, and return the results in natural language.

Instead of manually writing SQL queries, users can ask questions such as:

- Who are all the students in the CSE department?
- Who scored the highest marks in Python?
- What is the average marks for each course?

## Architecture

```text
User Question
     |
     v
Gemini LLM + LangChain Agent
     |
     v
Custom SQL Tool
     |
     v
SQLite Database
     |
     v
Query Results
     |
     v
Natural Language Response
```

## Tech Stack

- Python
- LangChain
- Google Gemini
- SQLite
- python-dotenv

## Features Implemented

- SQLite database with students, courses, and enrollments tables.
- Python functions for database operations.
- Gemini integration using `ChatGoogleGenerativeAI`.
- Custom SQL execution tool using LangChain's `@tool`.
- Read-only database access.
- Agent creation using LangChain's `create_agent`.
- Natural-language question answering through tool calling.
- SQL JOIN and aggregate query support.

## Project Structure

```text
natural-language-sql-assistant/
│
├── data/
│   └── school.db
│
├── sql_assistant/
│   ├── __init__.py
│   ├── database.py
│   ├── model.py
│   ├── tools.py
│   └── agent.py
│
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

The SQLite database is generated locally and is not required to be committed.

## Setup and Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd agentic-ai-learning-lab/projects/natural-language-sql-assistant
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file using `.env.example` as a template.

```env
GOOGLE_API_KEY=your_google_api_key
```

Obtain a Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey).

### 5. Initialize the database

```bash
python -c "from sql_assistant.database import initialize_database; initialize_database()"
```

### 6. Run the application

```bash
python main.py
```

## Example Interaction

**User:**
```text
Who scored the highest marks in Python?
```

**Assistant:**
```text
Priya scored the highest marks in Python
with 96 marks in the 2026-Spring semester.
```

## Concepts Learned

- Connecting an LLM to a Python application.
- Using LangChain model integrations.
- Defining custom tools with the `@tool` decorator.
- Understanding tool calling.
- Creating agents using `create_agent`.
- Providing system instructions and database schema context.
- Executing SQL queries through an AI agent.

## Future Improvements

- Stronger SQL validation and query limits.
- Streaming agent responses.
- Better error handling.
- Conversation memory.
- Structured output.
- Human-in-the-loop approval for sensitive operations.
- Improved testing and deployment.

## Learning Status

This is an evolving learning project. New concepts and improvements will be added as I progress through Agentic AI courses and experiments.
