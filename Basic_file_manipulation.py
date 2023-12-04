import os
i = 1
while i <= 2:
    print("\n1. Create\n2. Open\n3. write\n4. Delete\n5. Exit\n")
    user = int(input())
    if user == 1:
        filename = input("Enter file name to be created(example.txt): ")
        if os.path.exists(filename):
            print("\nFile already exists")
        else:
            open(filename,'x')
            print("file created")
    elif user == 2:
        filename = input("Enter file name to be opened(example.txt): ")
        if os.path.exists(filename):
            print("\n" + filename + ":\n")
            print("File content: " + open(filename,'r').read())
        else:
            print("File not found")
    elif user == 3:
        filename = input("Enter file name to be edited(example.txt): ")
        text  = input("Write a text to add to" + filename + ": ")
        open(filename,'a').write(text)
        print("file opened")
    elif user == 4:
        filename = input("Enter file name to be deleted(example.txt): ")
        if os.path.exists(filename):
            os.remove(filename)
            print("file deleted")
        else:
            print("File not found")
    elif user == 5:
        break
    else:
        print("INVALID INPUT")