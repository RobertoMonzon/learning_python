# Given the following list of numbers, perform the sum of all even and odd* numbers separately in the variables sum_even and sum_odd respectively:

# list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

# *Remembering from the previous days: the module (or remainder) of a number divided by 2 is zero when said value is even, and 1 when it is odd

# number % 2 == 0 (even values)

# number % 2 == 1 (odd values)


list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
sum_pairs = 0
odd_sum = 0

for number in list_numbers:
    if number % 2 == 0:
        sum_pairs = sum_pairs + number

    elif number % 2 == 1:
        odd_sum = odd_sum + number
        
print(odd_sum)
print(sum_pairs)