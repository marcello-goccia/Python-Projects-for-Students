## Title
Check if Element Exists in List

## Description
You are given a list of integers. Write a program to check if a specific element exists in the list. 
If it does, print "Found", otherwise print "Not Found".

## Input Description
The variable "numbers" is already initialized with a list of integers.
The integer "target" is already initialized with an integer

## Output Description
Output "Found" if the target exists in the list, otherwise output "Not Found".

## Input Samples
numbers = [10, 20, 30]
target = 20

## Output Samples
Found


## 3 Hidden Test Cases (Input/Output) for validate code
1 2 3
2
Output: Found

5 4 3
10
Output: Not Found

10 20 30
25
Output: Not Found

## Code Template
numbers = list(map(int, input().split())) 
target = int(input())


## Solution
if target in numbers:
    print("Found")
else:
    print("Not Found")

