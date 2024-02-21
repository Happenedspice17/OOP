#Program 1 (25 pts)
# Number Guessing Game: Implement a number guessing game where the computer randomly selects a
# number between 1-100, and the user has to guess it, receiving hints on whether the guess is too high or too low

# Import the random library
import random

# Initialize the number of random between 1 - 100
number = random.randint(1, 100)

# The main function with the number to guess as argument
def main(number_to_guess):
    # Input the number of the user and save it in the guess variable
    guess = int(input("Enter the number you think the computer chose: "))
    # A print to test
    # print(number_to_guess)
    # The main condition of the game, if the guess is less than the random number, show the hint
    # and re-run the main program with the same number to guess
    if guess > number_to_guess:
        # Print the hint
        print("The number you choosed is greater than the chosen by the computer, try again")
        # Re-run the program
        main(number_to_guess)
    # An else if to show if the hint that the number is less 
    elif guess < number_to_guess:
        # The print of the hint
        print("The number you choosed is less than the chosen by the computer, try again")
        # Re-run the program
        main(number_to_guess)
    # The final else that runs when the user wins
    else:
        # Print and finish the program
        print("Nice, you won!")
    

# Run the main program
main(number)