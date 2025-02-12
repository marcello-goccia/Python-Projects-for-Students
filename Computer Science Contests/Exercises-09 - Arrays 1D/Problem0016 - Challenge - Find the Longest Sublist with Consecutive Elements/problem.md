## Title
Challenge - Find the Longest Sublist with Consecutive Elements


## Description
You are given a list of integers. Write a program that finds and prints the longest sublist of consecutive numbers 
in the list. If there are multiple sublists of the same length, return the first one.

## Input Description
The variable "numbers" is already initialized with a list of integers.

## Output Description
Output the longest sublist of consecutive numbers.

## Input Samples
numbers = [1, 9, 2, 3, 4, 20, 21, 22]

## Output Samples
2 3 4

## 3 Hidden Test Cases (Input/Output) for validate code

5 6 7 8 1 2 3
Output: 5 6 7 8

10 15 12 13 14 10 11
Output: 12 13 14

1 2 3 5 6 7 8
Output: 5 6 7 8

## Code Template
numbers = list(map(int, input().split())) 

## Solution
longest_sublist = []
current_sublist = []

for i in range(len(numbers)):
    if i == 0 or numbers[i] == numbers[i-1] + 1:
        current_sublist.append(numbers[i])
    else:
        if len(current_sublist) > len(longest_sublist):
            longest_sublist = current_sublist
        current_sublist = [numbers[i]]

if len(current_sublist) > len(longest_sublist):
    longest_sublist = current_sublist

for i in longest_sublist:
	print(i, end=" ")

