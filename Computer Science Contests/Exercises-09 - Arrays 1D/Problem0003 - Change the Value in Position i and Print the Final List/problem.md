## Title
Change the Value in Position i and Print the Final List

## Description
You are given a list of integers. Write a program that changes the value at a certain position in the list to a new value.
Then, print the final list.

## Input Description
The variable "numbers" is already initialized with a list of integers.
A integer is given as input, which represents the index in the list to be modified.
The new value to be assigned at index is given as input.

## Output Description
Output the final list after the modification.

## Input Samples

2
99

Also numbers = [10, 20, 30, 40] but you do not need to do anything

## Output Samples
10 20 99 40


## 3 Hidden Test Cases (Input/Output) for validate code
1 2 3 4
1
100
Output: 1 100 3 4

5 6 7
0
500
Output: 500 6 7

10 20 30 40
3
1000
Output: 10 20 30 1000

## Code Template
numbers = list(map(int, input().split())) 

## Solution
i = int(input())  # Index to change
new_value = int(input())  # The new value to assign
numbers[i] = new_value
print(numbers)
