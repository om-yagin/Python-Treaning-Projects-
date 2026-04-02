import json

# دالة الحفظ
def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file)

# تحميل البيانات لو موجودة
try:
    with open("students.json", "r") as file:
        students = json.load(file)
except:
    students = []

# لو ما في بيانات، ندخلها أول مرة
if not students:
    num = int(input("How many students are there this year? "))

    for student in range(num):
        name = input(f"What is the name of student {student + 1}: ")
        pers = float(input(f"What is the percentage of student {student + 1}: "))

        person = {"name": name, "pers": pers}
        students.append(person)

    save_data()  # نحفظ بعد الإدخال الأول

# القائمة
while True:
    print("\n1. Add a new student")
    print("2. Remove a student")
    print("3. Edit a student")
    print("4. Show top 10 students")
    print("5. Show passed / failed students")
    print("6. Exit")

    choice = input("Choose a number: ")

    # 1. Add
    if choice == "1":
        name = input("Enter student name: ")
        pers = float(input("Enter percentage: "))
        students.append({"name": name, "pers": pers})
        save_data()
        print("Student added successfully")

    # 2. Remove
    elif choice == "2":
        stu_name = input("Enter student name to remove: ")
        found = False

        for stu in students:
            if stu["name"] == stu_name:
                students.remove(stu)
                save_data()
                print("Removed successfully")
                found = True
                break

        if not found:
            print("Student not found")

    # 3. Edit
    elif choice == "3":
        stu_name = input("Enter student name to edit: ")
        found = False

        for stu in students:
            if stu["name"] == stu_name:
                edit_choice = input("Edit (name / percentage): ").lower()

                if edit_choice == "name":
                    stu["name"] = input("Enter new name: ")

                elif edit_choice == "percentage":
                    stu["pers"] = float(input("Enter new percentage: "))

                else:
                    print("Invalid option")

                save_data()
                print("Edited successfully")
                found = True
                break

        if not found:
            print("Student not found")

    # 4. Top 10
    elif choice == "4":
        sorted_students = sorted(students, key=lambda x: x["pers"], reverse=True)
        top_10 = sorted_students[:10]

        print("\nTop 10 students:")
        for stu in top_10:
            print(f'{stu["name"]} - {stu["pers"]}')

    # 5. Passed / Failed
    elif choice == "5":
        passed = [stu for stu in students if stu["pers"] >= 50]
        failed = [stu for stu in students if stu["pers"] < 50]

        passed_sorted = sorted(passed, key=lambda x: x["pers"], reverse=True)
        failed_sorted = sorted(failed, key=lambda x: x["pers"])

        print(f"\nPassed students ({len(passed_sorted)}):")
        for stu in passed_sorted:
            print(f'{stu["name"]} - {stu["pers"]}')

        print(f"\nFailed students ({len(failed_sorted)}):")
        for stu in failed_sorted:
            print(f'{stu["name"]} - {stu["pers"]}')

    # 6. Exit
    elif choice == "6":
        print("bye")
        break

    else:
        print("Invalid choice, try again")
