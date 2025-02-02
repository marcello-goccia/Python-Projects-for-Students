## Title
Print the First Element of a 2D List

## Description
You are given a 2D list. Write a program to print the first element of the first row in the matrix.

## Input Description
The variable "matrix" is already initialized with a 2D list of integers.
You need to print the first element of the first row.

## Output Description
Print the first element of the first row.

## Input Samples
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  
You do not need to fill up this matrix, the system will do this for you.

## Output Samples
1

## 3 Hidden Test Cases (Input/Output) for validate code
2
10 20
30 40
OUTPUT 10

3
1 2 3
4 5 6
7 8 9
OUTPUT 1

2
5 6 7
8 9 10
OUTPUT 5

## Code Template
n = int(input())  # Number of rows
matrix = []

# For each row in the matrix
for i in range(n):
    row = list(map(int, input().split()))  # Read the row as space-separated integers
    matrix.append(row)  # Add the row to the matrix


## Solution
print(matrix[0][0])