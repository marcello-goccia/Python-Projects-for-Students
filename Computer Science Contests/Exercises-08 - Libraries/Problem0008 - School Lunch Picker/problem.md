## Title
School Lunch Picker

## Description

Help the school cafeteria randomly assign daily specials! They have several menu items and need to pick one randomly 
each day.

Write a function `pick_lunch_special` that takes two parameters:today's day number (1-5) and 
yesterday's menu number (1-5). 
The function should return a random menu number (1-5) that is different from yesterday's menu number 
to avoid repetition.

## Input Description
Two integers: today's day number (1-5) and yesterday's menu number (1-5).

## Output Description
An integer representing today's menu number (different from yesterday's).

## Input Samples
2 3

## Output Samples
5


// PREPEND BEGIN
// PREPEND END

// TEMPLATE BEGIN

# Write your code here

// TEMPLATE END

// APPEND BEGIN
# Read input
x = input()
day, yesterday_menu = map(int, x.split())

# Call function and print result
output = pick_lunch_special(day, yesterday_menu)

lim1 = 1
lim2 = 5

if lim1 <= output <= lim2 and output != yesterday_menu:
    print("Within range")
else:
    print("Not valid")

// APPEND END


## Solution
import random

def pick_lunch_special(day, yesterday_menu):
    while True:
        menu_number = random.randint(1, 5)
        if menu_number != yesterday_menu:
            return menu_number
