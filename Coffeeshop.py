#Code to determine discount in coffeeshop

# Print statement and ask person to input their status.
print("Welcome to the coffee shop! Please choose your status from the following options:")
print("1: Staff")
print("2: Student")
print("3: None")
status = int(input("Please enter a number: "))

#if statement staff customer
if status == 1:
    status = "Staff"
    print("Welcome staff-member. What is the cost of the item?")
    cost_staff = float(input("Please enter the cost of the item: £"))
    print("The amount payable today is £" + "%.2f" % cost_staff)

#elif customer student
elif status == 2:
    status = "Student"
    print("Welcome student. You qualify for a 10% discount. Please enter the cost of the item.")
    cost_student = float(input("Please enter the cost of the item: £"))
    cost_student_discount = cost_student * 0.90
    print("The amount payable today is £" + "%.2f" % cost_student_discount)

#else customer not student or staff
else:
    print("Unfortunately, your status is unknown and you do not qualify for a discount.")
    print("What is the cost of the item?")
    cost_customer = float(input("Please enter the cost of the item: £"))
    print("The amount payable today is £" + "%.2f" % cost_customer)
    