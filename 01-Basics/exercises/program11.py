# Importing the math module
import math

# Defining a function called 'rads_deg' that takes a value in radians and converts it to degrees
def rads_deg(value):
    # Multiplying the value by 180 to convert it to degrees
    deg = value * 180
    
    # Returning the result
    return deg

# Defining a function called 'deg_rads' that takes a value in degrees and converts it to radians
def deg_rads(value):
    # Multiplying the value by pi/180 to convert it to radians
    rad = (value * math.pi) / 180
    
    # Returning the result
    return rad

# Calling the 'rads_deg' function with the argument 2 and printing the result
print(rads_deg(2))

# Calling the 'deg_rads' function with the argument 90 and printing the result
print(deg_rads(90))
