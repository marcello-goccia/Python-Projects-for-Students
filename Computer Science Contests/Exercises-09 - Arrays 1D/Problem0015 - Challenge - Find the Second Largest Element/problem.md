## Title
Challenge - Find the Second Largest Element

## Description
Write a program that finds and prints the second largest element in a list of integers. 
If there is no second largest (i.e., the list contains fewer than two distinct elements), print "No second largest".

## Input Description
The variable "numbers" is already initialized with a list of integers.

## Output Description
Output the second largest element if it exists, otherwise output "No second largest".

## Input Samples
numbers = [10, 20, 30, 20]


## Output Samples
20

## 3 Hidden Test Cases (Input/Output) for validate code
1 2 3 4
Output: 3

5 5 5
Output: No second largest

100 200 300 400 400
Output: 300

## Code Template
numbers = list(map(int, input().split())) 

## Solution
numbers = list(set(numbers))  # Remove duplicates
if len(numbers) < 2:
    print("No second largest")
else:
    numbers.sort(reverse=True)
    print(numbers[1])

