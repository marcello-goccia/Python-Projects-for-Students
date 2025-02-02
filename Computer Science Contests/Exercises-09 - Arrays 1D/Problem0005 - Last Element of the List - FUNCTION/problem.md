## Title
Last Element of the List

## Description
Write a function 'last_element_of_list' that takes a list as input parameter and
returns the last element of the list.
Note: You only need to implement the function last_element_of_list, not any input or output handling.

## Input Description
************
The input list is already initialized with integers.

## Output Description
Return the last element in the list.

## Input Samples
The functions take a list as input parameter.
numbers = [10, 20, 30]

## Output Samples
30

## 3 Hidden Test Cases (Input/Output) for validate code
1 2 3 
3

5 4 3 
3

100
100

## Code Template

//PREPEND BEGIN
# No imports needed
//PREPEND END

//TEMPLATE BEGIN

# TODO: Write your code here

//TEMPLATE END

//APPEND BEGIN
# Read input
numbers = list(map(int, input().split()))

# Call the function and print result
print(last_element_of_list(numbers))


## Solution

def last_element_of_list(numbers):
    return numbers[-1]
