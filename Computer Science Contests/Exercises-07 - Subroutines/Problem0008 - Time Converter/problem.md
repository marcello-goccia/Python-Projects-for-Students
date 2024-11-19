## Title
Time Converter

## Description
Write a function convert_to_minutes that converts total time to minutes.
Example: 2 hours and 30 minutes = 150 minutes

## Input Description
Function receives two integer parameters:

hours (non-negative)
minutes (0-59)

## Output Description
Return total minutes as an integer.

## Input Samples
2 30

## Output Samples
150


## Template_code

//PREPEND BEGIN
# No imports needed
//PREPEND END

//TEMPLATE BEGIN
def convert_to_minutes(___, ___):
    # TODO: Write your code here
    pass
//TEMPLATE END

//APPEND BEGIN
# Read input
hours, minutes = map(int, input().split())
print(convert_to_minutes(hours, minutes))

# Test cases
# assert convert_to_minutes(1, 0) == 60
# assert convert_to_minutes(0, 45) == 45
# assert convert_to_minutes(3, 15) == 195
//APPEND END