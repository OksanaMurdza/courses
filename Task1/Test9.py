def brackets(str):
    i = 1
    for j in str:
        if j=='[':
            i = i + 1
        if j == ']':
            if i > 0:
                i = i - 1

    if i > 1 :
         i = 0
         print(bool(i))
    elif i==1:
         print(bool(i))
    else:
         print(bool(i))

brackets("[[][][][]]")