###### Title
Sum of Elements in List

###### Description
Write a function 'sum_of_elements' that takes a list as input parameter and 
returns the sum of all elements in the list.

###### Input Description
The input list is already initialized with integers.

###### Output Description
Returns the sum of all elements in the list.

###### Input Samples
The functions take a list as input parameter.
numbers = [1, 2, 3, 4]

###### Output Samples
10

###### 3 Hidden Test Cases (Input/Output) for validate code
5, 10, 15
30

[]
0

10, -10, 5
5

###### Code Template
//PREPEND BEGIN
# No imports needed
//PREPEND END

//TEMPLATE BEGIN

# TODO: Write your code here

//TEMPLATE END

//APPEND BEGIN
# Read input
numbers = list(map(int, input().split()))

# Call the function and print result
print(sum_of_elements(numbers))


###### Solution
def sum_of_elements(numbers):
    return sum(numbers)

