In Python we are learning 1D arrays (lists for Python) and I need 10 easy OJ problems about lists. 
The students do not know anything about lists. Order the exercises from very easy to slightly more difficult.
Considering that the students are just starting programming then they may have difficulties. 
The students so far have learned the following: variables assignment (any datatype), casting, input/output, 
operators (// and % * as well), conditionals, iterations, functions.
Provide me the problems with the OJ Format. Each question should follow the following structure:

## Title
## Description
## Input Description
## Output Description
## Input Samples
## Output Samples
## 3 Hidden Test Cases (Input/Output) for validate code
## Code template
## Solution

The code_template part is where you can write some code that the student can use. I would like that the problem already 
prepares the input list for the student (if any). 
For example, if the problem requires the student to sum the elements of the list, the code_template should already have
the following code:
n = int(input())  
numbers = list(map(int, input().split())) 

The student then MUST use "numbers" in their code, and the Input Description should have something like this:
"The variable numbers is already initialized with a list of integers."

so if the students need to print the sum ofhte elements in the array, they should write something like this in the 
solution space and it would be fine:

print(sum(numbers))
Thank you


## Title
First Element of the List

## Description:
You are given a list of integers. Write a program to print the first element of the list.


## Input Description:
The variable "numbers" is already initialized with a list of integers.


## Output Description:
Output the first element in the list.

## Input Samples
numbers = [10, 20, 30]

## Output Samples
10

## 3 Hidden Test Cases (Input/Output) for validate code
1 2 3
1

5 4 3
5

100
100

## Code Template

numbers = list(map(int, input().split())) 

## Solution

print(numbers[0])


