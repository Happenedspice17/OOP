
#! Abstraction

#* Determine the qualities of an object

'''
Person has
Name, str
Age, int
Hobbies, list, set, dict
height float

It is better because we have a bunch of variables inside one person
'''

class Person:
    #* Constructor, where you create the object with the attributes that you want it to have
    def __init__(self, name: str, age: int, height: float) -> None:
        self.name = name
        self.age = age
        self.hobbies = []
        self.height = height

    def say_hello(self) -> None:
        print("Hello, my name is " +  self.name)

    def say_age(self) -> None:
        print("I am " + str(self.age) + " years old")

    def birthday(self) -> None:
        self.age += 1

    def add_hobby(self, hobby: str) -> None:
        self.hobbies.append(hobby)

class Point2D:
    def __init__(self) -> None:
        self.x_pos = 0
        self.y_pos = 0

    #* good practice code
    def set_x(self, x: float) -> None:
        self.x_pos = x

    def set_y(self, y: float) -> None:
        self.y_pos = y

    def get_x(self) -> float:
        return self.x_pos
    
    def get_y(self) -> float:
        return self.y_pos


my_point = Point2D()
my_point.set_x(10)
