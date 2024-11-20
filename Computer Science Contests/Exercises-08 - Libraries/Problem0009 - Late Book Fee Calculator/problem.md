## Title
Late Book Fee Calculator

## Description
The city library needs a program to calculate late fees for different types of books. 
Each book type has its own late fee policy:

Fiction books: First 7 days free, then $2 per day
Textbooks: First 14 days free, then $5 per day
Reference books: First 10 days free, then $3 per day

Write a function calculate_late_fees that takes the days_borrowed and the book_type and returns the total late fee for the book (integer)

## Input Description
Number of days the book is overdue (integer)
Book type (string: 'fiction', 'textbook', or 'reference')

## Output Description
Total late fee for the book (integer)

## Input Samples
10 fiction

## Output Samples
6


#PREPEND BEGIN
# No imports needed
#PREPEND END

#TEMPLATE BEGIN
def calculate_late_fees(days_borrowed, book_type):
    # TODO: Write your code here
    pass
#TEMPLATE END

#APPEND BEGIN
# Read input
x = input()
days_borrowed, book_type = x.split()
days_borrowed = int(days_borrowed)

# Call function and print result
print(calculate_late_fees(days_borrowed, book_type))

# Test cases
#assert calculate_late_fees(7, 'fiction') == 0
#assert calculate_late_fees(14, 'textbook') == 10
#assert calculate_late_fees(20, 'reference') == 30
#APPEND END
