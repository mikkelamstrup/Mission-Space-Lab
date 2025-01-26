"""
Solution for Task 3 of the "Mission Space Lab" project,
a project developed by the Raspberry Pi Foundation and ESA Education.
This task and solution were created by Mikkel Amstrup Brandt Neiiendam,
educator and certified ESA Education mentor.

Task 3:
The program must automatically generate 5 random values.
The values must be within the range of 0 to 1000.
The generated values should be displayed in the terminal.
The average of the values must be saved in result.txt.
"""

import random

# Generate a list of 5 random floating-point values between 0 and 1000
randomValues = [random.uniform(0, 1000) for _ in range(5)]

# Print each randomly generated value to the terminal
print("Random values generated:")
for i, value in enumerate(randomValues, start=1):
    print(f"Value {i}: {value:.4f}")  # Display each value with 4 decimal places

# Calculate the average of the random values
gennemsnit = sum(randomValues) / len(randomValues)

# Open a file named "result.txt" in write mode and save the average
# Format the average to ensure it is stored with up to 5 significant figures
with open("result.txt", "w") as file:
    file.write(f"{gennemsnit:.5g}")

# Inform the user that the file has been created and contains the average
print("The file 'result.txt' has been generated.\nHere you can see the average value.")