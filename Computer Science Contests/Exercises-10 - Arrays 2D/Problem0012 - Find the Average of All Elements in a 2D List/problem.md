## Title
Find the Average of All Elements in a 2D List 

## Description
You are given a 2D list. Write a program to calculate the average of all elements in the matrix.

## Input Description
The variable "matrix" is already initialized with a 2D list of integers.
You need to calculate the average of all the elements in the matrix as an integer value and print it.

## Output Description
Print the average of all the elements in the matrix.

## Input Samples
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
You do not need to fill up this matrix, the system will do this for you.


## Output Samples
5

## 3 Hidden Test Cases (Input/Output) for validate code
2
10, 20
30, 40
output
25

2
1, 1
1, 1
output
1

2
5, 6, 7
8, 9, 10
output
7


## Code Template
n = int(input())  # Number of rows
matrix = []

# For each row in the matrix
for i in range(n):
    row = list(map(int, input().split()))  # Read the row as space-separated integers
    matrix.append(row)  # Add the row to the matrix



## Solution
total_sum = 0
total_count = 0

for row in matrix:
    total_sum += sum(row)
    total_count += len(row)

average = total_sum // total_count
print(int(average))