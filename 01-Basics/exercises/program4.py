# Importing the matplotlib.pyplot module and aliasing it as 'plt'
import matplotlib.pyplot as plt

# Defining a function called 'collatz_conjecture' that takes an integer 'n' as an argument
def collatz_conjecture(n):
    # List to store the sequence
    sequence = [n]
    
    # Looping until 'n' becomes 1
    while n != 1:
        # If 'n' is even, divide it by 2
        if n % 2 == 0:
            n = n // 2
        # If 'n' is odd, multiply it by 3 and add 1
        else:
            n = 3 * n + 1
        
        # Append the new value of 'n' to the sequence list
        sequence.append(n)
    
    # Return the sequence list
    return sequence

# Defining a function called 'plot_collatz_sequence' that takes a list 'sequence' as an argument
def plot_collatz_sequence(sequence):
    # Plot the sequence
    plt.title('Collatz Conjecture Sequence')
    plt.xlabel('Step')
    plt.ylabel('Value')
    plt.grid(True)
    plt.plot(sequence)
    plt.show()

# Prompting the user to enter a number to apply the Collatz conjecture
n = int(input("Enter a number to apply Collatz conjecture: "))

# Applying the Collatz conjecture to the input number
sequence = collatz_conjecture(n)

# Plotting the Collatz conjecture sequence
plot_collatz_sequence(sequence)
