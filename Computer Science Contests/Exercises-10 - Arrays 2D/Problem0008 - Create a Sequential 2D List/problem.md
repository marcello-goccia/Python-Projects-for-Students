## Title
Create a Sequential 2D List

## Description
You are given two integers, representing the number of rows and columns of a matrix. 
Create a 2D list with these dimensions, where each element is a unique integer starting from 0 and increasing 
sequentially, row by row.
Your task is to populate the matrix with these values and print it.

## Input Description
The first line contains an integer (number of rows).
The second line contains an integer (number of columns).

## Output Description
Print the created matrix in the form of a 2D list, where each row is printed on a new line. 
The matrix should contain integers starting from 0, increasing by 1, row by row.

## Input Samples
3
3

## Output Samples
0 1 2
3 4 5
6 7 8


## Input Samples
2
4

## Output Samples
0 1 2 3
4 5 6 7


## 3 Hidden Test Cases (Input/Output) for validate code
5
1
Output
0
1
2
3
4


1
5
Output
0 1 2 3 4

4
4
Output
0 1 2 3
4 5 6 7
8 9 10 11
12 13 14 15

## Code Template
---------

## Solution

n = int(input())  # Number of rows
m = int(input())  # Number of columns

# Solution to the problem
matrix = [[0] * m for _ in range(n)]

# For each row in the matrix
counter = 0
for row in range(n):
    for col in range(m):
        matrix[row][col] = counter
        counter += 1

# Print the matrix
print(matrix)