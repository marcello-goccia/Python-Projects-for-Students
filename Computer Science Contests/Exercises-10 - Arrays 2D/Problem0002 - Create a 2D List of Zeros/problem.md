## Title
Create a 2D List of Zeros

## Description
Write a program that creates a 2D list with n rows and m columns, filled with zeros.

## Input Description
You are given two integers: the first representing the number of rows and the second representing the number of columns.
You need to create a 2D list with the specified number of rows and columns, where all elements are initialized to zero.

## Output Description
Print the created 2D list row by row, see output sample.

## Input Samples
2
3

## Output Samples
0 0 0
0 0 0

## 3 Hidden Test Cases (Input/Output) for validate code
3
2
OUTPUT:
0 0
0 0
0 0

1
4
OUTPUT:
0 0 0 0

1
1
OUTPUT:
0

## Code Template
-------

## Solution
matrix = [[0] * m for _ in range(n)]

# Print the matrix row by row
for row in matrix:
    print(" ".join(map(str, row)))