###### Title
Check if List is Empty

###### Description
Write a function 'is_list_empty' that takes a list as input parameter and
returns "Empty" if the list is empty, otherwise returns "Not Empty".

###### Input Description
The input list is already initialized with integers.

###### Output Description
Returns "Empty" if the list is empty, otherwise output "Not Empty".

###### Input Samples
The functions take a list as input parameter.
numbers = [10, 20]

###### Output Samples
Not Empty

###### 3 Hidden Test Cases (Input/Output) for validate code
1 2 3
Not Empty

[]
Empty

5
Not Empty

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
print(is_list_empty(numbers))
//APPEND END
###### Solution

def is_list_empty(numbers):
    return "Empty" if not numbers else "Not Empty"
