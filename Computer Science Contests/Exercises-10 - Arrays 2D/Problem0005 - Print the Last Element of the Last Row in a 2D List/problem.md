## Title
Print the Last Element of the Last Row in a 2D List

## Description
Write a program to print the last element of the last row in a given 2D list (matrix).

## Input Description
The variable "matrix" is already initialized with a 2D list of integers.
You need to print the last element of the last row in the matrix.

## Output Description
Print the last element of the last row.

## Input Samples
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
You do not need to fill up this matrix, the system will do this for you.

## Output Samples
9

## 3 Hidden Test Cases (Input/Output) for validate code
2
10 20
30 40
output 40

2
5 6
7 8
output 8

3
1 2 3
4 5 6
7 8 9
output 9

## Code Template
n = int(input())  # Number of rows
matrix = []

# For each row in the matrix
for i in range(n):
    row = list(map(int, input().split()))  # Read the row as space-separated integers
    matrix.append(row)  # Add the row to the matrix


## Solution
print(matrix[-1][-1])