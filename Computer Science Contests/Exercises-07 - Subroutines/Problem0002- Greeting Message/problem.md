## Title
Greeting Message

## Description
Write a function greet that takes a string as a parameter and returns a greeting in the format "Hello, [name]!".

## Input Description
The function receives a single string parameter name.

## Output Description
The function should return a single string in the format "Hello, [name]!".

## Input Samples
Alice

## Output Samples
Hello, Alice!

## Code Template

//PREPEND BEGIN
# Import statements or constants (if needed)
//PREPEND END

//TEMPLATE BEGIN

def greet(name):
    # TODO: Write your code here
    pass
  
//TEMPLATE END


//APPEND BEGIN
# Read input
name = input()  # Assumes input is something like "Alice"

# Call the function and print result
print(greet(name))  # Display result to validate

# Additional test cases
#assert greet("John") == "Hello, John!"
#assert greet("Python") == "Hello, Python!"
//APPEND END
