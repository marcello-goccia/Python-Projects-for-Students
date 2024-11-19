## Title
Electricity Bill Calculator

## Description
Write a function calculate_electricity_bill that calculates the electricity bill:

First 50 units: $0.50 per unit
Next 100 units: $0.75 per unit
Units above 150: $1.00 per unit
Additional 20% tax on total bill

## Input Description
Function receives total electricity units consumed.

## Output Description
Return the total bill amount as an integer (rounded down).

## Input Samples
120

## Output Samples
116

## Code_Template

//PREPEND BEGIN
# No imports needed
//PREPEND END

//TEMPLATE BEGIN
def calculate_electricity_bill(___):
    # TODO: Write your code here
    pass
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
