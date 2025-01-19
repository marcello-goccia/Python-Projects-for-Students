## Title
Discount Calculator

## Description
Write a function named calculate_discount that calculates final price:

Discount is applied to original price
If discount makes price negative, return 0
Round down the final price to the nearest integer

## Input Description
Function receives two parameters:

original_price: initial price as a number
discount_percentage: discount percentage as a number

## Output Description
Return final price after discount.

## Input Samples
100 20

## Output Samples
80


## Code_Template


//PREPEND BEGIN
# No imports needed
//PREPEND END

//TEMPLATE BEGIN

# TODO: Write your code here

//TEMPLATE END

//APPEND BEGIN
# Read input
original_price, discount = map(int, input().split())
print(calculate_discount(original_price, discount))

# Test cases
# assert calculate_discount(50, 10) == 45
# assert calculate_discount(200, 50) == 100
# assert calculate_discount(30, 80) == 6
//APPEND END