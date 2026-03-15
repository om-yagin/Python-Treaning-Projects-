import random
import string

print("Welcome to password generator:\n")

total_target = int(input("Enter the total number of characters in the password:\n"))

password = []

num_letters = int(input("How many letters?\n"))
password += random.choices(string.ascii_lowercase, k=num_letters)

num_numbers = int(input("How many numbers?\n"))
password += random.choices(string.digits, k=num_numbers)

num_symbols = int(input("How many symbols?\n"))
password += random.choices(string.punctuation, k=num_symbols)

total_entered = num_letters + num_numbers + num_symbols

if total_entered == total_target:

    random.shuffle(password)
    final_password = "".join(password)
    
    print("\nHere is your password:")
    print(final_password)
else:
    print(f"\nError! Your total ({total_target}) does not match the sum of parts ({total_entered}).")
