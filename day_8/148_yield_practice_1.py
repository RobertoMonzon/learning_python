# Create a generator (stored in the generator variable) that is capable of returning an infinite sequence of numbers, starting at 1, and returning a higher consecutive number each time next is called.

def gen():
    num=0
    while True:
       num += 1
       yield print(num)



[_ for _ in gen()]