## Title
Print Element at Given Position in a 2D List

## Description
You are given a 2D list. Write a program that takes two integers as inputs and prints the element at those
position in the matrix.

## Input Description
The variable "matrix" is already initialized with a 2D list of integers.
The program receives two integer inputs. The first input represents the row index, and the second represents the 
column index. These indices are used to access an element within 2D list "matrix".

## Output Description
The program should print the single integer value found at the specified row and column within the "matrix".

## Input Samples
1
2

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
You do not need to fill up this matrix, the system will do this for you.

## Output Samples
6

## 3 Hidden Test Cases (Input/Output) for validate code
3
1 2 3
4 5 6
7 8 9
1
2
output 6

2
10 20
30 40
0
1
output 20

2
5 6 7
8 9 10
1
0
output 8

## Code Template
n = int(input())  # Number of rows
matrix = []

# For each row in the matrix
for i in range(n):
    row = list(map(int, input().split()))  # Read the row as space-separated integers
    matrix.append(row)  # Add the row to the matrix


## Solution
i = int(input())
j = int(input())
print(matrix[i][j])