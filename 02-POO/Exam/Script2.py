# Script 2 (25 pts)
# 1. Define a function named read_numbers that opens and reads the contents of a file named
# values.txt. This file contains two numbers separated by a dash (-). The function should split these
# numbers, convert them to integers, and return them as two separate values.
# 2. Call the read_numbers function and store the returned values in two variables, num1 and num2.
# 3. Define another function named perform_operations that takes two parameters. These parameters
# will be the variables where you stored the numbers from the file.
# 4. Within the perform_operations function, implement code to print the results of the following
# arithmetic operations:
# 1. Addition (num1 + num2).
# 2. Subtraction (num1 - num2).
# 3. Multiplication (num1 * num2).
# 4. Division (num1 / num2).
# 5. Modulus (num1 % num2).
# 5. Call perform_operations using num1 and num2 as arguments to display the results of the arithmetic
# operations.


import os

# Read the file
def read_file() -> int:
    # If the file exists
    if os.path.isfile("values.txt"):
        # Opens the file as read
        with open("values.txt", "r") as file:
            # Read each line
            for line in file:
                # Strip and split the line with the - to take both values
                data = line.strip().split("-")
                # print(data[0]) # Just to debug
                # Append each number into the list and making them an int 
                # by the old way (I assure myself that it was only the digit)
                num1 = int(data[0])
                num2 = int(data[1])
    
    # Return the numbers to use it later
    return num1, num2

# Function to perform the operations
def perform_operations(num1: int, num2: int) -> None:
    # 1. Addition (num1 + num2).
    print(num1 + num2)
    # 2. Subtraction (num1 - num2).
    print(num1 - num2)
    # 3. Multiplication (num1 * num2).
    print(num1 * num2)
    # 4. Division (num1 / num2).
    print(num1 / num2)
    # 5. Modulus (num1 % num2).
    print(num1 % num2)

# Run the function
num1, num2 = read_file()
perform_operations(num1, num2)
