## Title
Add Two Elements to an Existing List

## Description
You are given an existing list. Write a program to add two elements to this list. 
After adding the elements, print the updated list.

## Input Description
The variable "numbers" is already initialized with a list of integers.
Two numbers are given as input, which will be added to the list.


## Output Description
Output the updated list after adding the two integers.

## Input Samples
4
5

Also numbers = [1, 2, 3] but you do not need to do anything


## Output Samples
1 2 3 4 5


## 3 Hidden Test Cases (Input/Output) for validate code
5 6 7
8
9
Output: 5 6 7 8 9

10 15 20
25
30
Output: 10 15 20 25 30

100 200 300
400
500
Output: 100 200 300 400 500

## Code Template
numbers = list(map(int, input().split()))  # The existing list is already initialized


## Solution
x = int(input())  # First element to add
y = int(input())  # Second element to add
numbers.append(x)
numbers.append(y)
print(numbers)

