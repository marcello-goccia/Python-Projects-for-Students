## Title
Calculate Shipping Cost

## Description
Write a function named calculate_shipping that calculates shipping cost based on package weight.
Rules:

If weight is up to 2kg, cost is $5
If weight is above 2kg, cost is $5 plus $2 for each additional kg
Weight will always be a positive integer

## Input Description
Function receives one integer parameter weight representing package weight in kg.

## Output Description
Return the total shipping cost as an integer.

## Input Samples
3

## Output Samples
7



## TEMAPLE_CODE

//PREPEND BEGIN
# No imports needed
//PREPEND END

//TEMPLATE BEGIN

# TODO: Write your code here

//TEMPLATE END

//APPEND BEGIN
# Read input
weight = int(input())
print(calculate_shipping(weight))

# Test cases
# assert calculate_shipping(1) == 5
# assert calculate_shipping(5) == 11
# assert calculate_shipping(10) == 21
//APPEND END
