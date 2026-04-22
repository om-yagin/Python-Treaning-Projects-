import string

letters = string.ascii_lowercase

words = input("Enter a sentence: \n").lower()

co_word = ""

for letter in words:

    if letter == " ":
        co_word += " "

    else:
        org_posi = letters.index(letter)
        new_posi = (org_posi + 1) % len(letters)
        co_word += letters[new_posi]

print(f"Here is your encrypted sentence:\n {co_word}")
