#Create a function called sum_absolute, which takes a set of arguments of any extension, and returns the sum of their absolute values (that is, it takes the unsigned values and adds them, or what is the same, considers them all -negative and positive- as positive).

def sum_absolute(*args):
    sum=0
    for arg in args:
        sum += abs(arg)
    return sum


print(sum_absolute(-1,2,-3,5))