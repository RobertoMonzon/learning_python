# Create a function called reduce_list() that takes a list as an argument (also creates the variable list_numbers), and returns the same list, but eliminating duplicates (leaving only one of the numbers if there are duplicates) and eliminating the highest value. The order of the elements can be changed.

# For example, if given the list [1,2,15,7,2] it should return [1,2,7].

# Create a function called average() that can receive as an argument the list returned by the previous function, and that calculates the average of its values. It should return the result, without printing it.

list_numbers= [1,2,3,6,2,3,4,5]

def reduce_list(list_):
    list_=list(set(list_))
    list_.sort()
    list_.pop(-1)
    return list_



def average(list_):
        sum_=sum(list_)
        avg=sum_/(len(list_))
        return avg
    
list_of_numbers=reduce_list(list_numbers)
print(average(list_of_numbers))