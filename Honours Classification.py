def honours_classification(mark):
    """This function returns the honours classification
    of the weighted average mark entered"""
    if(mark>=70):
        honours="First Class."
    elif(mark>=60):
        honours="Upper Second."
    elif(mark>=50):
        honours="Lower Second."
    elif(mark>=40):
        honours="Third class."
    elif(mark>=35):
        honours="Pass degree."
    elif(0<mark<35):
        honours="Failed."
    else:
        print("Mark must be between 0 and 100")
    return honours

def congratulatory_message(mark):
    """This function returns the congratulatory message
    of the weighted average mark entered"""
    if(mark>=70):
        message="Excellent, well done!"
    elif(mark>=60):
        message="Very good, well done!"
    elif(mark>=50):
        message="Good, well done!"
    elif(mark>=40):
        message="Could have done better!"
    elif(mark>=35):
        message="Work harder next time!"
    else:
        message="Oh dear, try again!"
    return message

# User inputs first and last name and mark.
first_name=input("Please enter first name: ")
last_name=input("Please enter last name: ")
mark=int(input("Please enter weighted mark: "))

# If mark is less than 0 or more than 100, they must enter it again.
while mark<0 or mark>100:
    mark=int(input("Please enter weighted mark between 0-100: "))

# If mark is within range, print message.
else:
    honours = honours_classification(mark)
    message = congratulatory_message(mark)
    print(first_name, last_name, "you got", honours, message)