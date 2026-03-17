def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "Fail"

subjects = int(input("Enter number of subjects: "))
total = 0

for i in range(subjects):
    marks = float(input("Enter marks: "))
    total += marks

average = total / subjects

grade = calculate_grade(average)

print("Total:", total)
print("Average:", average)
print("Grade:", grade)