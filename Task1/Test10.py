def charFreq(n):
    dict = {}
    for i in (range(len(n))):
        if (n[i] in dict):
            dict[n[i]] = int(dict.get(n[i])) + 1
        else:
            dict[n[i]] = 1
    return dict

text = input("Enter string:")
n = charFreq(text)

print(n)