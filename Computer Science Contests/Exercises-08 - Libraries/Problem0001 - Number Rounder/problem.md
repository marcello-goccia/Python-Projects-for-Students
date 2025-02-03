## Title
Number Rounder

## Description
Create a function that rounds a decimal number to the nearest integer.

## Input Description
Write a function round_number that takes a float number and returns it rounded to the nearest integer.

## Output Description
Return a single line containing an integer number.

## Input Samples
3.7

## Output Samples
4

## 3 Hidden Test Cases (Input/Output) for validate code

//PREPEND BEGIN

//PREPEND END

//TEMPLATE BEGIN
def round_number(num):
    # TODO: Write your code here
    pass
//TEMPLATE END

//APPEND BEGIN
# Read input
variable = input() 
variable = float(variable)

# Call the function and print result
print(round_number(variable))  # Display result to validate

//APPEND END



#TEMPLATE BEGIN
def round_number(num):
    # TODO: Write your code here
    pass
#TEMPLATE END

#APPEND BEGIN
# Read input
x = float(input())

# Call function and print result
print(round_number(x))

#APPEND END

## Solution
def round_number(num):
    return int(round(num))