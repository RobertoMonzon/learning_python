# Create a function (even_count) that counts the number of even numbers in a list (number_list), and returns the result of that count.

number_list=[1,2,3,4,5,6,7,8,9,10]

def even_count(number_list):
    quantity=0
    for element in number_list:
        if element%2 ==0:
            quantity+=1
        else:
            pass
    return quantity

print(even_count(number_list))