import random
fname = input("Enter your firstname: ")
lname = input("Enter your lastname: ")
age = input("Enter your age: ")
special = ["!","@","#","$","%","^","&","*","~","?"]
password = ["fname","lname","age","special"]
i = random.randint(0,3)
j = random.randint(0,9)

password[i] = fname
password[i - 1] = age
password[i - 2] = special[j]
password[i - 3] = lname

print(password[0] + password[2] + password[1] + password[3])