AR_list = []

while True:
    print("\n--- MENU ---")
    print("1- Add person")
    print("2- Remove person")
    print("3- Show list")
    print("4- Exit")

    choice = input("Choose a number: ").lower()


    if choice in ["1", "add"]:
        name = input("Enter name: ")
        age = input("Enter age: ")

        person = {
            "name": name,
            "age": age
        }

        AR_list.append(person)
        print("✅ Added successfully")


    elif choice in ["2", "remove"]:
        name = input("Enter name to remove: ")

        found = False
        for person in AR_list:
            if person["name"] == name:
                AR_list.remove(person)
                print("✅ Removed successfully")
                found = True
                break

        if not found:
            print("❌ Name not found")


    elif choice in ["3", "show"]:
        if len(AR_list) == 0:
            print("📭 No people yet")
        else:
            print("\n--- People List ---")
            for i, person in enumerate(AR_list, start=1):
                print(f"{i}- {person['name']} ({person['age']})")


    elif choice in ["4", "exit"]:
        print("👋 Bye!")
        break

    else:
        print("❌ Invalid choice")
