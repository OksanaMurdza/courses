def polindrom(str):
    newStr = str[::-1]
    if str == newStr:
        print("True")
    else:
        print("False")

polindrom("radar")