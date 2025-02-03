## Title
Weather Forecast Game

## Description
You're creating a simple weather prediction game! Given today's temperature, predict if tomorrow will be warmer or colder.

Write a function predict_temperature that takes today's temperature and returns tomorrow's predicted temperature (randomly fluctuating between -2 and +2 degrees from today's temperature).

## Input Description
An integer representing today's temperature in Celsius.

## Output Description
An integer representing tomorrow's predicted temperature.

## Input Samples
20

## Output Samples
21


// PREPEND BEGIN
// PREPEND END

// TEMPLATE BEGIN
# Write your code here
// TEMPLATE END

// APPEND BEGIN
# Read input
today_temp = int(input())

# Call function and print result
output = predict_temperature(today_temp)

lim1 = today_temp - 2
lim2 = today_temp + 2

if lim1 <= output <= lim2:
    print("Within range")
else:
    print("Out of range")

# Test cases
#result = predict_temperature(20)
#assert 18 <= result <= 22
#result = predict_temperature(25)
#assert 23 <= result <= 27

// APPEND END

## Solution please
import random

def predict_temperature(today_temp):
    return today_temp + random.randint(-2, 2)