import sqlite3
from pathlib import Path
DATABASE_PATH = Path(__file__).resolve().parent.parent /"data"/"school.db"

def initialize_database():
    connection = sqlite3.connect(DATABASE_PATH)
    try:
        connection.execute("PRAGMA foreign_keys = ON")

        connection.executescript("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                department TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS courses (
                course_id INTEGER PRIMARY KEY,
                course_name TEXT NOT NULL UNIQUE,
                credits INTEGER NOT NULL
            );
            CREATE TABLE IF NOT EXISTS enrollments (
                enrollment_id INTEGER PRIMARY KEY,
                student_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                marks REAL NOT NULL,
                semester TEXT NOT NULL,

                FOREIGN KEY (student_id)
                    REFERENCES students(student_id),

                FOREIGN KEY (course_id)
                    REFERENCES courses(course_id),

                UNIQUE(student_id, course_id, semester)
            );
        """)
        connection.executemany(
            """
            INSERT OR IGNORE INTO students
            (student_id, name, age, department)
            VALUES (?, ?, ?, ?)
            """,
            [
                (1, "Rahul", 21, "CSE"),
                (2, "Priya", 20, "CSE"),
                (3, "Arjun", 22, "ECE"),
                (4, "Sneha", 21, "IT")
            ]
        )
        connection.executemany(
            """
            INSERT OR IGNORE INTO courses
            (course_id, course_name, credits)
            VALUES (?, ?, ?)
            """,
            [
                (1, "Python", 4),
                (2, "Machine Learning", 4),
                (3, "DBMS", 3)
            ]
        )
        connection.executemany(
            """
            INSERT OR IGNORE INTO enrollments
            (enrollment_id, student_id, course_id, marks, semester)
            VALUES (?, ?, ?, ?, ?)
            """,
            [
                (1, 1, 1, 92, "2026-Spring"),
                (2, 1, 2, 88, "2026-Spring"),
                (3, 2, 1, 96, "2026-Spring"),
                (4, 2, 3, 91, "2026-Spring"),
                (5, 3, 3, 85, "2026-Spring"),
                (6, 4, 2, 94, "2026-Spring")
            ]
        )
        connection.commit()

    finally:
        connection.close()

def get_all_students():
    connection = sqlite3.connect(DATABASE_PATH)

    try:
        cursor = connection.execute(
            "SELECT * FROM students"
        )

        students = cursor.fetchall()

        return students

    finally:
        connection.close()
def get_students_by_department(department):
    connection = sqlite3.connect(DATABASE_PATH)

    try:
        cursor = connection.execute(
            "SELECT * FROM students WHERE department = ?",
            (department,)
        )

        students = cursor.fetchall()

        return students

    finally:
        connection.close()
def get_all_courses():
    connection = sqlite3.connect(DATABASE_PATH)

    try:
        cursor = connection.execute(
            "SELECT * FROM courses"
        )

        courses = cursor.fetchall()
        return courses
    finally:
        connection.close()
def get_student_marks(student_name):
    connection = sqlite3.connect(DATABASE_PATH)

    try:
        cursor = connection.execute(
            """SELECT
            students.name,
            courses.course_name,
            enrollments.marks,
            enrollments.semester
        FROM enrollments
        JOIN students
            ON enrollments.student_id = students.student_id
        JOIN courses
            ON enrollments.course_id = courses.course_id
        WHERE students.name = ?""",(student_name,)
        )
        marks = cursor.fetchall()
        return marks
    finally:
        connection.close()