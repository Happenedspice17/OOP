# Defining a function called 'savings_goal' that takes three arguments: starting amount, goal amount, and monthly savings
def savings_goal(starting, goal, monthly_savings) -> float:
    # Initializing variables to store the current savings and the number of months
    savings, n = 0, 0
    
    # Looping until the savings reach or exceed the goal
    while savings < goal:
        # Calculating the savings for the current month
        savings = monthly_savings * (1 + n) + starting
        
        # Incrementing the number of months
        n += 1
    
    # Returning the total number of months needed to reach the goal
    return n+1

# Calling the 'savings_goal' function with the given values and printing the result
print(f"It would take you {savings_goal(4000, 30000, 2000)} months to reach that value")
