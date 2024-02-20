# Defining a function called 'pythagorean' that takes three arguments: a, b, and c
def pythagorean(a, b, c):
    # Calculating the square of 'a' and 'b' and adding them together
    value = a * a + b * b
    
    # Calculating the square of 'c'
    result = c * c
    
    # Checking if the sum of squares of 'a' and 'b' is equal to the square of 'c'
    if value == result:
        # Printing a message indicating that the numbers form a Pythagorean triple
        print("It is pythagorean triple")
    else:
        # Printing a message indicating that the numbers do not form a Pythagorean triple
        print("It is not pythagorean triple")
    
    # Returning the calculated values of 'value' and 'result'
    return value, result

# Calling the 'pythagorean' function with the arguments 3, 4, and 5 and printing the result
print(pythagorean(3, 4, 5))
