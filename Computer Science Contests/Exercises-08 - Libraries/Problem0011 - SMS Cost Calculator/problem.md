## Title
SMS Cost Calculator

## Description
A mobile carrier wants to implement a messaging cost system:

Standard SMS messages are limited to 160 characters
Messages longer than 160 characters are split into multiple SMS
Each SMS costs $1 to send
Calculate the total number of SMS needed to send a message

Write a function calculate_message_cost that takes the full SMS message and returns the number of SMS required to send the message (integer)


## Input Description
The full text message (string)

## Output Description
The function returns the number of SMS required to send the message (integer)

## Input Samples
Hello world! This is a test message.

## Output Samples
1


#PREPEND BEGIN
# No imports needed
#PREPEND END

#TEMPLATE BEGIN
def calculate_message_cost(message):
    # TODO: Write your code here
    pass
#TEMPLATE END

#APPEND BEGIN
# Read input
message = input()

# Call function and print result
print(calculate_message_cost(message))

# Test cases
#assert calculate_message_cost('Hello') == 1
#assert calculate_message_cost('This is a longer message!') == 2
#assert calculate_message_cost('A' * 160) == 1
#APPEND END
