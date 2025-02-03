## Title
Pizza Slices Calculator

## Description
The local pizzeria needs help calculating how many pizzas to order for groups! Each person typically eats 3.7 slices, and each pizza has 8 slices.

Create a function calculate_pizzas that takes the number of people and returns the number of whole pizzas needed.
Round up to ensure everyone gets enough pizza!

## Input Description
An integer representing the number of people.

## Output Description
An integer representing the number of pizzas needed.

## Input Samples
5

## Output Samples
3

## Template Code
//PREPEND BEGIN
//PREPEND END

//TEMPLATE BEGIN

# Write your code here
//TEMPLATE END

//APPEND BEGIN
# Read input
number_of_people = int(input())

# Call function and print result
output = calculate_pizzas(number_of_people)

print(output)

// APPEND END


## Solution please check the code below.
def calculate_pizzas(number_of_people):
    slices_per_person = 3.7
    slices_per_pizza = 8
    total_slices_needed = number_of_people * slices_per_person
    pizzas_needed = -(-total_slices_needed // slices_per_pizza)  # This is a trick to round up
    return int(pizzas_needed)