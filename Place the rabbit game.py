print("Welcome to place the rabbit 🐇\n")

field = [  ["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"] ]

print(f"{field[0]}\n{field[1]}\n{field[2]}")

print("\nWhere should the rabbit go?")

position = input("Please choose a row and a column (e.g. 2,3): ")

row, column = position.split(",")

row = int(row.strip())
column = int(column.strip())

if row < 1 or row > 3 or column < 1 or column > 3:
    print("\n❌ Error: numbers must be between 1 and 3")

else:
    field[row - 1][column - 1] = "🐇"
    print("\n✅ Success!\n")
    print(f"{field[0]}\n{field[1]}\n{field[2]}")
