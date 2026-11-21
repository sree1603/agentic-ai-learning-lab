# from sql_assistant.database import initialize_database

# def main():
#     # print("Welcome to Natural Language SQL Assistant!")
#     initialize_database()
#     print("Database initialized successfully")

# if __name__ == "__main__":
#     main()

# from sql_assistant.database import (
#     get_all_students,
#     get_students_by_department,
#     get_all_courses,
#     get_student_marks
# )


# def main():
#     print("\n--- All Students ---")
#     print(get_all_students())

#     print("\n--- CSE Students ---")
#     print(get_students_by_department("CSE"))

#     print("\n--- All Courses ---")
#     print(get_all_courses())

#     print("\n--- Rahul's Marks ---")
#     print(get_student_marks("Rahul"))


# if __name__ == "__main__":
#     main()

# from sql_assistant.model import get_model_response


# def main():
#     question = "Explain what a relational database is in 3 simple sentences."

#     response = get_model_response(question)

#     print("\n--- Gemini Response ---")
#     print(response)


# if __name__ == "__main__":
#     main()




from sql_assistant.agent import ask_database


def main():
    print("Natural Language SQL Assistant")
    print("Type 'exit' to quit.")

    while True:
        question = input("\nYou: ")

        if question.lower() == "exit":
            print("Goodbye!")
            break

        response = ask_database(question)

        print("\nAssistant:", response)


if __name__ == "__main__":
    main()
