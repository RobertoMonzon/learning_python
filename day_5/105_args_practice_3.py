# Create a function named person_numbers that receives a name as its first argument, followed by an indefinite number of numbers.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"

def person_numbers(name,*args):

    sum_numbers=sum(args)
    return(f"{name}, the sum of your numbers is {sum_numbers}")
    

print(person_numbers("Roberto",1,2,3))