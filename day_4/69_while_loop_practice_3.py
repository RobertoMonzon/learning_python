# Create a For loop through the following list of numbers, printing each of its elements to the screen, and break the flow the moment you encounter a negative value:

# list_numbers = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

list_numbers = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for num in list_numbers:
    if num > 0:
        print(num)
    else:
        break