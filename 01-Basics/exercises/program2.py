# Importing the matplotlib.pyplot module and aliasing it as 'plt'
import matplotlib.pyplot as plt

# Importing the math module
import math

# Creating two empty lists to store x and y values
x = []
y = []

# Printing a message to the console
print("Printing exponential growth") 

# Defining a function called 'plotter' that takes two arguments: x and y
def plotter(x, y):
    # Looping from -1 to 7 (inclusive) with a step of 1
    for i in range(-1, 8, 1):
        # Calculating the value of 'y' for each 'x' using the exponential function e^x
        value = math.exp(i)
        
        # Appending the current 'x' value to the 'x' list
        x.append(i)
        
        # Appending the current 'y' value to the 'y' list
        y.append(value)

    # Setting the title of the plot to "Exponential growth e^x"
    plt.title(f"Exponential growth e^x")
    
    # Adding a grid to the plot
    plt.grid()
    
    # Labeling the x-axis of the plot as 'X'
    plt.xlabel("X")
    
    # Labeling the y-axis of the plot as 'Y'
    plt.ylabel("Y")
    
    # Plotting the x and y values on the graph
    plt.plot(x, y)
    
    # Displaying the plot
    plt.show()

# Calling the 'plotter' function with the 'x' and 'y' lists as arguments
plotter(x, y)
