def calculate_grade(test_score):
    if test_score >= 90:
        return "A"
    elif test_score in range(80,90):
        return "B"
    elif test_score in range(70,80):
        return "C"
    elif test_score in range(70,80):
        return "D"
    elif test_score <= 69:
        return "F"
    else:
        return "unknown"