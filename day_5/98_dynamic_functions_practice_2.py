# Create a function (add_less) that adds the numbers of a list (stored in the variable list_numbers) as long as they are greater than 0 and less than 1000, and returns the result of said sum.

list_numbers=[1,2,3,1001]


def sum_less(list_numbers):
    total=0
    for element in list_numbers:
        if element in range (0,1000):
            total+=element
        else:
            pass
    return total

print(sum_less(list_numbers))
