# Student Management System

A simple console-based Student Management System written in Python.
It stores student records in a JSON file so the data is saved between runs.

## Features
- Add, view, search, update and delete students
- Unique Student IDs
- Input validation (age, semester, marks, empty fields)
- Automatic grade calculation from marks
- Data saved in `students.json`

## Technologies Used
- Python 3 (core language only)
- JSON for file storage

## How to Run
1. Install Python 3 from python.org
2. Download or clone this repository
3. Open a terminal in the project folder and run:

```
python student_management.py
```

## Example Menu
```
====================================
      STUDENT MANAGEMENT SYSTEM
====================================
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Calculate Grade
7. Exit
```

## Grading Scale
| Marks    | Grade |
|----------|-------|
| 90-100   | A+    |
| 80-89    | A     |
| 70-79    | B     |
| 60-69    | C     |
| 50-59    | D     |
| Below 50 | F     |

## Project Structure
```
student-management-system/
├── student_management.py
├── README.md
└── .gitignore
```
`students.json` is created automatically when the program runs.

## Future Improvements
- Sort students by marks or name
- Store marks for multiple subjects
- Export records to a CSV file
- Add a simple GUI
