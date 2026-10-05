import json
import os

FILE_NAME = "students.json"


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def load_students():
    if not os.path.exists(FILE_NAME):
        save_students([])          # create an empty file on first run
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read students.json. Starting with an empty list.")
        return []


def get_number(prompt, low, high):
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
            print(f"Please enter a number between {low} and {high}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def find_student(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def print_student(student):
    print(f"ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | "
          f"Course: {student['course']} | Semester: {student['semester']} | "
          f"Marks: {student['marks']} | Grade: {calculate_grade(student['marks'])}")


def add_student(students):
    student_id = get_number("Student ID: ", 1, 999999)
    if find_student(students, student_id):
        print("Error: Student ID already exists.")
        return
    student = {
        "id": student_id,
        "name": get_text("Name: "),
        "age": get_number("Age (15-60): ", 15, 60),
        "course": get_text("Course: "),
        "semester": get_number("Semester (1-8): ", 1, 8),
        "marks": get_number("Marks (0-100): ", 0, 100),
    }
    students.append(student)
    save_students(students)
    print("Student added successfully.")


def view_students(students):
    if not students:
        print("No students found.")
        return
    for student in students:
        print_student(student)


def search_student(students):
    keyword = input("Enter Student ID or name to search: ").strip().lower()
    found = False
    for student in students:
        if keyword == str(student["id"]) or keyword in student["name"].lower():
            print_student(student)
            found = True
    if not found:
        print("No matching student found.")


def update_student(students):
    student = find_student(students, get_number("Student ID to update: ", 1, 999999))
    if student is None:
        print("Student not found.")
        return
    print("Enter the new details:")
    student["name"] = get_text("Name: ")
    student["age"] = get_number("Age (15-60): ", 15, 60)
    student["course"] = get_text("Course: ")
    student["semester"] = get_number("Semester (1-8): ", 1, 8)
    student["marks"] = get_number("Marks (0-100): ", 0, 100)
    save_students(students)
    print("Student updated successfully.")


def delete_student(students):
    student = find_student(students, get_number("Student ID to delete: ", 1, 999999))
    if student is None:
        print("Student not found.")
        return
    students.remove(student)
    save_students(students)
    print("Student deleted successfully.")


def show_grade(students):
    student = find_student(students, get_number("Student ID: ", 1, 999999))
    if student is None:
        print("Student not found.")
        return
    print(f"{student['name']} scored {student['marks']} -> Grade {calculate_grade(student['marks'])}")


def main():
    students = load_students()
    while True:
        print("\n====================================")
        print("      STUDENT MANAGEMENT SYSTEM")
        print("====================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Calculate Grade")
        print("7. Exit")
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            show_grade(students)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


main()
