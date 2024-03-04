# 2-14BHAND

# 2-19
# This program demonstates string concatenation.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Combine the names with a space between them.
full_name = first_name + " " + last_name

# Display the users full name.
print("Your full name is " + full_name)

# 2-20
# This program demonstrates how a floating point
# number is displaying with no formatting.
from calendar import month


amount_due = 5000.0
monthly_payment = amount_due / 12.0
print(f"The monthly payment is {monthly_payment}.")

# 2-20-1
# This program demosntrates how a floating point
# number can be rounded.
amount_due = 5000.0
monthly_payment = amount_due / 12.0
print(f"The monthly payment is {monthly_payment:.2f}.")


# 2-22
# This program demonstrates how a flaoting-point
# number can be dispalyed as currency
monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print(f"Your annual pay is ${annual_pay:,.2f}")


# 2-23
# This program displays the following numbers
# in two colums
num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999

# Each number is displayed in a feild of 10 spaces
# and rounded to 2 decimal places
print(f"{num1:10.2f}{num2:10.2f}")
print(f"{num3:10.2f}{num4:10.2f}")
print(f"{num5:10.2f}{num6:10.2f}")


# 2-24
# This program demonstrates how to center align strings
name1 = "Gordon"
name2 = "Smith"
name3 = "Washington"
name4 = "Alvarado"
name5 = "Livingston"
name6 = "Jones"

# Display the names.
print(f"***{name1:^20}***")
print(f"***{name2:^20}***")
print(f"***{name3:^20}***")
print(f"***{name4:^20}***")
print(f"***{name5:^20}***")
print(f"***{name6:^20}***")
