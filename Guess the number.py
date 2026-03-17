import random
correct_number=random.randint(1,10)
num=int(input("Guess a number from 1 to 10: \n"))
while num!=correct_number:
    if num>correct_number:
        num=int(input("too high! try again: \n"))
    else:  
        num=int(input("too low! try again: \n"))
print("congragulations!you gess it!")
