## Title
Sum of Elements in List

## Description
You are given a list of integers. Write a program to calculate and print the sum of all elements in the list.

## Input Description
The variable "numbers" is already initialized with a list of integers.

## Output Description
Output a single integer: the sum of all elements in the list.

## Input Samples
numbers = [1, 2, 3, 4]

## Output Samples
10

## 3 Hidden Test Cases (Input/Output) for validate code
5, 10, 15
30

[]
0

10, -10, 5
5

## Code Template
numbers = list(map(int, input().split())) 

## Solution
print(sum(numbers))

