# Create a function called attribute_count that counts the number of parameters that are passed, and returns that number as the result.

def attribute_count(**kwargs):
    quantity=0
    for key in kwargs.items():
        quantity+=1
    return quantity

print(attribute_count(y=1,x=2,z=2))