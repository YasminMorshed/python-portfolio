# We use the datetime module for manipulating date and time

from datetime import datetime, date

# We ask user to input their date of birth

print("Your date of birth (dd mm yyyy)")

# strptime creates datetime object from the string, the arrow makes inputting easier 

date_of_birth = datetime.strptime(input("--->"), "%d %m %Y")

# We are defining a function to return the age of the person based on today's date and their date of birth

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

# Finally, we calculate the age by inputting the person's date of birth into the function

age = calculate_age(date_of_birth)

# We print the age for the user

print(age)