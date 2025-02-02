## Title
Find the Maximum Element

## Description
Write a program that finds the largest element in the list.

## Input Description
The variable "numbers" is already initialized with a list of integers.

## Output Description
Output a single integer: the largest element in the list.

## Input Samples
numbers = [1, 2, 3, 4]


## Output Samples
4


## 3 Hidden Test Cases (Input/Output) for validate code
5 3 8 2
8

10 20 5 50
50

100 200 300
300

## Code Template
numbers = list(map(int, input().split())) 

## Solution
print(max(numbers))
