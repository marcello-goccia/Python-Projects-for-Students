## Title
School Lunch Picker

## Description
Help the school cafeteria randomly assign daily specials! They have several menu items and need to pick one randomly each day.

Write a function pick_lunch_special that takes a day number (1-5 for Monday-Friday) and returns a random menu number (1-5).
The function should never return yesterday's menu number to avoid repetition.


## Input Description
Two integers: today's day number (1-5) and yesterday's menu number (1-5).

## Output Description
An integer representing today's menu number (different from yesterday's).

## Input Samples
2 3

## Output Samples
5



#PREPEND BEGIN
import random
#PREPEND END

#TEMPLATE BEGIN
def pick_lunch_special(day, yesterday_menu):
    # TODO: Write your code here
    pass
#TEMPLATE END

#APPEND BEGIN
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


# Test cases
#result = pick_lunch_special(2, 3)
#assert 1 <= result <= 5 and result != 3
#result = pick_lunch_special(1, 4)
#assert 1 <= result <= 5 and result != 4
#APPEND END
