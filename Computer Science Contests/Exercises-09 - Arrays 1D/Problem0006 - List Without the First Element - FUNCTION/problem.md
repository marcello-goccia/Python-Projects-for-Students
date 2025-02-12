## Title
List Without the First Element

## Description
Write a function 'list_without_first_element()' that takes a list as input parameter and
returns the list without the first element.

## Input Description
The input list is already initialized with integers.

## Output Description
Returns the list without the first element

## Input Samples
The functions take a list as input parameter.
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
my_list = list_without_first_element(numbers)

for i in my_list:
	print(i,  end=' ')
//APPEND END

## Solution
def list_without_first_element(numbers):
    return numbers[1:]

