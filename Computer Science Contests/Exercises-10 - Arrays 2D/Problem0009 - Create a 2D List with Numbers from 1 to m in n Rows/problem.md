## Title
Create a 2D List with Numbers from 1 to m in n Rows

## Description
Write a function called `create_2d_list` that takes two parameters as input. 
The first input parameter represents the number of rows of a matrix.
The second input parameter represents the number of columns of a matrix.
The function will create a 2D list with these dimensions, where each row contains numbers from 1 to the number of 
columns. Your task is to populate the matrix with these values and return it to the calling function.

## Input Description
The first input parameter represents the number of rows of a matrix.
The second input parameter represents the number of columns of a matrix.

## Output Description
Returns the created matrix in the form of a 2D list.

## Input Samples
Example of input parameters: 3, 4

## Output Samples
1 2 3 4
1 2 3 4
1 2 3 4

## 3 Hidden Test Cases (Input/Output) for validate code
Example of input parameters: 5, 1
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
//PREPEND BEGIN
# No imports needed
//PREPEND END

//TEMPLATE BEGIN

# TODO: Write your code here

//TEMPLATE END

//APPEND BEGIN
# Read input
rows = int(input())  # Number of rows
cols = int(input())  # Number of cols

# Call the function and print result
matrix = create_2d_list(rows, cols)

for row in range(rows):
    for col in range(cols):
        if col == cols - 1:
            print(matrix[row][col])
        else:
            print(matrix[row][col], end=' ')
//APPEND END

## Solution
def create_2d_list(rows, cols):
    matrix = []
    for _ in range(rows):
        row = list(range(1, cols + 1))
        matrix.append(row)
    
    for row in matrix:
        print(" ".join(map(str, row)))
    
    return matrix
