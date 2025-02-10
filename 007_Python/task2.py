#code to grade students based on their score

def grade_student(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

scores = [95, 85, 72, 58, 67]

for score in scores:
    grade = grade_student(score)
    print(f"Score: {score}, Grade: {grade}")
