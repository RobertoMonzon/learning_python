# Create a generator (stored in the generator variable) that is capable of returning multiples of 7 indefinitely, starting from 7 itself, and that each time it is called it returns the next multiple (7, 14, 21, 28... ).

def gen():
    num=1
    while True:
        num+=1
        yield print(num*7)

        


[_ for _ in gen()]