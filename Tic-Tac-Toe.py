import random
while True:
    pos = ["1","2","3","4","5","6","7","8","9"]
    prompt = ["$$$!!!YOU WIN!!!$$$","YOU LOOSE","It's a draw"]
    j = 1
    k = 1
    l = 0
    pcvalue = []
    pc = random.randint(0,8)

    while j <= 2:
        print("Choose 'X' or 'O' to play: ")
        sign = input().upper()
        if sign == "X":
            pcsign = "O"
            break
        elif sign == "O":
            pcsign = "X"
            break
        else:
            print("Please enter valid INPUT: ")

    print("     |     |     ")
    print("  " + pos[0] + "  |  " + pos[1] + "  |  " + pos[2] + "  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  " + pos[3] + "  |  " + pos[4] + "  |  " + pos[5] + "  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  " + pos[6] + "  |  " + pos[7] + "  |  " + pos[8] + "  ")
    print("     |     |     ")
    print(" ")

    while l <= 8:
        pos[l] = " "
        l += 1

    while j <= 5:
        print("Enter the number")
        value = input()
        if value == "1":
            if pos[0] == " ":
                pos[0] = sign
                pcvalue.append(0)
                if " " not in pos:
                    break
                while pc in pcvalue:
                    pc = random.randint(0,8)
                pcvalue.append(pc)
                pos[pc] = pcsign
            else:
                print("You cheated")
                break
        elif value == "2":
            if pos[1] == " ":
                pos[1] = sign
                pcvalue.append(1)
                if " " not in pos:
                    break
                while pc in pcvalue:
                    pc = random.randint(0,8)
                pcvalue.append(pc)
                pos[pc] = pcsign
            else:
                print("You cheated")
                break
        elif value == "3":
            if pos[2] == " ":
                pos[2] = sign
                pcvalue.append(2)
                if " " not in pos:
                    break
                while pc in pcvalue:
                    pc = random.randint(0,8)
                pcvalue.append(pc)
                pos[pc] = pcsign
            else:
                print("You cheated")
                break
        elif value == "4":
            if pos[3] == " ":
                pos[3] = sign
                pcvalue.append(3)
                if " " not in pos:
                    break
                while pc in pcvalue:
                    pc = random.randint(0,8)
                pcvalue.append(pc)
                pos[pc] = pcsign
            else:
                print("You cheated")
                break
        elif value == "5":
            if pos[4] == " ":
                pos[4] = sign
                pcvalue.append(4)
                if " " not in pos:
                    break
                while pc in pcvalue:
                    pc = random.randint(0,8)
                pcvalue.append(pc)
                pos[pc] = pcsign
            else:
                print("You cheated")
                break
        elif value == "6":
            if pos[5] == " ":
                pos[5] = sign
                pcvalue.append(5)
                if " " not in pos:
                    break
                while pc in pcvalue:
                    pc = random.randint(0,8)
                pcvalue.append(pc)
                pos[pc] = pcsign
            else:
                print("You cheated")
                break
        elif value == "7":
            if pos[6] == " ":
                pos[6] = sign
                pcvalue.append(6)
                if " " not in pos:
                    break
                while pc in pcvalue:
                    pc = random.randint(0,8)
                pcvalue.append(pc)
                pos[pc] = pcsign
            else:
                print("You cheated")
                break
        elif value == "8":
            if pos[7] == " ":
                pos[7] = sign
                pcvalue.append(7)
                if " " not in pos:
                    break
                while pc in pcvalue:
                    pc = random.randint(0,8)
                pcvalue.append(pc)
                pos[pc] = pcsign
            else:
                print("You cheated")
                break
        elif value == "9":
            if pos[8] == " ":
                pos[8] = sign
                pcvalue.append(8)
                if " " not in pos:
                    break
                while pc in pcvalue:
                    pc = random.randint(0,8)
                pcvalue.append(pc)
                pos[pc] = pcsign
            else:
                print("You cheated")
                break
        else:
            print("INVALID INPUT")
            break
        print("     |     |     ")
        print("  " + pos[0] + "  |  " + pos[1] + "  |  " + pos[2] + "  ")
        print("_____|_____|_____")
        print("     |     |     ")
        print("  " + pos[3] + "  |  " + pos[4] + "  |  " + pos[5] + "  ")
        print("_____|_____|_____")
        print("     |     |     ")
        print("  " + pos[6] + "  |  " + pos[7] + "  |  " + pos[8] + "  ")
        print("     |     |     ")
        print(" ")

        a = pos[0] == pos[1] == pos[2] == sign
        b = pos[3] == pos[4] == pos[5] == sign
        c = pos[6] == pos[7] == pos[8] == sign
        d = pos[0] == pos[3] == pos[6] == sign
        e = pos[1] == pos[4] == pos[7] == sign
        f = pos[2] == pos[5] == pos[8] == sign
        g = pos[0] == pos[4] == pos[8] == sign
        h = pos[2] == pos[4] == pos[6] == sign
        abc = a or b or c or d or e or f or g or h
        a2 = pos[0] == pos[1] == pos[2] == pcsign
        b2 = pos[3] == pos[4] == pos[5] == pcsign
        c2 = pos[6] == pos[7] == pos[8] == pcsign
        d2 = pos[0] == pos[3] == pos[6] == pcsign
        e2 = pos[1] == pos[4] == pos[7] == pcsign
        f2 = pos[2] == pos[5] == pos[8] == pcsign
        g2 = pos[0] == pos[4] == pos[8] == pcsign
        h2 = pos[2] == pos[4] == pos[6] == pcsign
        abc2 = a2 or b2 or c2 or d2 or e2 or f2 or g2 or h2
        if  abc:
            print(prompt[0])
            break
        elif  abc2:
            print(prompt[1])
            break
        j += 1
    if " " not in pos:
        a = pos[0] == pos[1] == pos[2] == sign
        b = pos[3] == pos[4] == pos[5] == sign
        c = pos[6] == pos[7] == pos[8] == sign
        d = pos[0] == pos[3] == pos[6] == sign
        e = pos[1] == pos[4] == pos[7] == sign
        f = pos[2] == pos[5] == pos[8] == sign
        g = pos[0] == pos[4] == pos[8] == sign
        h = pos[2] == pos[4] == pos[6] == sign
        abc = a or b or c or d or e or f or g or h
        a2 = pos[0] == pos[1] == pos[2] == pcsign
        b2 = pos[3] == pos[4] == pos[5] == pcsign
        c2 = pos[6] == pos[7] == pos[8] == pcsign
        d2 = pos[0] == pos[3] == pos[6] == pcsign
        e2 = pos[1] == pos[4] == pos[7] == pcsign
        f2 = pos[2] == pos[5] == pos[8] == pcsign
        g2 = pos[0] == pos[4] == pos[8] == pcsign
        h2 = pos[2] == pos[4] == pos[6] == pcsign
        abc2 = a2 or b2 or c2 or d2 or e2 or f2 or g2 or h2
        print("     |     |     ")
        print("  " + pos[0] + "  |  " + pos[1] + "  |  " + pos[2] + "  ")
        print("_____|_____|_____")
        print("     |     |     ")
        print("  " + pos[3] + "  |  " + pos[4] + "  |  " + pos[5] + "  ")
        print("_____|_____|_____")
        print("     |     |     ")
        print("  " + pos[6] + "  |  " + pos[7] + "  |  " + pos[8] + "  ")
        print("     |     |     ")
        print(" ")
        if not abc and not abc2:
            print(prompt[2])
        elif abc:
            print(prompt[0])
        elif abc2:
            print(prompt[1])
    outlet=input("do you want to stop playing yes/no?").lower()
    if outlet=="yes":
        break