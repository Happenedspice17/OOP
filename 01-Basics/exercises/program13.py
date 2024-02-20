# Defining a function called 'bmi'
def bmi():
    # Prompting the user to enter their height in meters and converting it to a float
    height = float(input("Enter your height in meters: "))
    
    # Prompting the user to enter their weight in kilograms and converting it to a float
    weight = float(input("Enter your weight in kg: "))

    # Calculating the BMI using the formula: weight / (height * height)
    bmi_val = weight / (height * height)
    
    # Printing the calculated BMI
    print(bmi_val)

# Calling the 'bmi' function
bmi()
