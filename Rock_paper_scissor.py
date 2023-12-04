import random

print("'Rock', 'Paper' or 'Scissor': ")
print(" And 'exit' to quit:")

i = 1
while i <= 2:
    choose = input().upper()
    x = random.randint(1, 3)
    if choose == "ROCK":
        if x == 1:
            print(" YOU   Computer")
            print(" Rock    Rock")
            print("It's a draw")
        elif x == 2:
            print(" YOU   Computer")
            print(" Rock    Scissor")
            print("You win")
        elif x == 3:
            print(" YOU   Computer")
            print(" Rock    Paper")
            print("You Loose")
    elif choose == "PAPER":
        x = random.randint(1, 3)
        if x == 1:
            print(" YOU   Computer")
            print(" Paper    Rock")
            print("You win")
        elif x == 2:
            print(" YOU   Computer")
            print(" Paper    Scissor")
            print("You Loose")
        elif x == 3:
            print(" YOU   Computer")
            print(" Paper    Paper")
            print("It's a draw")
    elif choose == "SCISSOR":
        x = random.randint(1, 3)
        if x == 1:
            print(" YOU   Computer")
            print(" Scissor    Rock")
            print("You Loose")
        elif x == 2:
            print(" YOU   Computer")
            print(" Scissor    Scissor")
            print("It's a draw")
        elif x == 3:
            print(" YOU   Computer")
            print(" Scissor    Paper")
            print("You Win")
    elif choose == "EXIT":
        break
    else:
        print("Invalid input")