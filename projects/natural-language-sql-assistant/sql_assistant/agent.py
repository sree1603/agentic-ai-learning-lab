
from langchain.agents import create_agent

from sql_assistant.model import model
from sql_assistant.tools import execute_sql


SYSTEM_PROMPT = """
You are a helpful Natural Language SQL Assistant.

You answer questions about students, courses, enrollments,
marks, and departments using the school SQLite database.

Database schema:

1. students
   - student_id
   - name
   - age
   - department

2. courses
   - course_id
   - course_name
   - credits

3. enrollments
   - enrollment_id
   - student_id
   - course_id
   - marks
   - semester

Rules:
- Use the execute_sql tool whenever a question requires database information.
- Generate valid SQLite SQL queries.
- Use JOINs when information is spread across multiple tables.
- Never invent database results.
- Only retrieve information. Never attempt to modify the database.
- Explain query results clearly in simple English.
"""


agent = create_agent(
    model=model,
    tools=[execute_sql],
    system_prompt=SYSTEM_PROMPT
)


def ask_database(question: str):
    response = agent.invoke(
        {
            "messages": [
                {"role": "user", "content": question}
            ]
        }
    )

    return response["messages"][-1].text
