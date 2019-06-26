import sys

def start():
    revers("abc")

def revers(str):
    new_str = ""
    for i in str:
        new_str = i + new_str
    print("revers str", str, "=", new_str)

start()