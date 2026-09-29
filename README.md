# GradeMark Pro
## Student Grade and Marks Management System

### Overview
GradeMark Pro is a Python desktop application using Tkinter for managing student academic records, calculating percentages/grades, and displaying basic class performance statistics.

### Problem Statement
Manual student-mark management can be time-consuming and can cause record and calculation errors. GradeMark Pro provides a centralized desktop interface for student CRUD operations, grade calculation, validation, and JSON persistence.

### Objectives
- Manage student academic records.
- Provide add, edit and delete operations.
- Calculate percentage, grade and grade points.
- Display class average, pass and fail counts.
- Validate user input.
- Persist data using JSON.
- Demonstrate modular Python development.

### Major Functional Modules
1. Dashboard
2. Student Management / CRUD
3. Marks Calculator
4. Data Management
5. Validation and Grade Utilities

### Technologies
Python 3, Tkinter/ttk, JSON, unittest, Git/GitHub.

### Grading Scale
| Percentage | Grade | Points |
|---|---|---|
| 90+ | A+ | 10 |
| 80–89 | A | 9 |
| 70–79 | B+ | 8 |
| 60–69 | B | 7 |
| 50–59 | C | 6 |
| 40–49 | D | 5 |
| Below 40 | F | 0 |

### Installation and Run
1. Install Python 3.x.
2. Extract/clone this project.
3. Open a terminal in the project folder.
4. Run `python main.py`.

### Testing
Run:
`python -m unittest discover -s tests -p "test_*.py"`

### Project Structure
```text
main.py                 GUI and application entry
data_manager.py         JSON storage
student_manager.py     Student CRUD logic
grade_utils.py          Percentage/grade/pass logic
calculator.py           Calculator logic
dashboard.py            Dashboard statistics
validation.py           Input validation
config.py               Constants
students.json           Persistent records
tests/                  Unit tests
docs/                   Design documentation and diagrams
screenshots/            Application screenshots
```

### Data Storage
Student records are stored in `students.json`. The application loads the records when it starts and saves changes after add, update, and delete operations.

### Non-Functional Requirements
- Usability: simple tab-based GUI.
- Reliability: validation and error handling.
- Maintainability: separated modules.
- Resource efficiency: lightweight standard-library implementation.

### Future Enhancements
Authentication, subject-wise marks, GPA/CGPA, charts, export to PDF/CSV, database support, advanced search/filtering, and expanded automated testing.

### Academic Submission
This repository is organized to support the VITyarthi Build Your Own Project submission requirements. The detailed project report is in `docs/GradeMark_Pro_Project_Report.pdf`.

## VITyarthi Submission Files
- `statement.md` — problem statement, scope, target users and high-level features.
- `docs/VITyarthi_Requirement_Mapping.md` — requirement-to-project mapping.
- `docs/GradeMark_Pro_Project_Report.pdf` — detailed project report.
- `docs/diagrams/` — architecture, workflow, use case, class/component, sequence and ER/storage diagrams.
- `docs/testing_report.md` — automated and manual testing plan.
- `GITHUB_SETUP.md` — repository setup steps.
- `SUBMISSION_CHECKLIST.md` — final submission checklist.

## Student Details
Update the report cover with your name, registration/roll number, course/subject, faculty/instructor, institution and academic year/semester before submission.
