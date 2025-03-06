## Title
Create a 2D List of Zeros

## Description
Write a function called 'create_2d_list_zeros' that creates and returns a 2D list with n rows and m columns, 
filled with zeros.

## Input Description
The functions takes two integers as input parameters: the first representing the number of rows and 
the second representing the number of columns.
You need to create a 2D list with the specified number of rows and columns, where all elements are initialized to zero.

## Output Description
Return the created 2D list

## Input Samples
Two parameters, example: 2 3

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
//PREPEND BEGIN
# No imports needed
//PREPEND END

//TEMPLATE BEGIN

# TODO: Write your code here

//TEMPLATE END

//APPEND BEGIN
# Read input
n = int(input())  # Number of rows
m = int(input())  # Number of columns

# Call the function and print result
matrix = create_2d_list_zeros(n, m)

for row in range(n):
    for col in range(m):
        if col == m - 1:
            print(matrix[row][col])
        else:
            print(matrix[row][col], end=' ')
//APPEND END

## Solution
def create_2d_list_zeros(n, m):
    return [[0] * m for _ in range(n)]
