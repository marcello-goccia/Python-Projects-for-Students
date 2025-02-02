###### Title
Modify a Value in a 2D List

###### Description
Write a function called `modify_value` that takes four parameters as input. 
The first parameter is a 2D list, the second parameter is the row index, 
the third parameter is the column index, and the fourth parameter is the new value. 
The function will modify the value at the specified row and column indices. 
The function returns the updated list.

###### Input Description
The first parameter is a 2D list, the second parameter is the row index, 
the third parameter is the column index, and the fourth parameter is the new value. 
The function will modify the value at the specified row and column indices. 
The function returns the updated list.

###### Output Description
The program will return the modified 2D list.

###### Input Samples
Example of input parameters
[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 2, 10

###### Output Samples
1 2 3
4 5 10
7 8 9

###### 3 Hidden Test Cases (Input/Output) for validate code
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


###### Code Template
//PREPEND BEGIN
# No imports needed
//PREPEND END

//TEMPLATE BEGIN

# TODO: Write your code here

//TEMPLATE END

//APPEND BEGIN
# Read input
n = int(input())  # Number of rows
matrix = []

# For each row in the matrix
for i in range(n):
    row = list(map(int, input().split()))  # Read the row as space-separated integers
    matrix.append(row)  # Add the row to the matrix

i = int(input())  # index row
j = int(input())  # index column
new_value = int(input()) # element to chance

# Call the function and print result
matrix = modify_value(matrix, i, j, new_value)

for row in range(n):
    for col in range(m):
        if col == m - 1:
            print(matrix[row][col])
        else:
            print(matrix[row][col], end=' ')


###### Solution
# Read the row index, column index, and new value
def modify_value(matrix, row_index, col_index, new_value):
    # Update the value in the matrix
    matrix[row_index][col_index] = new_value
    return matrix
