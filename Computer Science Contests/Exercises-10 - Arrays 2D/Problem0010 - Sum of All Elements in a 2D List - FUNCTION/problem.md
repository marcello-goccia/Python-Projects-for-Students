###### Title
Sum of All Elements in a 2D List 

###### Description
Write a function called 'sum_elements_in_list' that takes a 2D list as input parameter and
returns the sum of all the elements in the matrix.

###### Input Description
The input 2D list is already initialized with integers.

###### Output Description
Returns the sum of all the integers in the matrix.

###### Input Samples
The functions take a 2D list as input parameter.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

###### Output Samples
It will return the value 45

###### 3 Hidden Test Cases (Input/Output) for validate code
2
10 20
30 40
output
100

2
1 1
1 1
output
4

2
5 6 7
8 9 10
output
45

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
print(sum_elements_in_list(matrix))

# for row in range(n):
#     for col in range(m):
#         if col == m - 1:
#             print(matrix[row][col])
#         else:
#             print(matrix[row][col], end=' ')
//APPEND END


###### Solution
def sum_elements_in_list(matrix):
    total_sum = 0
    for row in matrix:
        # Iterate through each element in the row
        for element in row:
            # Add the element to the total sum
            total_sum += element
    return total_sum