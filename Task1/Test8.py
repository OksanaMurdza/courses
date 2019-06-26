from random import randint

first = int(input("First range "))
last = int(input("2 range "))

a = randint(first, last)
b = int(input("Write number "))
if a == b:
    print("You win")
else:
    b = int(input("Write again "))
    if a == b:
        print("You win")
    else:
        print("Fail")