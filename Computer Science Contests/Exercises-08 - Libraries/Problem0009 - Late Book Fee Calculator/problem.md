## Title
Late Book Fee Calculator

## Description
The city library needs a program to calculate late fees for different types of books. 
Each book type has its own late fee policy:

Fiction books: First 7 days free, then $2 per day
Textbooks: First 14 days free, then $5 per day
Reference books: First 10 days free, then $3 per day

Write a function calculate_late_fees that takes the days_borrowed and the book_type as input parameters and returns the total late fee for the book (integer)

## Input Description
Number of days the book is overdue (integer)
Book type (string: 'fiction', 'textbook', or 'reference')

## Output Description
Total late fee for the book (integer)

## Input Samples
10 fiction

## Output Samples
6

// PREPEND BEGIN
# No imports needed
// PREPEND END

// TEMPLATE BEGIN

# Write your code here

// TEMPLATE END

// APPEND BEGIN
# Read input
x = input()
days_borrowed, book_type = x.split()
days_borrowed = int(days_borrowed)

# Call function and print result
print(calculate_late_fees(days_borrowed, book_type))

// APPEND END


## Solution
def calculate_late_fees(days_borrowed, book_type):
    if book_type == 'fiction':
        free_days = 7
        fee_per_day = 2
    elif book_type == 'textbook':
        free_days = 14
        fee_per_day = 5
    elif book_type == 'reference':
        free_days = 10
        fee_per_day = 3
    else:
        return 0  # Invalid book type

    late_days = max(0, days_borrowed - free_days)
    return late_days * fee_per_day
