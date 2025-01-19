## Title
Reverse Case

## Description
Write a program to convert all lowercase letters in a string to uppercase and all uppercase letters to lowercase.

## Input Description
A single string.

## Output Description
The string with reversed case.

## Input Samples
HeLLo WoRLd

## Output Samples
hEllO wOrlD



## SOLUTION for IGCSE COmputer Science

```python 
# Input string from the user
input_string = input("Enter a string: ")

# Initialize a variable to store the result
converted_string = ""

# Iterate through each character in the string
for char in input_string:
    # Check if the character is lowercase
    if 'a' <= char <= 'z':
        # Convert to uppercase
        converted_string += char.upper()
    # Check if the character is uppercase
    elif 'A' <= char <= 'Z':
        # Convert to lowercase
        converted_string += char.lower()
    else:
        # If not a letter, leave it as it is
        converted_string += char

# Output the converted string
print("The converted string is:", converted_string)
```
