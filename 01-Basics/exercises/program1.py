# Importing the matplotlib.pyplot module and aliasing it as 'plt'
import matplotlib.pyplot as plt

# Creating two empty lists to store x and y values
x = []
y = []

# Defining a function called 'plotter' that takes two arguments: x and y
def plotter(x, y):
    # Printing a message to the console
    print("Program to display a linear graph, input the following values") 

    # Prompting the user to input the value for 'c' and converting it to an integer
    c = int(input("Input the value for c: "))
    
    # Prompting the user to input the value for 'm' and converting it to an integer
    m = int(input("Input the value for m: "))
    
    # Looping from 1 to 9 (inclusive) with a step of 1
    for i in range (1, 10, 1):
        # Calculating the value of 'y' for each 'x' using the linear equation y = mx + c
        value = m*i+c
        
        # Appending the current 'x' value to the 'x' list
        x.append(i)
        
        # Appending the current 'y' value to the 'y' list
        y.append(value)

    # Setting the title of the plot to the linear equation y = mx + c
    plt.title(f"Y = {m}x + {c}")
    
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
