## Title
Store and Return List from User Input

## Description
Write a function called `get_list` that does not take any input parameters
but it stores "n" numbers in a list from the user input. The function should return the list. 

## Input Description
- An integer `n` that specifies how many integers will be entered.
- A list of `n` integers.

## Output Description
Return the list containing the `n` numbers.

## Input Samples
3
1
2
3

## Output Samples
[1, 2, 3]


## 3 Hidden Test Cases (Input/Output) for validate code
2
5
10
Output: 5 10

4 
1
3
5
7
Output: 1 3 5 7

5
2
4
6
8
10
Output: 2 4 6 8 10

## Code Template

//PREPEND BEGIN
//PREPEND END

//TEMPLATE BEGIN


//TEMPLATE END


//APPEND BEGIN
# Read input
my_list = get_list()

for i in my_list:
    print(i, end=' ')
//APPEND END


## Solution

def get_list():
    n = int(input())  # Number of elements
    numbers = []

    for _ in range(n):
        numbers.append(int(input()))  # Add each element to the list

    return numbers

