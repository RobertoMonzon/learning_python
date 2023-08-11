# Create a function called list_attributes that returns in the form of a list the values of the attributes given in the form of keywords (keywords). The function must expect to receive any number of such arguments.

def list_attribute(**kwargs):
    list_=[]
    for element in kwargs.values():
        list_.append(element)
    return list_

print(list_attribute(a=2,b=3,c=3,d=4,e=5))