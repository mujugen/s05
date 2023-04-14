def calculate_letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"


def calculate_grade(participation, summative, final_exam):
    return (participation * 0.3) + (summative * 0.3) + (final_exam * 0.4)


students = []

for _ in range(5):
    name = input("Enter the student's name: ")
    participation = float(input("Enter the class participation grade: "))
    summative = float(input("Enter the summative assessment grade: "))
    final_exam = float(input("Enter the final examination grade: "))

    grade = calculate_grade(participation, summative, final_exam)
    letter_grade = calculate_letter_grade(grade)

    students.append((name, grade, letter_grade))

print("\n{:<15} {:<10} {}".format("Name", "Grade", "Letter Grade"))
print("=" * 30)

for student in students:
    print("{:<15} {:<10.2f} {}".format(student[0], student[1], student[2]))
