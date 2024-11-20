## Title
Number Rounder

## Description
Create a function that rounds a decimal number to the nearest integer.

## Input Description
Write a function round_number that takes a float number and returns it rounded to the nearest integer.

## Output Description
A single line containing a float number.

## Input Samples
An integer representing the rounded number.

## Output Samples
3.7

## 3 Hidden Test Cases (Input/Output) for validate code
4


#PREPEND BEGIN
import math
#PREPEND END

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

# Test cases
#assert round_number(3.7) == 4
#assert round_number(5.4) == 5
#assert round_number(2.5) == 3
#APPEND END
