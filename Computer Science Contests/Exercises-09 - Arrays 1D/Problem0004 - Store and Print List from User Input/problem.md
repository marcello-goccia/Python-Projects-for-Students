## Title
Store and Print List from User Input


## Description
Write a program that stores "n" numbers in a list. 
After creating the list, print the list.

## Input Description
A number "n" that specifies how many integers they will enter.
Then, "n" integersm, each one in a new line.

## Output Description
Output the list containing the "n" numbers.

## Input Samples
3
1
2
3

## Output Samples
1 2 3

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
------

## Solution
n = int(input())  # Number of elements
numbers = []

for _ in range(n):
    numbers.append(int(input()))  # Add each element to the list

print(numbers)
