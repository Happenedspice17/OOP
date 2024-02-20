# Tuples
# Tuples are similar to lists, but inmutable
# meaning that values in a tuple cannot be changed.

# to define a tuple, we use parenteses

# List Mutable, ordered, multiple values at same []
# Tuple Unmutable, ordered, multilple values ()
# Sets Mutable, unordered, not allow repeated elements {}

# Create a tuple

t = (1, 2, 3, 4, 5)

print(t)
print(t[0])

# Only way to modify
list_t = list(t)
list_t.append(6)
t = tuple(list_t)

# Like a list of constants

# Sets

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

for element in set_a:
    print(element)

# Set operations
# Intersections
print(set_a & set_b) # NOT and, just &
# Union
print(set_a | set_b) # Or

# Dictionary to define a person
# Name, last_name, age 

person = {
    "name": "Carlos",
    "last_name": "Escamilla",
    "age": 20
}

print(person["name"])

list_of_people = []
list_of_people.append(person)
print(list_of_people)
print(list_of_people[0]["name"])
