## Title
Multiply Two Numbers

## Description
Write a function named multiply_two_numbers that takes two integers as parameters and returns their product.

Note: You only need to implement the function multiply_two_numbers, without worrying about input or output handling.

## Input Description
The function receives two integer parameters, a and b.

## Output Description
The function should return a single integer that represents the product of the two input integers.

## Input Samples
4 5


## Output Samples
20


## 3 Hidden Test Cases (Input/Output) for validate code


## Code_template:

//PREPEND BEGIN
import math  # Example of import statements or constants
//PREPEND END

//TEMPLATE BEGIN

def multiply_two_numbers(___, ___):
    # TODO: Write your code here
    pass

//TEMPLATE END

//APPEND BEGIN
# Read input
x = input()  # Assumes the input is something like "4 5" or "10 20"
a, b = map(int, x.split())  # Convert split input directly to integers

# Call the function and print result
print(multiply_two_numbers(a, b))  # Display result to validate

# Additional test cases
# assert multiply_two_numbers(1, 2) == 2
# assert multiply_two_numbers(-5, 5) == -25
# assert multiply_two_numbers(10, 20) == 200
//APPEND END

