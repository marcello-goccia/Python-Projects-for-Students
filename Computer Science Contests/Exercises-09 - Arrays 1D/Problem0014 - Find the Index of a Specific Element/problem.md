## Title
Find the Index of a Specific Element

## Description
Write a program to find the index of a given element in the list.

## Input Description
The variable "numbers" is already initialized with a list of integers.
The integer "target" is already initialized with an integer

## Output Description
Output the index of the first occurrence of target in the list. If target is not in the list, print -1.

## Input Samples
numbers = [1, 2, 3, 4]
target = 3


## Output Samples
2

## 3 Hidden Test Cases (Input/Output) for validate code

1, 2, 3, 4
5
Output: -1

5, 10, 15 
10
Output: 1

10, 20, 30
30
Output: 2

## Code Template
numbers = list(map(int, input().split())) 
target = int(input())


## Solution
if target in numbers:
    print(numbers.index(target))
else:
    print(-1)

