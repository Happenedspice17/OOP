#Script 1 (25 pts)
# 1. Read the contents of the text file named menu.txt. This file contains the menu items that you will
# process.
# 2. Store the contents of the file in a variable. Ensure that the entire content is captured in this variable as a
# single string or a list of strings, depending on how you choose to read the file.
# 3. Define a function named print_menu that accepts one argument. This argument will be the variable
# where you stored the file's contents.
# 4. Inside the print_menu function, write code that prints the contents of the menu to the console.
# 5. Call the print_menu function to display the menu.

# Import the os to find a file
import os

# Make the variable of the complete file within a list
complete_file = []
# If the file exists
if os.path.isfile("menu.txt"):
    # Opens the file as read
    with open("menu.txt", "r") as file:
        # Read each line
        for line in file:
            # Strip and split the line with the return \n
            data = line.strip().split("\n")
            # print(data[0]) Just to debug
            # Append each piece of data into the list
            complete_file.append(data[0])


# Function to print the menu
def print_menu(complete_file: list) -> None:
    # A for loop to iterate within the array and print each value
    for value in complete_file:
        print(value)

# Run the function
print_menu(complete_file)