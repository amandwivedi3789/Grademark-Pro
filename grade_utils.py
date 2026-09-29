from config import GRADES, PASS_MARKS

def calculate_percentage(obtained, total):
    if total <= 0 or obtained < 0 or obtained > total:
        raise ValueError("Invalid marks entered.")
    return (obtained / total) * 100

def get_grade_info(percentage):
    for mark, grade, points in GRADES:
        if percentage >= mark:
            return grade, points
    return "F", 0

def is_pass(marks):
    return marks >= PASS_MARKS
