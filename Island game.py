print("Welcome to our island 🏝️")
print("There is two doors 🚪. one is blue 🔵 and the other is red 🔴")

door = input("Which one you want to open? ").lower()

if door == "blue":
    print("Ops! you chose the crocodile door 🐊🐊🐊")
    print("Game over.")

elif door == "red":
    print("Great! now you entered the room and you found three boxes 🎁🎁🎁: white, black, green.")
    box = input("Which box you will open? ").lower()

    if box == "white":
        print("Ops! you opened a box filled with snakes 🐍🐍")
    elif box == "black":
        print("Ops! You opened a box filled with spiders 🕷️🕷️")
    elif box == "green":
        print("Congratulations! You found the treasure! 💰💰💰")
    else:
        print("Invalid choice!")

else:
    print("Invalid choice!")
