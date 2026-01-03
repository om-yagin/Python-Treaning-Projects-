students = []

print("Enter student names (type 'done' to finish):")

while True:
    name = input("Student name: ")

    if name.lower() == "done":
        break

    students.append(name)

present_students = []
absent_students = []

for student in students:
    while True:
        answer = input(f"Is {student} present? (yes/no): ").lower()

        if answer == "yes":
            present_students.append(student)
            break
        elif answer == "no":
            absent_students.append(student)
            break
        else:
            print("Please type yes or no")

print("\n===== Final Attendance =====")

print("\nPresent students:")
for s in present_students:
    print("-", s)

print("\nAbsent students:")
for s in absent_students:
    print("-", s)
