
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

    def say_hello(self):
        print("Hello, my name is " +  self.name)

    def say_age(self):
        print("I am " + str(self.age) + " years old")

    def birthday(self):
        self.age += 1

    def add_hobby(self, hobby: str) -> None:
        self.hobbies.append(hobby)