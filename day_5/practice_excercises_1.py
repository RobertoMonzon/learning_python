# Create a function called return_different() that receives 3
# integers as parameters.
# If the sum of the 3 numbers is greater than 15, it will return the
# bigger number.
# If the sum of the 3 numbers is less than 10, it will return the
# minor number.
# If the sum of the 3 numbers is a value between 10 and 15
# (included) will return the number of intermediatevalue

list_=[1,5,2]

def return_different(a,b,c):
    list_=[a,b,c]
    if sum(list_) > 15:
        list_=list(set(list_))
        list_.sort()
        return list_[-1]
    elif sum(list_) < 10:
        list_=list(set(list_))
        list_.sort()
        return list_[0]
    elif sum(list_) >= 10 and sum(list_) <= 15:
        list_=list(set(list_))
        list_.sort()
        middle= float(len(list_))/2
        return list_[int(middle - .5)]



print(return_different(2,6,1))
    