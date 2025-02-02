## Title
Create a 2D List with Numbers from 1 to m in n Rows

## Description
You are given two integers, representing the number of rows and columns of a matrix. 
Create a 2D list with these dimensions, where each row contains numbers from 1 to the number of columns.
Your task is to populate the matrix with these values and print it.

## Input Description
You are given two integers representing the number of rows and columns of a matrix.
You need to create a 2D list where each row contains numbers from 1 to the number of columns.

## Output Description
Print the created matrix in the form of a 2D list, where each row is printed on a new line.

## Input Samples
3
4

## Output Samples
1 2 3 4
1 2 3 4
1 2 3 4

## 3 Hidden Test Cases (Input/Output) for validate code
5
1
output
1
1
1
1
1


2
3
output
1 2 3
1 2 3

4
2
output
1 2
1 2
1 2
1 2



## Code Template
--------

## Solution

matrix = []
for _ in range(rows):
    row = list(range(1, cols + 1))
    matrix.append(row)

for row in matrix:
    print(" ".join(map(str, row)))