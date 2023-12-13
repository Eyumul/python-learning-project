import random

n2 = n1 = n0 = 0
while n2 <= 9:
    while n1 <= 9:
        while n0 <= 9:
            if n2 == 5 or n2 == 7 or n2 == 8 or n1 == 5 or n1 == 7 or n1 == 8 or n0 == 5 or n0 == 7 or n0 == 8:
                n0 += 1
                continue
            if n2 == 2 or n1 == 9 or n0 == 1:
                if n2 == 4 or n1 == 2 or n0 == 2 or n0 == 4:
                    if (n2 == 6 and n1 == 4) or (n1 == 4 and n0 == 6) or (n2 == 6 and n0 == 4) or (n2 == 3 and n1 == 4) or (n1 == 3 and n0 == 4) or (n2 == 3 and n0 == 4) or (n2 == 6 and n1 == 3) or (n1 == 3 and n0 == 6) or (n2 == 3 and n0 == 6):
                        if n2 == 6 or n2 == 9 or n1 == 9 or n0 == 6:
                            print (str(n2)+str(n1)+str(n0))
            n0 += 1
        n0 = 0
        n1 += 1
    n1 = 0
    n2 += 1