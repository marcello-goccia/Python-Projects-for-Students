## Title
Electricity Bill Calculator

## Description
Write a function named calculate_electricity_bill that calculates the electricity bill:

First 50 units: $0.50 per unit
Next 100 units: $0.75 per unit
Units above 150: $1.00 per unit
Additional 20% tax on total bill

## Input Description
Function receives only one parameter, which is the total electricity units consumed.

## Output Description
Return the total bill amount as an integer (rounded down).

## Input Samples
120

## Output Samples
93

## Code_Template

//PREPEND BEGIN
# No imports needed
//PREPEND END

//TEMPLATE BEGIN

# TODO: Write your code here

//TEMPLATE END

//APPEND BEGIN
# Read input
units = int(input())
print(calculate_electricity_bill(units))

# Test cases
# assert calculate_electricity_bill(50) == 25
# assert calculate_electricity_bill(200) == 220
# assert calculate_electricity_bill(75) == 69
//APPEND END
