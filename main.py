from typing import list, dict

a: list = [1, 2, 3]
while a:
    i=a.pop()
    print(i)

d:dict={'a':1, 'b':2}

def my_func(s: list):
    for i in s:
        print(i)

my_func(a)