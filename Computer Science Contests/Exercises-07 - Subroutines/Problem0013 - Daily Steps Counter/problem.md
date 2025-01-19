## Title
Daily Steps Counter

## Description
Sarah is tracking her daily steps and wants to know on which day she first reaches her daily goal of 10,000 steps.

The function should not take any parameters. Instead, it should read the input from the user during execution.
The function should keep asking for the steps walked on each day, one day at a time.
The program should exit (i.e., stop asking for input) when the number of steps for a day is greater than or equal to 10,000.
Goal:
Write a function named daily_steps_counter that:

Prompts the user to enter the steps walked each day.
Stops when a value greater than or equal to 10,000 is entered.
Prints the day number when Sarah first reached her goal.

## Input Description
Each line contains an integer representing the steps walked that day.
The program should stop reading input when a value ≥ 10000 is entered.

## Output Description
The function returns the day number when Sarah first reached her goal.

## Input Samples
5000
7500
8900
10500

## Output Samples
Day 4

# Template Code 

//PREPEND BEGIN
# Import statements or constants (if needed)
//PREPEND END

//TEMPLATE BEGIN

# Function to track the daily steps and find when the goal is reached
def daily_steps_counter():
    day = 1
    
    # Keep reading steps until the goal is reached
    while True:
        # Step 1: Read the input (steps for the day)
        steps = int(input())
        
        # Step 2: If the steps are greater than or equal to 10000, print the day and exit
        if steps >= 10000:
            print(f"Day {day}")
            break
        
        # Step 3: Increment the day count for the next input
        day += 1

//TEMPLATE END

//APPEND BEGIN

# Call the function and print result
daily_steps_counter()

# Additional test cases (optional, but usually for testing purposes):
# For example:
# Simulate input and check that the function prints the expected output

//APPEND END