import string

sentence=input("enter a sentence with symbols: \n")
cle_sentence=""

for char in sentence:
    if char not in string.punctuation:
        cle_sentence+=char
        
print("\n ****here is your sentence without symbls: \n")
print(cle_sentence)
