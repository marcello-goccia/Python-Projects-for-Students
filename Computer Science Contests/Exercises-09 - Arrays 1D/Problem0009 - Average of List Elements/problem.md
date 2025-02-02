## Title
Average of List Elements

## Description
Write a program to calculate and print the average of the list elements as a whole number

## Input Description
The variable "numbers" is already initialized with a list of integers.

## Output Description
Output a float: the average of the elements in the list as a whole number

## Input Samples
numbers = [1, 5, 6, 7, 4]

## Output Samples
4

## 3 Hidden Test Cases (Input/Output) for validate code
1 1 1
1

2 4 6
4

10 20 30
20


## Code Template
numbers = list(map(int, input().split())) 

## Solution
average = sum(numbers) / len(numbers)
print(average)
