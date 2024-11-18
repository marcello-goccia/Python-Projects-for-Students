## Title
Triangle Pattern

## Description
Write a program that takes a number n as input and prints a right-aligned triangle pattern with n rows. Each row contains stars (*), starting with 1 star in the first row and increasing by 1 star in each subsequent row.

## Input Description
A single positive integer, greater than 1.

## Output Description
A triangle pattern of stars with n rows.

## Input Samples
5

## Output Samples
    *
   **
  ***
 ****
*****


## Solution

# Input: Number of rows
n = int(input("Enter the number of rows: "))

# Loop to generate each row
for i in range(1, n + 1):
    # Print spaces (n - i) followed by stars (i)
    print(' ' * (n - i) + '*' * i)

