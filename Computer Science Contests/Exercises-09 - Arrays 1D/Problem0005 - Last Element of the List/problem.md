## Title
Last Element of the List

## Description
You are given a list of integers. Write a program to print the last element of the list.

## Input Description
The variable "numbers" is already initialized with a list of integers.

## Output Description
Output the last element in the list.

## Input Samples
numbers = [10, 20, 30]

## Output Samples
30

## 3 Hidden Test Cases (Input/Output) for validate code
1 2 3 
3

5 4 3 
3

100
100

## Code Template
numbers = list(map(int, input().split())) 

## Solution
print(numbers[-1])
