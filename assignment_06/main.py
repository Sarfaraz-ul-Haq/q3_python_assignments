from typing import List
from typing import Tuple


# main function
def manage_student_database():

    # student names will be appended one by one in this empty list
    student_list: List[str] = []

    while True:
        student_name: str = input(
            """Please enter the student's name (or type "stop" to finish): """
        )

        # while loop will break when the user enters "stop"
        if student_name.lower() == "stop":
            break

        # if user enters empty string then the rest of the code will not work and loop will start again
        if student_name.strip() == "":
            print("Empty name entered")
            continue

        # condition to check duplicate name
        if student_name in student_list:
            print("The name is already in the list")
        else:
            student_list.append(student_name)

    # copy of student_list without spaces
    student_list_without_spaces: List[str] = list(
        map(lambda student: student.replace(" ", ""), student_list)
    )

    student_names_with_ids: Tuple[int, str] = list(enumerate(student_list, start=1))
    print(f"\nComplete list of students:\n{student_names_with_ids}\n")
    # ____________________________________________________________

    print("List of students with IDs:")
    for student in student_names_with_ids:
        print(f"ID: {student[0]}, Name: {student[1]}")
    # ____________________________________________________________

    total_students: int = len(student_list)
    print(f"\nTotal number of students: {total_students}")
    # ____________________________________________________________

    student_names_length: int = len("".join(student_list_without_spaces))
    print(f"Total length of all student names combined: {student_names_length}")
    # ____________________________________________________________

    longest_name: str = max(student_list_without_spaces, key=len)
    print(f"The student with the longest name is: {longest_name}")

    shortest_name: str = min(student_list_without_spaces, key=len)
    print(f"The student with the shortest name is: {shortest_name}")


manage_student_database()
