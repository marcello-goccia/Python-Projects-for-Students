## Title
Check if a 2D List is Empty

## Description
Write a program to check if a given 2D list is empty. 
A matrix is empty if it contains no rows or if all rows are empty.

## Input Description
The variable "matrix" is already initialized with a 2D list of integers.
You need to check if the matrix is empty and print True (boolean value) if it is empty, 
otherwise print False (boolean value).

## Output Description
Print True if the matrix is empty, otherwise print False. Boolean values.

## Input Samples
matrix = [[], []]
matrix = [[10, 20], [30, 40]]

## Output Samples
True
False

## 3 Hidden Test Cases (Input/Output) for validate code


## Code Template
n = int(input())  # Number of rows
matrix = []

# For each row in the matrix
for i in range(n):
    row = list(map(int, input().split()))  # Read the row as space-separated integers
    matrix.append(row)  # Add the row to the matrix


## Solution
