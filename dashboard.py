from grade_utils import is_pass

def get_statistics(students):
    total = len(students)
    if not total:
        return {"total": 0, "average": 0, "passed": 0, "failed": 0}
    average = sum(float(s["marks"]) for s in students) / total
    passed = sum(1 for s in students if is_pass(float(s["marks"])))
    return {"total": total, "average": average,
            "passed": passed, "failed": total - passed}
