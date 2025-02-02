###### Title
Check if a 2D List is Empty

###### Description
Write a function called 'is_list_empty' that takes a 2D list as input parameter and
returns True if the 2D list is empty, otherwise returns False.

A 2d list is empty if it contains no rows or if all rows are empty.

###### Input Description
The input 2D list is already initialized with integers.

You need to check if the 2D list is empty and returns True if it is empty, 
otherwise returns False (boolean values).

###### Output Description
Returns True if the matrix is empty, otherwise print False. Boolean values.

###### Input Samples
The functions take a 2D list as input parameter.
matrix = [[], []]

The functions take a 2D list as input parameter.
matrix = [[10, 20], [30, 40]]

###### Output Samples
True

False

###### 3 Hidden Test Cases (Input/Output) for validate code

1. Test Case 1:
   - **Input**: `matrix = [[], []]`
   - **Output**: `True`

2. Test Case 2:
   - **Input**: `matrix = [[10, 20], [30, 40]]`
   - **Output**: `False`

3. Test Case 3:
   - **Input**: `matrix = [[3, 5], [1, 2], [4, 7]]`
   - **Output**: `False`

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

# Call the function and print result
print(is_list_empty(matrix))


###### Solution

# Check if the matrix is empty
def is_list_empty(matrix):
    return all(len(row) == 0 for row in matrix) or len(matrix) == 0