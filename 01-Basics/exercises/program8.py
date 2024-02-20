# Quadratic Equation Solver: Write a script that solves quadratic equations (ax^2 + bx + c = 0),
# handling both real and complex roots

import math

def solve_quadratic(a, b, c):
    # Calculate the inside of the root
    inner_root = (b**2) - (4*a*c)
    
    # Check if the inside of the root is positive, negative, or zero
    if inner_root > 0:
        # Two real and distinct roots
        root1 = (-b + math.sqrt(inner_root)) / (2*a)
        root2 = (-b - math.sqrt(inner_root)) / (2*a)
        return root1, root2
    elif inner_root == 0:
        # Two real and equal roots
        root = -b / (2*a)
        return root, root
    else:
        # Two complex roots
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(inner_root)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2


a = 1
b = -3
c = 2
root1, root2 = solve_quadratic(a, b, c)
print(f"Root 1: {root1}")
print(f"Root 2: {root2}")
