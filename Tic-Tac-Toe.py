import random
def play(value,pc):
        num = int(value)
        if choice == value:
                if pos[num - 1] == " ":
                    pos[num -1] = sign
                    pcvalue.append(num-1)
                    while pc in pcvalue and len(pcvalue) != 9:
                        pc = random.randint(0,8)
                    pcvalue.append(pc)
                    pos[pc] = pcsign
                else:
                    print("You cheated")
                    return 0
def grid(a,b,c,d,e,f,g,h,i):
        print("     |     |     ")
        print("  " + a + "  |  " + b + "  |  " + c + "  ")
        print("_____|_____|_____")
        print("     |     |     ")
        print("  " + d + "  |  " + e + "  |  " + f + "  ")
        print("_____|_____|_____")
        print("     |     |     ")
        print("  " + g + "  |  " + h + "  |  " + i + "  ")
        print("     |     |     ")
        print(" ")
def check(a0,a1,a2,a3,a4,a5,a6,a7,a8,checksign):
        a = a0 == a1 == a2 == checksign
        b = a3 == a4 == a5 == checksign
        c = a6 == a7 == a8 == checksign
        d = a0 == a3 == a6 == checksign
        e = a1 == a4 == a7 == checksign
        f = a2 == a5 == a8 == checksign
        g = a0 == a4 == a8 == checksign
        h = a2 == a4 == a6 == checksign
        abc = a or b or c or d or e or f or g or h
        return abc
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
    grid(pos[0],pos[1],pos[2],pos[3],pos[4],pos[5],pos[6],pos[7],pos[8])
    while l <= 8:
        pos[l] = " "
        l += 1
    while j <= 5:
        print("Enter the number")
        choice = input()
        while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8" and choice != "9":
             print("INVALID INPUT\n Please Tryagain: ")
             grid(pos[0],pos[1],pos[2],pos[3],pos[4],pos[5],pos[6],pos[7],pos[8])
             choice = input()
        if play(choice,pc) == 0:
             break
        grid(pos[0],pos[1],pos[2],pos[3],pos[4],pos[5],pos[6],pos[7],pos[8])
        if  check(pos[0],pos[1],pos[2],pos[3],pos[4],pos[5],pos[6],pos[7],pos[8],sign):
            print(prompt[0])
            break
        elif  check(pos[0],pos[1],pos[2],pos[3],pos[4],pos[5],pos[6],pos[7],pos[8],pcsign):
            print(prompt[1])
            break
        if " " not in pos:
            grid(pos[0],pos[1],pos[2],pos[3],pos[4],pos[5],pos[6],pos[7],pos[8])
            if not check(pos[0],pos[1],pos[2],pos[3],pos[4],pos[5],pos[6],pos[7],pos[8],sign) and not check(pos[0],pos[1],pos[2],pos[3],pos[4],pos[5],pos[6],pos[7],pos[8],pcsign):
                print(prompt[2])
            elif check(pos[0],pos[1],pos[2],pos[3],pos[4],pos[5],pos[6],pos[7],pos[8],sign):
                print(prompt[0])
            elif check(pos[0],pos[1],pos[2],pos[3],pos[4],pos[5],pos[6],pos[7],pos[8],pcsign):
                print(prompt[1])
            break
        j += 1
    outlet=input("do you want to stop playing yes/no?").lower()
    if outlet=="yes":
        break