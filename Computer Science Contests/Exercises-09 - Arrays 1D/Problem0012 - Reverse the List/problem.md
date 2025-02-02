## Title
Reverse the List

## Description
Write a program that takes a list of integers and reverses the order of the elements in the list.

## Input Description
The variable "numbers" is already initialized with a list of integers.

## Output Description
Output the reversed list.


## Input Samples
numbers = [1, 2, 3, 4]


## Output Samples
4 3 2 1


## 3 Hidden Test Cases (Input/Output) for validate code
1 2 3
3 2 1

5 4 3 2 1
1 2 3 4 5

0
0

## Code Template
numbers = list(map(int, input().split())) 

## Solution
print(numbers[::-1])

