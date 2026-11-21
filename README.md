# Agentic AI Learning Lab

A hands-on learning repository documenting my journey into **Agentic AI**, LLMs, and intelligent AI applications.

I'm following structured courses from Anthropic, LangChain, Microsoft, and MongoDB, and building small practical projects to apply the concepts I learn.

Rather than just completing courses, my goal is to understand how AI agents work, experiment with different frameworks, and continuously improve my implementations.

## Learning Roadmap

| # | Course | Provider | Status |
|---|---|---|---|
| 01 | Building Effective Human Agent Teams | Anthropic | Completed |
| 02 | LangChain Essentials – Python | LangChain | Completed |
| 03 | Claude Platform 101 | Anthropic | Not started |
| 04 | Model Context Protocol: Advanced Topics | Anthropic | Not started |
| 05 | LangSmith Fleet – Build No-Code Agents | LangChain | Not started |
| 06 | Develop an Agent with Integrated Tools | Microsoft | Not started |
| 07 | AI Agents with MongoDB | MongoDB | Not started |

## Projects

### 01. Natural Language SQL Assistant

**Status:** In progress

A conversational SQL assistant that allows users to retrieve information from a SQLite database using natural-language questions.

**Technologies:** Python, LangChain, Google Gemini, SQLite

**Concepts explored:**
- LLM integration with LangChain
- Custom tools using the `@tool` decorator
- Tool calling
- Agent creation using `create_agent`
- ReAct-style agent workflows
- Natural-language to SQL interaction

**Current capabilities:**
- Answers questions about students, courses, marks, and departments.
- Generates SQL queries based on natural-language questions.
- Executes queries through a custom read-only SQL tool.
- Converts database results into natural-language responses.

[Explore the project](projects/natural-language-sql-assistant/)

## Technologies and Concepts

- Python
- LangChain
- Google Gemini
- Large Language Models (LLMs)
- AI Agents
- Tool Calling
- Multi-Agent Systems
- Model Context Protocol (MCP)
- Agent Memory
- Structured Output
- Human-in-the-Loop

This list will evolve as I explore and implement more concepts.

## Repository Structure

```text
agentic-ai-learning-lab/
│
├── projects/
│   ├── natural-language-sql-assistant/
│   └── future-projects/
│
├── learning-notes/
│
├── certificates/
│
├── README.md
└── .gitignore
```

Each project has its own README, source code, setup instructions, and dependencies wherever appropriate.

## My Approach

1. Complete a course and understand its core concepts.
2. Build a small project applying what I learned.
3. Document the implementation and important learnings.
4. Improve earlier projects as I gain new knowledge.
5. Track progress through commits and course completion certificates.

This repository is a continuous work in progress. I'm using it to learn by building, experimenting, debugging, and improving.

