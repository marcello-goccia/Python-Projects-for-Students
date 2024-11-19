## Title
Convert Temperatures Between Celsius and Fahrenheit

## Description
Write a function convert_temperature that takes two parameters:

temp (a float): The temperature value to convert.
unit (a string): The unit of the temperature to convert from ('C' for Celsius, 'F' for Fahrenheit).

The function should return the converted temperature value as integer discarding the decimal values
Use the formula:

From Celsius to Fahrenheit: F = 9/5 * C + 32

From Fahrenheit to Celsius: C = 5/9 * (F - 32)

## Input Description
A float representing the temperature (temp).
A string representing the unit of the temperature ('C' for Celsius or 'F' for Fahrenheit).

## Output Description
An integer representing the converted temperature.

## Input Samples
60 C
45 F

## Output Samples
140
7


# Code_Template

//PREPEND BEGIN
# Import statements or constants (if needed)
//PREPEND END

//TEMPLATE BEGIN

def convert_temperature(temp, unit):
    # TODO: Write your code here
    pass

//TEMPLATE END


//APPEND BEGIN
# Read input
x = input()  # Assumes input is something like "60 C" or "45 F"
temp, unit = x.split()
temp = float(temp)

# Call the function and print result
print(convert_temperature(temp, unit))  # Display result to validate

# Additional test cases
#assert convert_temperature(0, 'C') == 32
#assert convert_temperature(32, 'F') == 0
#assert convert_temperature(100, 'C') == 212
//APPEND END
