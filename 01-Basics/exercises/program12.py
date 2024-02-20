# Defining a function called 'print_multiplication_table' that takes an integer 'N' as an argument
def print_multiplication_table(N):
    # Looping through the numbers from 1 to N
    for i in range(1, N + 1):
        # Looping through the numbers from 1 to N again
        for j in range(1, N + 1):
            # Printing the multiplication of 'i' and 'j' in the format "i * j = result"
            print(f"{i} * {j} = {i * j}")
        
        # Printing a newline after each row of the table
        print()

try:
    # Prompting the user to enter a number 'N' and converting it to an integer
    N = int(input("Enter a number (N) to print the multiplication table: "))
    
    # Calling the 'print_multiplication_table' function with the input 'N'
    print_multiplication_table(N)
    
# Handling the case where the user enters a non-integer value for 'N'
except ValueError:
    # Printing an error message
    print("Please enter a valid integer.")
