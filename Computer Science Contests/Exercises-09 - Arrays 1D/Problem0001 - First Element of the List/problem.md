## Title
First Element of the List

## Description:
You are given a list of integers. Write a program to print the first element of the list.

## Input Description:
The variable "numbers" is already initialized with a list of integers.

## Output Description:
Output the first element in the list.

## Input Samples
numbers = [10, 20, 30]

## Output Samples
10

## 3 Hidden Test Cases (Input/Output) for validate code
1 2 3
1

5 4 3
5

100
100

## Code Template

numbers = list(map(int, input().split())) 

## Solution

print(numbers[0])


