"""
Solution for Task 2 of the "Mission Space Lab" project,
a project developed by the Raspberry Pi Foundation and ESA Education.
This task and solution were created by Mikkel Amstrup Brandt Neiiendam,
educator and certified ESA Education mentor.

Task 2:
The program must now generate a “result.txt” file when it runs.
The file should save the calculated average value.
The saved value must not exceed 5 significant figures.
"""

# Prompt the user to input the first floating-point number
tal1 = float(input("Enter your first number here: "))

# Prompt the user to input the second floating-point number
tal2 = float(input("Enter your second number here: "))

# Calculate the average of the two numbers
gennemsnit = (tal1 + tal2) / 2

# Open a file called "result.txt" in write mode and save the average
# Format the average value to ensure it only contains up to 5 significant figures
with open("result.txt", "w") as file:
    file.write(f"{gennemsnit:.5g}")

# Inform the user that the file has been created and contains the average value
print("The file 'result.txt' has been generated.\nHere you can see the average value.")