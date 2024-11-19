## Title
Repeat String

## Description
Write a function repeat_string that takes a string and an integer as parameters and returns the string repeated n times.

## Input Description
The function receives a string s and an integer n.


## Output Description
The function should return the string repeated n times.



## Input Samples
hello 3


## Output Samples
hellohellohello


## Code_Temaplte

//PREPEND BEGIN
# Import statements or constants (if needed)
//PREPEND END

//TEMPLATE BEGIN

def repeat_string(s, n):
    # TODO: Write your code here
    pass
  
//TEMPLATE END


//APPEND BEGIN
# Read input
x = input()  # Assumes input is something like "hello 3"
s, n = x.split()
n = int(n)

# Call the function and print result
print(repeat_string(s, n))  # Display result to validate

# Additional test cases
#assert repeat_string("hi", 2) == "hihi"
#assert repeat_string("a", 4) == "aaaa"
//APPEND END
