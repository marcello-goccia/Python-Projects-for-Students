## Title
Transpose a Matrix

## Description
You are given a 2D list. Write a program to compute and print the transpose of the matrix.

The transpose of a matrix is a new matrix in which the rows become columns and the columns become rows.

Example:
For a matrix:

1 2 3
4 5 6

The transpose will be:

1 4
2 5
3 6

## Input Description
The variable "matrix" is already initialized with a 2D list of integers.
You need to compute the transpose of this matrix.

## Output Description
Print the transpose of the matrix. The matrix should be printed row by row.


## Input Samples
matrix = [[1, 2], [3, 4], [5, 6]]
You do not need to fill up this matrix, the system will do this for you.

## Output Samples
1 3 5
2 4 6

## 3 Hidden Test Cases (Input/Output) for validate code
3
1 2
3 4
5 6
output
1 3 5
2 4 6

2
10 20 30
40 50 60
output
10 40
20 50
30 60

2
1 2 3 4
5 6 7 8
output
1 5
2 6
3 7
4 8


## Code Template
n = int(input())  # Number of rows
matrix = []

# For each row in the matrix
for i in range(n):
    row = list(map(int, input().split()))  # Read the row as space-separated integers
    matrix.append(row)  # Add the row to the matrix


## Solution

# Step 1: Initialize an empty list to hold the transposed matrix
transpose = []

# Step 2: Loop through each column in the original matrix
for i in range(len(matrix[0])):
    # Step 3: Create a new row for the transposed matrix
    new_row = []
    
    # Step 4: Loop through each row and append the i-th element of each row to the new_row
    for j in range(len(matrix)):
        new_row.append(matrix[j][i])
    
    # Step 5: Append the new_row to the transpose list
    transpose.append(new_row)

# Step 6: Print the transposed matrix
for row in range(len(transpose)):
    for col in range(len(transpose[row])):
        if col == len(transpose[0]) - 1:
            print(transpose[row][col])
        else:
            print(transpose[row][col], end=' ')




