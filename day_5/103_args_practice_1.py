# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their squared values.

# For example, for the arguments sum_squares(1,2,3) it must return 14 (1+4+9).


def sum_squares(*args):
    sum=0
    for arg in args:
        sum+=(arg**2)
    return sum
    
print(sum_squares(2,2,2))
