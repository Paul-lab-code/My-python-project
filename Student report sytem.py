def calc_average(score):
    return sum(score) / len(score)


def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


student = {}
choice = "yes"
print("--- Student Gradebook Manager ---")
while choice == "yes":
    name = input("Enter student name: ")
    score_input1 = int(input("Enter student scores for maths: "))
    score_input2 = int(input("enter scores for english: "))
    score_input3 = int(input("enter scores for science: "))
    score = []
    score.extend([score_input1, score_input2, score_input3])
    average = calc_average(score)
    grade = assign_grade(average)
    student[name] = {
        "scores": score,
        "average": average,
        "grade": grade
    }
    choice = input("Do you want to add another student? (yes/no): ")
print("--- Gradebook Summary ---")
for x, y in student.items():
    print(f"{x}: {y}")
choice3 = "yes"
while choice3 == "yes":
    choice2 = input("Enter students name to view details: ")
    if choice2 in student:
        detail = student[choice2]
        print(f"score: {detail}")
    else:
        print("student record not found.")
    choice3 = input("do you want to enter another student name? ")
