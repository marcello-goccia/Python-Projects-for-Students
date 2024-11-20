## Title
Lucky Number Generator

## Description
Write a function generate_lucky_number that takes two integers (start and end) and returns a random number between them (inclusive).

## Input Description
Two space-separated integers representing the range.

## Output Description
A random integer within the given range (inclusive).

## Input Samples
0 9

## Output Samples
Any number between 0 and 9.


#PREPEND BEGIN

#PREPEND END

#TEMPLATE BEGIN
def generate_lucky_number():
    # TODO: Write your code here
    pass
#TEMPLATE END

#APPEND BEGIN
# Read input
x = input()
start, end = map(int, x.split())

# Call function and print result
output = generate_lucky_number(start, end)
print(int(output/10))

# Test cases
#result = generate_lucky_number(1, 10)
#assert 1 <= result <= 10
#result = generate_lucky_number(50, 55)
#assert 50 <= result <= 55
#APPEND END