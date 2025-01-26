"""
Solution for Task 3 of the "Mission Space Lab" project,
a project developed by the Raspberry Pi Foundation and ESA Education.
This task and solution were created by Mikkel Amstrup Brandt Neiiendam,
educator and certified ESA Education mentor.

The program must:
1. Generate random values for 1 minute.
2. Calculate the average of the generated values.
3. Upon completion, display:
   - The total number of generated values.
   - The calculated average.
4. Create a result.txt file containing the average formatted with 5 significant figures in km/s.
"""

import random
from datetime import datetime, timedelta

# List to store the generated random values
generatedValues = []

# Get the current time as the program's start time
startTime = datetime.now()

# Set the end time to 1 minute after the start time
endTime = startTime + timedelta(minutes=1)

# Inform the user that the program is running
print("The program is generating random values for 1 minute...")

# Generate random values for 1 minute
while datetime.now() < endTime:
    value = random.uniform(0, 1000)  # Generate a random value between 0 and 1000
    generatedValues.append(value)  # Add the generated value to the list
    print(f"New value generated: {value:.4f}")  # Print the value to the terminal

# Calculate the average of the generated values if any values exist
if generatedValues:
    average = sum(generatedValues) / len(generatedValues)
else:
    average = 0  # If no values were generated, set the average to 0

# Format the average to 5 significant figures
formattedAverage = f"{average:.5g}"

# Write the formatted average to a file named "result.txt"
with open("result.txt", "w") as file:
    file.write(f"{formattedAverage}")

# Display the program's results to the user
print("\nThe program has now completed.")
print(f"\nTotal values generated: {len(generatedValues)}")
print(f"\nThe calculated average is: {average:.4f} km/s")
print("\nThe result has been saved in 'result.txt' with 5 significant figures.")