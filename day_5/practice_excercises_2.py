# Write a function (you can give it any name you want) that receives any word as a parameter, and that return all your unique (non-repeating) letters but in order.
# For example, if when calling this function we pass the word "amusing"


def name_(name):
    list_= list(name.upper())
    list_=list(set(list_))
    list_.sort()
    return list_


print(name_("Roberto"))