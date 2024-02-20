# Importing the matplotlib.pyplot module and aliasing it as 'plt'
import matplotlib.pyplot as plt

# Defining a function called 'plot_letter_frequency'
def plot_letter_frequency():
    # Prompting the user to enter a string and converting it to lowercase
    user_input = input("Enter a string: ").lower()
    
    # Dictionary to store the frequency of each letter
    letter_freq = {}   
    
    # Looping through each character in the user input
    for char in user_input:
        # Checking if the character is a letter
        if char.isalpha(): 
            # If the letter is already in the dictionary, increment its frequency
            if char in letter_freq:
                letter_freq[char] += 1
            # If the letter is not in the dictionary, add it with a frequency of 1
            else:
                letter_freq[char] = 1
    
    # Sorting the letter frequency dictionary by keys
    sorted_freq = sorted(letter_freq.items())
    
    # Unpacking the sorted dictionary into two lists: letters and frequencies
    letters, frequencies = zip(*sorted_freq)
    
    # Creating a bar plot of the letter frequencies
    plt.bar(letters, frequencies)
    
    # Labeling the x-axis of the plot as 'Letter'
    plt.xlabel('Letter')
    
    # Labeling the y-axis of the plot as 'Frequency'
    plt.ylabel('Frequency')
    
    # Setting the title of the plot to 'Letter Frequency Histogram'
    plt.title('Letter Frequency Histogram')
    
    # Displ
