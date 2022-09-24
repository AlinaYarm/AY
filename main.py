from typing import List, Dict

a: List = [1, 2, 3]
while a:
    i=a.pop()
    print(i)

d:Dict={'a':1, 'b':2}

def my_func(s: List):
    for i in s:
        print(i)

my_func(a)