# Importing the math module
import math

# Defining a function called 'calculate_area_of_polygon' that takes two arguments: sides and length
def calculate_area_of_polygon(sides, length):
    # Calculate the area of a regular polygon using the formula:
    # Area = (n * s^2) / (4 * tan(pi / n))
    # where n is the number of sides, s is the length of each side,
    # and pi is the mathematical constant pi.
    return (sides * length ** 2) / (4 * math.tan(math.pi / sides))

# Defining a function called 'main'
def main():
    try:
        # Prompting the user to enter the number of sides of the polygon and converting it to an integer
        sides = int(input("Enter the number of sides of the polygon: "))
        
        # Prompting the user to enter the length of each side of the polygon and converting it to a float
        length = float(input("Enter the length of each side of the polygon: "))
        
        # Checking if the number of sides is less than 3
        if sides < 3:
            # Raising a ValueError if the number of sides is less than 3
            raise ValueError("A polygon must have at least 3 sides.")
        
        # Calculating the area of the regular polygon using the 'calculate_area_of_polygon' function
        area = calculate_area_of_polygon(sides, length)
        
        # Printing the calculated area with two decimal places
        print(f"The area of the regular polygon is: {area:.2f} square units.")
    
    # Handling the case where the user enters a non-integer value for the number of sides or a negative value for the length of each side
    except ValueError as e:
        # Printing an error message
        print(f"Error: {e}")

# Calling the 'main' function
main()
