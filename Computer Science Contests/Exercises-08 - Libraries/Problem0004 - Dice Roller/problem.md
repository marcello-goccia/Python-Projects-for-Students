## Title
Dice Roller

## Description
Write a function roll_dice that takes the number of dice to roll and returns their sum.
Each die has 6 faces (1-6).

## Input Description
A single integer representing the number of dice to roll.

## Output Description
An integer representing the sum of all dice rolls.

## Input Samples
2

## Output Samples
7


#PREPEND BEGIN
import random
#PREPEND END

#TEMPLATE BEGIN
def roll_dice(num_dice):
    # TODO: Write your code here
    pass
#TEMPLATE END

#APPEND BEGIN
# Read input
num_dice = int(input())

# Call function and print result
output = roll_dice(num_dice)

lim1 = num_dice * 1
lim2 = num_dice * 6

if lim1 <= output <= lim2:
    print("Within range")
else:
    print("Out of range")

# Test cases
#result = roll_dice(2)
#assert 2 <= result <= 12
#result = roll_dice(3)
#assert 3 <= result <= 18
#APPEND END

## Solution
import random

def roll_dice(num_dice):
    return sum(random.randint(1, 6) for _ in range(num_dice))
