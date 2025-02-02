## Title


## Description


## Input Description


## Output Description


## Input Samples

You do not need to fill up this matrix, the system will do this for you.


## Output Samples


## 3 Hidden Test Cases (Input/Output) for validate code


## Code Template
n = int(input())  # Number of rows
matrix = []

# For each row in the matrix
for i in range(n):
    row = list(map(int, input().split()))  # Read the row as space-separated integers
    matrix.append(row)  # Add the row to the matrix


## Solution
