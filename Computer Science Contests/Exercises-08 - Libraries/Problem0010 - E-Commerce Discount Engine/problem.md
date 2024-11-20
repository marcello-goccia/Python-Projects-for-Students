## Title
E-Commerce Discount Engine

## Description
An online store wants to implement a smart discount system:

New customers: No discount
Regular customers: 10% discount on purchases over $100
Premium customers: 20% discount on purchases over $200
Discounts are applied only to the amount exceeding the threshold

Write a function apply_discount that takes the total purchase and the customer type and returns the final price after applying appropriate discount (float)


## Input Description
Total purchase amount (float)
Customer type (string: 'new', 'regular', or 'premium')

## Output Description
Final price after applying appropriate discount (float)

## Input Samples
150 regular

## Output Samples
135.0



#PREPEND BEGIN
# No imports needed
#PREPEND END

#TEMPLATE BEGIN
def apply_discount(total_purchase, customer_type):
    # TODO: Write your code here
    pass
#TEMPLATE END

#APPEND BEGIN
# Read input
x = input()
total_purchase, customer_type = x.split()
total_purchase = float(total_purchase)

# Call function and print result

output = apply_discount(total_purchase, customer_type)
print(int(output))

# Test cases
#assert apply_discount(100, 'new') == 100
#assert apply_discount(200, 'regular') == 180
#assert apply_discount(500, 'premium') == 400
#APPEND END
