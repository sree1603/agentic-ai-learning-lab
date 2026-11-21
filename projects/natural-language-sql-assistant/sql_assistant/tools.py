import sqlite3
from langchain.tools import tool
from sql_assistant.database import DATABASE_PATH

@tool
def execute_sql(query: str) -> str:
    """
    Execute a read-only SQL query on the school database.

    Use this tool to retrieve information about students,
    courses, enrollments, marks, and departments.

    Only SELECT queries are allowed.
    """
    connection = None

    try:
        connection = sqlite3.connect(
            f"file:{DATABASE_PATH}?mode=ro",
            uri=True
        )
       # Enforce read-only access for this connection
        connection.execute("PRAGMA query_only = ON")

        cursor = connection.execute(query)
        rows = cursor.fetchall()

        if not rows:
            return "No records found."

        columns = [description[0] for description in cursor.description]

        results = [
            dict(zip(columns, row))
            for row in rows
        ]

        return str(results)

    except sqlite3.Error as error:
        return f"SQL execution error: {error}"

    finally:
        if connection:
            connection.close()
