## Title
Find the Maximum Value in a 2D List

## Description
You are given a 2D list (matrix). Write a program to find the maximum value in the matrix.

## Input Description:
The variable matrix is already initialized with a 2D list of integers.
You need to find and print the maximum value in the matrix.

## Output Description:
Print the maximum value in the matrix.

## Input Samples:
matrix = [[1, 2, 3], [4, 5, 6], [9, 8, 7]]
You do not need to fill up this matrix, the system will do this for you.

## Output Samples
9

## 3 Hidden Test Cases (Input/Output) for validate code
2
10 20
30 40
output 
40


2
10 20
30 40
output
40

2
5 4
2 3
output
5

## Code Template
n = int(input())  # Number of rows
matrix = []

# For each row in the matrix
for i in range(n):
    row = list(map(int, input().split()))  # Read the row as space-separated integers
    matrix.append(row)  # Add the row to the matrix



## Solution

# Initialize the maximum value with the smallest possible integer
max_value = float('-inf')

# Iterate through each element in the matrix to find the maximum value
for row in matrix:
    for value in row:
        if value > max_value:
            max_value = value

# Print the maximum value found in the matrix
print(max_value)