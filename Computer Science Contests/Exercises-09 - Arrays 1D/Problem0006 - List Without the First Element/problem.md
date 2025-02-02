## Title
List Without the First Element

## Description
Write a program that prints all elements of the list except the first one.

## Input Description
The variable numbers is already initialized with a list of integers.

## Output Description
Output a list with all elements except the first.

## Input Samples
numbers = [10, 20, 30]

## Output Samples
20 30


## 3 Hidden Test Cases (Input/Output) for validate code
1 2 3
2 3

5 4 3
4 3

100
[]

## Code Template
numbers = list(map(int, input().split())) 

## Solution
print(numbers[1:])

