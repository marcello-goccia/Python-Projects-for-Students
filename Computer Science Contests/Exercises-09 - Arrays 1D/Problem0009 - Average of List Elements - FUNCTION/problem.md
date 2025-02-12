###### Title
Average of List Elements

###### Description
Write a function called 'average_of_list_elements' that takes a list as input parameter and
returns the average of the elements in the list as a whole number.

###### Input Description
The input list is already initialized with integers.

###### Output Description
Returns the average of the elements in the list as a whole number

###### Input Samples
The functions take a list as input parameter.
numbers = [1, 5, 6, 7, 4]

###### Output Samples
4

###### 3 Hidden Test Cases (Input/Output) for validate code
1 1 1
1

2 4 6
4

10 20 30
20


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
print(average_of_list_elements(numbers))
//APPEND END

###### Solution
def average_of_list_elements(numbers):
    average = sum(numbers) / len(numbers)
    return average
