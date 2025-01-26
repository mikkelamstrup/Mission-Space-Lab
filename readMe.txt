# Mission Space Lab - Input/Output Tasks

## Overview
This repository contains solutions to tasks for the "Mission Space Lab" project, developed by the Raspberry Pi Foundation 
and ESA Education. These tasks are designed to teach students how to work with Python programming concepts such as user input, 
file handling, random number generation, and working with time.

The tasks and solutions were created by Mikkel Amstrup Brandt Neiiendam, educator and certified ESA Education mentor.

---

## Files and Descriptions

### **1. inputOutput1.py**
**Description:**
- This program allows the user to input two floating-point numbers.
- It calculates the average of the two numbers.
- The result is displayed to the user in the terminal.

**Usage:**
1. Run the script.
2. Enter two numbers when prompted.
3. The program will display the average of the two numbers.

---

### **2. inputOutput2.py**
**Description:**
- This program extends Task 1 by saving the calculated average to a file named `result.txt`.
- The saved average is formatted to a maximum of 5 significant figures.

**Usage:**
1. Run the script.
2. Enter two numbers when prompted.
3. The program will:
   - Display the average in the terminal.
   - Save the formatted average in `result.txt`.

---

### **3. inputOutput3.py**
**Description:**
- This program generates 5 random floating-point values in the range of 0 to 1000.
- It calculates the average of the generated values.
- The random values are displayed in the terminal.
- The calculated average is saved to `result.txt`, formatted with up to 5 significant figures.

**Usage:**
1. Run the script.
2. The program will:
   - Display the 5 random values in the terminal.
   - Save the calculated average in `result.txt`.

---

### **4. inputOutput4.py**
**Description:**
- This program generates random values continuously for 1 minute.
- It calculates the average of all generated values.
- Upon completion, the program:
   - Displays the total number of generated values and the calculated average in the terminal.
   - Saves the average to `result.txt`, formatted with up to 5 significant figures.

**Usage:**
1. Run the script.
2. The program will:
   - Generate random values for 1 minute.
   - Display the total number of generated values and the average.
   - Save the average in `result.txt`.

---

## How to Run the Programs
1. Ensure Python 3.x is installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the scripts.
4. Run the desired script 

---

## Notes
- Ensure you have write permissions in the directory where you run the programs, as they generate and save `result.txt`.
- The programs are designed for educational purposes and adhere to the requirements of the "Mission Space Lab" project.