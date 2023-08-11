# Create a class called Character, and give it the following class attribute:
# real = False
# Create an instance named harry_potter with the following instance attributes:
# species = "Human"
# magical = True
# age = 17

class Character:
    real=False
    def __init__(self,species,magical,age):
        self.species= species
        self.magical=magical
        self.age=age

harry_potter=Character("Human",True,17)
print(harry_potter.species)
print(harry_potter.magical)
print(harry_potter.age)
print(harry_potter.real)
