# Use the range() function and a loop to add the squares of all numbers from 1 to 15 (inclusive). 
#Store the result in a variable called sum_squares.

# For it:
# Create a range of values that you can loop through
# For each of these values, find its squared value (power of 2). You may need to create intermediate variables (optionally).
# Add all the squared values obtained. Accumulates the sum in the variable sum_squares.
sum= 0
for number in range (1,15+1):
    number = number**2
    sum= sum + number
sum_squares=sum
print(sum_squares)

