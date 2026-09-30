from data_manager import load_students, save_students

class StudentManager:
    def __init__(self):
        self.students = load_students()

    def add(self, student):
        if any(s["roll"] == student["roll"] for s in self.students):
            raise ValueError("Roll number already exists.")
        self.students.append(student)
        save_students(self.students)

    def update(self, old_roll, student):
        if old_roll != student["roll"] and any(
            s["roll"] == student["roll"] for s in self.students):
            raise ValueError("Roll number already taken.")
        for i, item in enumerate(self.students):
            if item["roll"] == old_roll:
                self.students[i] = student
                save_students(self.students)
                return
        raise ValueError("Student not found.")

    def delete(self, roll):
        self.students = [s for s in self.students if s["roll"] != roll]
        save_students(self.students)

    def find(self, roll):
        return next((s for s in self.students if s["roll"] == roll), None)
