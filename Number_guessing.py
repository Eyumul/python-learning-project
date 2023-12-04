import random
i = 1
number = random.randint(1,100)
print("Guess a number:")
while i <= 10:
    x = int(input())
    if x == number:
        print("CONGRAT YOU GOT THE NUMBER")
        break
    elif x > number:
        print("It is high, Try again")
    elif x < number:
        print("It is low, Try again")
    else:
        print("Invalid input")
        break