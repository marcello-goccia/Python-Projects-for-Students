## Title
Modify a Value in a 2D List

## Description
You are given a 2D list. Write a program to modify the value at a specific position in 
the 2D list. Print the updated list.

## Input Description
The variable matrix is already initialized with a 2D list of integers.
The program receives three integer inputs: the row index, the column index, and the new value. 
The program should update the element at the specified row and column in "matrix" with the new value, 
and then print the modified "matrix".

## Output Description
The program should print the modified 2D list ("matrix"), with each row printed on a separate line.

## Input Samples
1
2
10

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
You do not need to fill up this matrix, the system will do this for you.

## Output Samples
1 2 3
4 5 10
7 8 9

## 3 Hidden Test Cases (Input/Output) for validate code
3
1 2 3
4 5 6
7 8 9
1
2
10
output
1 2 3
4 5 10
7 8 9

2
10 20
30 40
0
1
100
output
10 100
30 40

2
5 6 7
8 9 10
1
0
15
output
5 6 7
15 9 10


## Code Template
n = int(input())  # Number of rows
matrix = []

# For each row in the matrix
for i in range(n):
    row = list(map(int, input().split()))  # Read the row as space-separated integers
    matrix.append(row)  # Add the row to the matrix


## Solution
# Read the row index, column index, and new value
row_index = int(input())
col_index = int(input())
new_value = int(input())

# Update the value in the matrix
matrix[row_index][col_index] = new_value

# Print the modified matrix
for row in matrix:
    print(" ".join(map(str, row)))