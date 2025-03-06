###### Title
Create a Sequential 2D List

###### Description
Write a function called `modify_value` that takes two parameters as input. 
The first input parameter represents the number of rows of a matrix.
The second input parameter represents the number of columns of a matrix.
The function will create a 2D list with these dimensions, where each element is a unique integer starting from 0 
and increasing sequentially, row by row.
Your task is to populate the matrix with these values and return it to the calling function.

###### Input Description
The first input parameter represents the number of rows of a matrix.
The second input parameter represents the number of columns of a matrix.

###### Output Description
Returns the created matrix in the form of a 2D list.
The matrix should contain integers starting from 0, increasing by 1, row by row.

###### Input Samples
Example of input parameters: 3,  3

###### Output Samples
0 1 2
3 4 5
6 7 8


###### Input Samples
Example of input parameters: 2, 4

###### Output Samples
0 1 2 3
4 5 6 7


###### 3 Hidden Test Cases (Input/Output) for validate code
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

###### Code Template
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
matrix = modify_value(rows, cols)

for row in range(rows):
    for col in range(cols):
        if col == cols - 1:
            print(matrix[row][col])
        else:
            print(matrix[row][col], end=' ')
//APPEND END

###### Solution

# Solution to the problem
def modify_value(rows, cols):
    matrix = [[0] * cols for _ in range(rows)]
    
    # For each row in the matrix
    counter = 0
    for row in range(n):
        for col in range(m):
            matrix[row][col] = counter
            counter += 1
    
    return matrix