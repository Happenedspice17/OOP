import datetime
import math

def gregorian_to_lunar(year, month, day):
    # Convert the given date to a datetime object
    date = datetime.date(year, month, day)
    
    # Calculate the number of days since the start of the lunar calendar
    start_date = datetime.date(1900, 1, 31)
    days_since_start = (date - start_date).days
    
    # Calculate the number of lunar months since the start of the lunar calendar
    lunar_months_since_start = math.floor(days_since_start / 29.53059)
    
    # Calculate the number of days into the current lunar month
    days_into_lunar_month = days_since_start - (lunar_months_since_start * 29.53059)
    
    # Calculate the lunar day
    lunar_day = math.floor(days_into_lunar_month) + 1
    
    # Calculate the lunar month
    lunar_month = lunar_months_since_start + 1
    
    # Calculate the lunar year
    lunar_year = 1900 + math.floor(lunar_months_since_start / 12)
    
    return lunar_year, lunar_month, lunar_day

# Test the function with a sample date
year, month, day = 2024, 2, 19
lunar_year, lunar_month, lunar_day = gregorian_to_lunar(year, month, day)
print(f"The lunar date corresponding to {year}-{month}-{day} is {lunar_year}-{lunar_month}-{lunar_day}.")
