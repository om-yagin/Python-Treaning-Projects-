import random
words=["good","hello","ugly","bad","night"]
random_word=random.choice(words)
space=[]
for letter in random_word:
    space+="_"
print(space)

while "_" in space:
    guess=input("guess a letter: ")

    for position in range(len(random_word)):
        if random_word[position] == guess:
            space[position]=guess
        
    print(space)
    print("_")
print("congratulations!, you guess it")
