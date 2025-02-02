## Title
Check if List is Empty

## Description
Write a program that checks if the list is empty. If it is empty, print "Empty", otherwise print "Not Empty".

## Input Description
The variable numbers is already initialized with a list of integers.

## Output Description
Output "Empty" if the list is empty, otherwise output "Not Empty".

## Input Samples
numbers = [10, 20]

## Output Samples
Not Empty

## 3 Hidden Test Cases (Input/Output) for validate code
1 2 3
Not Empty

[]
Empty

5
Not Empty

## Code Template
numbers = list(map(int, input().split())) 


## Solution
if len(numbers) == 0:
    print("Empty")
else:
    print("Not Empty")
