from grade_utils import calculate_percentage, get_grade_info
from validation import validate_calculator

def calculate_result(obtained, total):
    obtained, total = validate_calculator(obtained, total)
    percentage = calculate_percentage(obtained, total)
    grade, points = get_grade_info(percentage)
    return percentage, grade, points
