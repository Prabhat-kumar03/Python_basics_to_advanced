from datetime import datetime
from time import strptime

def calculate_age(birthdate_str):
    """
    Calculate age based on the provided birthdate string in 'YYYY-MM-DD' format.

    Args:
        birthdate_str (str): The birthdate as a string in 'YYYY-MM-DD' format.

    Returns:
        int: The calculated age.
    """
    # Parse the birthdate string into a datetime object
    birthdate = strptime(birthdate_str, '%Y-%m-%d')
    
    # Get the current date
    today = datetime.now()
    
    # Calculate age
    age = today.year - birthdate.tm_year   
    # Adjust age if the birthday hasn't occurred yet this year
    if (today.month, today.day) < (birthdate.tm_mon, birthdate.tm_mday):
        age -= 1
    
    return age

if __name__ == "__main__":
    birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
    age = calculate_age(birthdate_input)
    print(f"You are {age} years old.")