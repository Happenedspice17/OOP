# def country_name(country: str = "Mexico") -> str:
#     return f"The country is {country}"

# # Once a default value is set, all the parameters to the right of it 
# # must also have a default value
# def say_hello(name: str, age: int = 33, height: float = 1.90) -> str:
#     return "Hello " + name + ", I'm " + str(age) + " years old and I'm " + str(height) + " meters tall."

# print(country_name("USA"))
# print(country_name())

# class Person:
#     def __init__(self, name: str, age: int, height: float) -> None:
#         self.name = name
#         self.age = age
#         self.hobbies = []
#         self.height = height
#         #self.say_hello()

#     def say_hello(self, talk: bool = True) -> str:
#         if talk == True:
#             print("Hello my name is " + self.name)
#             return ""
#         else:
#             return "Hello my name is " + self.name

#     def say_age(self) -> str:
#         #print("I am " + str(self.age) + " years old")
#         #print(f"I am {self.age} years old")
#         return "I am " + str(self.age) + " years old"
    
#     def birthday(self) -> None:
#         self.age += 1
    
#     def add_hobby(self, hobby: str) -> None:
#         self.hobbies.append(hobby)
    
#     def say_hobbies(self) -> None:
#         print("My hobbies are: ")
#         for hobby in self.hobbies:
#             print(hobby)

# my_person = Person("John", 25, 1.75)
# my_person.name = "David"
# my_person.age = 33

# print(my_person.say_hello(False) + ". " + my_person.say_age())
# print(f"{my_person.say_hello(False)}. {my_person.say_age()}") # f-string which is a formatted string

# my_person.birthday()
# print(my_person.say_age())

# my_person.add_hobby("Reading")
# my_person.add_hobby("Playing video games")
# my_person.add_hobby("Watching movies")
# my_person.say_hobbies()

class Point2D:
    def __init__(self) -> None:
        self.x_pos = 0.0
        self.y_pos = 0.0

    def set_x(self, x: float) -> None:
        self.x_pos = x
    
    def set_y(self, y: float) -> None:
        self.y_pos = y
    
    def get_x(self) -> float:
        return self.x_pos
    
    def get_y(self) -> float:
        return self.y_pos
    
    def __add__(self, other):
        new_point = Point2D()
        new_point.x_pos = self.x_pos + other.x_pos
        new_point.y_pos = self.y_pos + other.y_pos
        return new_point

    def __str__(self) -> str:
        return f"({self.x_pos}, {self.y_pos})"



my_point1 = Point2D()
my_point1.x_pos = 5
my_point1.y_pos = 10

my_point2 = Point2D()
my_point2.set_x(10)
my_point2.set_y(20)

my_point3 = Point2D()
my_point3 = my_point1 + my_point2
#my_point3 += my_point1
#my_point3 += my_point2
print(my_point3.get_x())
print(my_point3.get_y())

print(my_point3)