import json
import os
from config import DATA_FILE

def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []

def save_students(students):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)

def add_student(student):
    students = load_students()
    students.append(student)
    save_students(students)

def update_students(students):
    save_students(students)

def delete_student(roll_no):
    students = [s for s in load_students() if s["roll"] != roll_no]
    save_students(students)

def find_student(roll_no):
    return next((s for s in load_students() if s["roll"] == roll_no), None)
