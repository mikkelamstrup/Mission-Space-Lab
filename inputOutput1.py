"""
Solution for Task 1 of the "Mission Space Lab" project,
a project developed by the Raspberry Pi Foundation and ESA Education.
This task and solution were created by Mikkel Amstrup Brandt Neiiendam,
educator and certified ESA Education mentor.

Task:
The student must write a program that adheres to the following requirements:
1. Allow the user to input 2 floating-point numbers.
2. Calculate the average of these numbers.
3. Display the calculated average to the user.
"""

# Prompt the user to input the first floating-point number
tal1 = float(input("Enter your first number here: "))

# Prompt the user to input the second floating-point number
tal2 = float(input("Enter your second number here: "))

# Calculate the average of the two numbers
gennemsnit = (tal1 + tal2) / 2

# Display the calculated average to the user
print(gennemsnit)