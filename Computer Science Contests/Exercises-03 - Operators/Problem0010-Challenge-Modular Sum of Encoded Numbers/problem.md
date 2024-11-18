## Title
Challenge: Modular Sum of Encoded Numbers

## Description
You are given a single string containing a series of comma-separated encoded numbers. Each encoded number is a three-digit string, where:

The first digit represents the hundreds place.
The second digit represents the tens place.
The third digit represents the units place.
For each encoded number:

1. Add the hundreds, tens, and units digits to get a single sum for that number.
2. Sum all these individual sums together.
3. Return the remainder when this total is divided by 7.
Write a program to decode these numbers and calculate the result as described.

## Input Description
A single string containing comma-separated three-digit numbers (e.g., "123,456,789").

## Output Description
A single integer representing the remainder when the total sum is divided by 7.

## Input Samples
"123,456,789"


## Output Samples
3

## Solution

```python
def modular_sum_of_encoded_numbers(encoded_string):
    # Split the string into a list of three-digit numbers
    numbers = encoded_string.split(',')
    total_sum = 0
    
    # Process each number
    for number in numbers:
        # Convert each digit to an integer and sum them
        hundreds = int(number[0])
        tens = int(number[1])
        units = int(number[2])
        individual_sum = hundreds + tens + units
        
        # Add the individual sum to the total sum
        total_sum += individual_sum
    
    # Return the remainder when the total sum is divided by 7
    return total_sum % 7

# Test case
print(modular_sum_of_encoded_numbers("123,456,789"))  # Expected output: 6
```