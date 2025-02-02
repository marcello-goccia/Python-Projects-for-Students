## Title
Sum of All Elements in a 2D List 

## Description
You are given a 2D list (matrix). Write a program to calculate the sum of all the elements in the matrix.

## Input Description
The variable matrix is already initialized with a 2D list of integers.
You need to calculate and print the sum of all the elements in the matrix.


## Output Description
Print the sum of all the integers in the matrix.

## Input Samples
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
You do not need to fill up this matrix, the system will do this for you.

## Output Samples
45

## 3 Hidden Test Cases (Input/Output) for validate code
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

## Code Template
for i in range(n):
    row = list(map(int, input().split()))  # Read the row as space-separated integers
    matrix.append(row)  # Add the row to the matrix

## Solution
for row in matrix:
    for element in row:
        print(element)

## Solution

# Initialize the sum variable
total_sum = 0

# Iterate through each row in the matrix
for row in matrix:
    # Iterate through each element in the row
    for element in row:
        # Add the element to the total sum
        total_sum += element

# Print the total sum
print(total_sum)