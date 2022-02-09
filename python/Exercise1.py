num1 = 1
num2 = 1

while num1 != 0 and num2 != 0:
    num1 = int(input("enter the first number: "))
    num2 = int(input("enter the second number: "))
    if num1 > num2:
        print("the first number is bigger\n")
    elif num1 < num2:
        print("the second number is bigger\n")
    else:
        print("they are equal\n")
