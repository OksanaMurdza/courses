def start():
    elements = [1, 2, 3, 4]
    summa(elements)
    multi(elements)

def summa(elements):

    sum = 0
    for i in elements:
        sum = sum + i
    print("Sum =", sum)

def multi(elements):
    res = 1
    for i in elements:
        res = res*i
    print("Multiply =", res)


start()