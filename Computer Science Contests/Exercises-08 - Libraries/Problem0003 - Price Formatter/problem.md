## Title
Price Formatter

## Description
Write a function format_price that takes a float price and returns it rounded to exactly 2 decimal places.

## Input Description
A single line containing a float number representing a price.

## Output Description
A float number rounded to exactly 2 decimal places.

## Input Samples
3.567

## Output Samples
3.57


#PREPEND BEGIN
import math
#PREPEND END

#TEMPLATE BEGIN
def format_price(price):
    # TODO: Write your code here
    pass
#TEMPLATE END

#APPEND BEGIN
# Read input
price = float(input())

# Call function and print result
output = format_price(price)

print(f"{output:.2f}")

# Test cases
#assert format_price(3.567) == 3.57
#assert format_price(10.123) == 10.12
#assert format_price(2.999) == 3.00
#APPEND END