def caesarCipher(str, number):
    str_new = ""
    for i in str:
        if ord(i) > ord('z'):
            str_new += chr(ord(i) - number)
        else:
            str_new += chr(ord(i) + number)
    print("Sting", str, "=", str_new)

caesarCipher("abc", 5)