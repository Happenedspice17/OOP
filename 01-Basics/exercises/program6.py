# Defining a function called 'gcd' that takes two integers 'a' and 'b' as arguments
def gcd(a, b):
    # Looping until 'b' becomes 0
    while b:
        # Swapping the values of 'a' and 'b' and calculating the remainder
        a, b = b, a % b
    
    # Returning the final value of 'a', which is the greatest common divisor
    return a

# Calling the 'gcd' function with the arguments 48 and 18
print(gcd(48, 18)) # Output: 6
