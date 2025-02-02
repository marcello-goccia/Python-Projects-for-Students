## Title
Count Occurrences of an Element

## Description
You are given a list of integers. Write a program to count how many times a specific number appears in the list.

## Input Description
The variable "numbers" is already initialized with a list of integers.
The integer "target" is already initialized with an integer

## Output Description
Output a single integer: the count of the target in the list.

## Input Samples
numbers = [1, 2, 2, 3, 4]
target = 2

## Output Samples
2

## 3 Hidden Test Cases (Input/Output) for validate code
5, 5, 5, 5
5
Output: 4

0, 1, 2, 3
4
Output: 0

10, 10, 10
5
Output: 0


## Code Template
numbers = list(map(int, input().split())) 
target = int(input())


## Solution
print(numbers.count(target))

