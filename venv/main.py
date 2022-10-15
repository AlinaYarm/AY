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

class Car:
    def __init__(self, color: str, number:int):
    self.color = color
    self.number = numbers
    self.speed = 0

    def move(self):
        print('Погнали!')
        self.speed = 100
    def stop(self):
        print('Приехали...')
        self.speed = 0
car = Car (color='red', number=777)


