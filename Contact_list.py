import os

filename = "Contact_list.txt"
while True:
    print("\n1. Add contact\n2. Open contact list\n3. Exit\n")
    user = input()
    if user == "1":
        
        fname  = input("Enter first name: ")
        lname = input("Enter last name: ")
        phone = input("Enter phone number: ")
        open(filename,'a').write("\nFirstname: " + fname)
        open(filename,'a').write("\nLastname: " + lname)
        open(filename,'a').write("\nPhonenumber: " + phone)
        print("contact added")
    elif user == "2":

        if os.path.exists(filename):
            print("\n" + filename + ":\n")
            print("Contacts:\n" + open(filename,'r').read())
        else:
            print("Contact list not found")
    elif user == "3":
        break
    else:
        print("INVALID INPUT")