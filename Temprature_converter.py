print("Choose temperature unit")
print(" 1. Celsius")
print(" 2. Fahrenheit")
print(" 3. Kelvin")
x = int(input())
print("Enter temperature value")
y = float(input())
if x == 1:
    print(str(y) + " degree celsius in")
    print("Fahrenheit = " + str((y * (9/5) + 32)))
    print("Kelvin = " + str(y + 273.15))
elif x == 2:
    print(str(y) + " degree fahrenheit in")
    print("Celsius = " + str(((y - 32) * (5 / 9))))
    print("Kelvin = " + str(((y - 32) * (5 / 9)) + 273.15))
elif x == 3:
    print(str(y) + " degree Kelvin in")
    print("Celsius = " + str(y - 273))
    print("Fahrenheit = " + str((y - 273) * (9/5) + 32))
else:
    print("INVALID INPUT")
