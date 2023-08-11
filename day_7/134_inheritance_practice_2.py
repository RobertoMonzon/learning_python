# Create a class called Pet, which has the following instance attributes: age, name, number_paws. 
# Create another class, Dog, that inherits its attributes from the first.

class Pet():
    def __init__(self,age,name,number_paws):
        self.age=age
        self.name=name
        self.number_paws=number_paws
        
class Dog(Pet):
    pass

dog_1=Dog(2,"Harry",4)
print(dog_1.age)
print(dog_1.name)
print(dog_1.number_paws)