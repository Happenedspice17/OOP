# Importing required libraries
import numpy as np
import matplotlib.pyplot as plt

# Defining a function called 'plotter'
def plotter():
    # Creating x axis with range and y axis 
    # Function for Plotting Sine and Cosine Graph
    # Creating an array of x values from -π to π with a step of 0.1
    x = np.arange(-np.pi, np.pi, 0.1)
    
    # Calculating the y values for the sine and cosine functions
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    # Setting the title of the plot to "Sin and Cos wave"
    plt.title(f"Sin and Cos wave")
    
    # Adding a grid to the plot
    plt.grid()
    
    # Labeling the x-axis of the plot as 'X'
    plt.xlabel("X")
    
    # Labeling the y-axis of the plot as 'Y'
    plt.ylabel("Y")
    
    # Plotting the sine graph with green color
    plt.plot(x, y1, color='green')
    
    # Plotting the cosine graph with dark blue color
    plt.plot(x, y2, color='darkblue')
    
    # Displaying the plot
    plt.show()

# Calling the 'plotter' function
plotter()
