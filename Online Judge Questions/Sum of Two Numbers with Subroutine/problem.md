## Title
Sum of Two Numbers

## Description
Write a function add_two_numbers(a, b) that takes in two integers as parameters and returns their sum.

Note: You only need to implement the function add_two_numbers, not any input or output handling.

Function Signature:

def add_two_numbers(a: int, b: int) -> int:

## Input Description
The function receives two integer parameters, a and b.

## Output Description
The function should return a single integer representing the sum of a and b.

## Input Samples
3 5

## Output Samples
8

## Template

```python
//PREPEND BEGIN
import math  # Example of import statements or constants
//PREPEND END

//TEMPLATE BEGIN

def add_two_numbers(a, b):
    # TODO: Write your code here
    pass
  
//TEMPLATE END


//APPEND BEGIN
#  Read input
x = input()  # Assumes the input is something like "3 5" or "10 20"
a, b = map(int, x.split())  # Convert split input directly to integers

# Call the function and print result
print(add_two_numbers(a, b))  # Display result to validate
//APPEND END
```

## Test cases

### test 1
1 2

3

### test 2
-5 5

0

### test 3
10 20

30