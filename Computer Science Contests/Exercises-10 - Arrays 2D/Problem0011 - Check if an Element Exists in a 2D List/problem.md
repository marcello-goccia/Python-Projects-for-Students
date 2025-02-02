## Title
Check if an Element Exists in a 2D List

## Description
Write a program that checks if a given element exists in a 2D list.
Print True if the element exists, otherwise print False (boolean values).

## Input Description
The variable "matrix" is already initialized with a 2D list of integers.
You also need to take an integer as input and check if that integer exists in the matrix.

## Output Description
Print True if the element exists in the matrix, otherwise print False (boolean values).

## Input Samples
5

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
You do not need to fill up this matrix, the system will do this for you.

## Output Samples
True

## 3 Hidden Test Cases (Input/Output) for validate code
2
10 20
30 40
25
output
False

2
1 2
3 4
3
output
True

1
100
100
output
True

## Code Template
n = int(input())  # Number of rows
matrix = []

# For each row in the matrix
for i in range(n):
    row = list(map(int, input().split()))  # Read the row as space-separated integers
    matrix.append(row)  # Add the row to the matrix


## Solution

exists = False

# Iterate through each row in the matrix
for row in matrix:
    # Iterate through each element in the row
    for element in row:
        # Check if the current element matches the element to check
        if element == element_to_check:
            exists = True
            break
    if exists:
        break

# Print the result
print(exists)