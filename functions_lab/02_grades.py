def grade(grade_number):
    if grade_number < 3:
        return 'Fail'
    elif grade_number < 3.5:
        return 'Poor'
    elif grade_number < 4.5:
        return 'Good'
    elif grade_number < 5.5:
        return 'Very Good'
    elif grade_number <= 6:
        return 'Excellent'


current_grade = float(input())

print(grade(current_grade))
