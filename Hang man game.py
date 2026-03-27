import random

words = ["good", "bad", "ugly", "apple", "banana", "water", "milk","cat","dog","sun","moon"]
random_word = random.choice(words)

display = []
for letter in random_word:
    display.append("_")

lives = 6
guessed_letters = []

# رسومات Hangman
stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]

while "_" in display and lives > 0:
    print(stages[6 - lives])
    print("Word:", " ".join(display))
    print("Guessed letters:", guessed_letters)

    guessed = input("Please guess a letter: ").lower()

    # تحقق من الإدخال (حرف واحد فقط)
    if len(guessed) != 1:
        print("⚠️ Please enter only ONE letter")
        continue

    # منع التكرار
    if guessed in guessed_letters:
        print("⚠️ You already guessed this letter")
        continue

    guessed_letters.append(guessed)

    # تحقق من الحرف
    if guessed not in random_word:
        lives -= 1
        print(f"❌ Wrong! {lives} lives left")
    else:
        for position in range(len(random_word)):
            if random_word[position] == guessed:
                display[position] = guessed

# النتيجة
if "_" not in display:
    print("🎉 YOU WIN!")
else:
    print(stages[6])
    print("💀 YOU LOSE! The word was:", random_word)
