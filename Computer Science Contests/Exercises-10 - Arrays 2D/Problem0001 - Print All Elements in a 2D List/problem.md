## Title
Print All Elements in a 2D List

## Description
You are given a 2D list. Write a program to print all the elements in the matrix, one by one.

## Input Description
The variable "matrix" is already initialized with a 2D list of integers.
You need to print all the elements of the matrix row by row.

## Output Description
Print all the elements of the matrix, each on a new line.

## Input Samples
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  
You do not need to fill up this matrix, the system will do this for you.

## Output Samples
1
2
3
4
5
6
7
8
9

## 3 Hidden Test Cases (Input/Output) for validate code
matrix = [[10, 20], [30, 40]]
10
20
30
40

matrix = [[5, 6, 7]]
5
6
7

matrix = [[10, 20], [30, 40], [50, 70]]
10
20
30
40
50
70


## Code Template
n = int(input())  # Number of rows
matrix = []

# For each row in the matrix
for i in range(n):
    row = list(map(int, input().split()))  # Read the row as space-separated integers
    matrix.append(row)  # Add the row to the matrix

## Solution
for row in matrix:
    for element in row:
        print(element)