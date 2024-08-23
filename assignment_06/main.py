from typing import List
from typing import Tuple


def manage_student_database():
    student_list: List[Tuple[int, str]] = []
    # id: list[int] = list(range(1, len(student_list) + 1))

    while True:
        student_name: str = input(
            """Please enter the student's name (or type "stop" to finish): """
        )

        if student_name == "stop":
            break

        if student_name in student_list:
            print("The name is already in the list")
        else:
            student_list.append(student_name)

    student_names_with_ids: Tuple[int, str] = list(enumerate(student_list, start=1))
    print(f"\nComplete list of students:\n{student_names_with_ids}\n")

    print("List of students with IDs:")
    for student in student_names_with_ids:
        print(f"ID: {student[0]}, Name: {student[1]}")

    total_students: int = len(student_list)
    print(f"\nTotal number of students: {total_students}")

    student_names_length: int = len("".join(student_list))
    print(f"Total length of all student names combined: {student_names_length}")

    longest_name: str = max(student_list, key=len)
    print(f"The student with the longest name is: {longest_name}")

    shortest_name: str = min(student_list, key=len)
    print(f"The student with the shortest name is: {shortest_name}")


manage_student_database()

# Todo
# Dont' append if the user enters without typing anything
# It should exclude spaces between names also
