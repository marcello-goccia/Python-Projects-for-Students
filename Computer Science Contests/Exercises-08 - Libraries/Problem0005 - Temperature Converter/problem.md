## Title
Temperature Converter

## Description
Write a function convert_temperature that generates a random temperature between two Celsius values, converts it to Fahrenheit, and rounds it to the nearest integer.
Formula: F = (C * 9/5) + 32

## Input Description
Two space-separated integers representing the minimum and maximum Celsius temperatures.

## Output Description
An integer representing the rounded Fahrenheit temperature.

## Input Samples
0 10

## Output Samples
43


#PREPEND BEGIN
import random
#PREPEND END

#TEMPLATE BEGIN
def convert_temperature(min_celsius, max_celsius):
    # TODO: Write your code here
    pass
#TEMPLATE END

#APPEND BEGIN
# Read input
x = input()
min_celsius, max_celsius = map(int, x.split())

# Call function and print result
output = convert_temperature(min_celsius, max_celsius)

lim1 = int(1.8 * min_celsius + 32)
lim2 = int(1.8 * max_celsius + 32)

if lim1 <= output <= lim2:
    print("Within range")
else:
    print("Out of range")


# Test cases
#result = convert_temperature(0, 10)
#assert 32 <= result <= 50
#result = convert_temperature(20, 30)
#assert 68 <= result <= 86
#APPEND END