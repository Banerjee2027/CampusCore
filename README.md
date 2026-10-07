# CampusCore - Student Management System

Keep track of students, their marks and their grades, either from the terminal or from the browser.

I made this for a college practical. The first version was a plain Python program that runs in the console. Later I built a web version with the same features, so the same idea exists in two forms: one to show how the logic works, one to show how it could look as an actual app.

**Live demo:** https://YOUR-USERNAME.github.io/student-management-system/

<!--
Add screenshots here once you have them, for example:

![Login page](screenshots/login.png)
![Students table](screenshots/students.png)
![Kanban board](screenshots/kanban.png)
-->

---

## What it can do

| Feature | Console | Web |
|---|:---:|:---:|
| Add a student | yes | yes |
| View all students | yes | yes |
| Search by ID or name | yes | yes |
| Update a student | yes | yes |
| Delete a student | yes | yes |
| Calculate a grade from marks | yes | yes |
| Sign up and log in | - | yes |
| Kanban board grouped by grade | - | yes |
| Dark mode | - | yes |

Each student has an ID, name, age, course, semester and marks. IDs are unique.

---

## Running it

### Console version (Python)

You only need Python 3. No packages to install.

```bash
python student_management.py
```

On Windows, if `python` is not recognised, try `py student_management.py`.

You will see a menu like this:

```text
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

Records are saved to `students.json`, which the program creates on its own the first time you run it.

### Web version

Download the project and open `index.html` in any browser. That is all, there is nothing to build or install.

It can also be hosted on GitHub Pages: go to **Settings > Pages**, choose the `main` branch, and save.

To try it quickly, sign up with any username and password, or use the demo account:

```text
username: admin
password: admin123
```

Once inside, the empty Students page has a **Load sample data** button if you want something to look at.

---

## Grading

Both versions use the same rule.

| Marks | Grade |
|---|---|
| 90 to 100 | A+ |
| 80 to 89 | A |
| 70 to 79 | B |
| 60 to 69 | C |
| 50 to 59 | D |
| Below 50 | F |

---

## Input rules

| Field | Rule |
|---|---|
| Student ID | whole number from 1 to 999999, must not already exist |
| Name, Course | cannot be empty |
| Age | 15 to 60 |
| Semester | 1 to 8 |
| Marks | 0 to 100 |

The console version keeps asking until the input is valid, so wrong input does not crash it.

---

## How the data is stored

- **Console:** a JSON file, `students.json`, in the same folder as the script. It is loaded when the program starts and saved after every add, update or delete.
- **Web:** the browser's `localStorage`. The data stays on the device you used.
- **Web accounts:** also in `localStorage`. Passwords are saved as salted SHA-256 hashes instead of plain text.

The two versions do not share data with each other.

---

## Project structure

```text
student-management-system/
├── student_management.py    console program
├── index.html               web version (HTML, CSS and JavaScript in one file)
├── README.md
└── .gitignore
```

`students.json` is listed in `.gitignore`. It is generated while using the program and changes on every run, so it does not need to be in the repository.

---

## Limitations

I would rather say these upfront than have them found later.

- The web login is front-end only. Accounts live in one browser, so an account made on a phone will not exist on a laptop. A real login system needs a server and a database.
- Data is not shared between browsers or devices.
- I tested everything by hand. There are no automated tests.
- The console version uses plain functions, lists and dictionaries on purpose, to keep the code easy to follow. It does not use classes.

---

## Ideas for later

- Sort students by marks or name
- Store marks for several subjects instead of one
- Export the list to CSV
- Back the web version with a real database so accounts and records work across devices

---

## Built with

- Python 3 (standard library only: `json`, `os`)
- HTML, CSS and vanilla JavaScript, no frameworks or libraries

---

Made by Anurag Banerjee 
