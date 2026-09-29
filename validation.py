def validate_student(data):
    if not all(str(v).strip() for v in data.values()):
        raise ValueError("Please fill in all fields.")
    try:
        marks = float(data["marks"])
    except ValueError:
        raise ValueError("Marks must be a valid number.")
    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100.")
    data["marks"] = marks
    return data

def validate_calculator(got, total):
    try:
        got, total = float(got), float(total)
    except ValueError:
        raise ValueError("Please enter valid numbers.")
    if got < 0 or total <= 0 or got > total:
        raise ValueError("Obtained marks must be between 0 and total marks.")
    return got, total
