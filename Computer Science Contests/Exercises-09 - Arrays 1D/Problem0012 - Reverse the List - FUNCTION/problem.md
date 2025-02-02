**###### Title
Reverse the List

###### Description
Write a function 'reverse_a_list' that takes a list as input parameter and
returns the list with the elements in reverse order.

###### Input Description
The input list is already initialized with integers.

###### Output Description
Returns the reversed list.


###### Input Samples
The functions take a list as input parameter.
numbers = [1, 2, 3, 4]


###### Output Samples
4 3 2 1


###### 3 Hidden Test Cases (Input/Output) for validate code
1 2 3
3 2 1

5 4 3 2 1
1 2 3 4 5

0
0

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
print(reverse_a_list(numbers))

###### Solution
def reverse_a_list(numbers):
    return numbers[::-1]

