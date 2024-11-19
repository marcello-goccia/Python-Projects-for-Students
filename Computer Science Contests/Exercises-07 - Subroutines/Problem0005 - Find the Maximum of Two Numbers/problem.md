## Title
Find the Maximum of Two Numbers

## Description
Write a function max_of_two that takes in two integers and returns the greater of the two.
Note: You only need to implement the function max_of_two, not any input or output handling.

## Input Description
The function receives two integer parameters, a and b.

## Output Description
The function should return the greater of the two integers.

## Input Samples
10 20


## Output Samples
20


## Code_template

//PREPEND BEGIN
# No imports needed
//PREPEND END

//TEMPLATE BEGIN

def max_of_two(__, ___):
    # TODO: Write your code here
    pass

//TEMPLATE END

//APPEND BEGIN
# Read input
x = input()  # Assumes the input is something like "10 20"
a, b = map(int, x.split())

# Call the function and print result
print(max_of_two(a, b))

# Additional test cases
# assert max_of_two(1, 2) == 2
# assert max_of_two(5, 5) == 5
# assert max_of_two(-3, -2) == -2
//APPEND END
