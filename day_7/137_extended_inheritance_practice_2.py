# "The platypus is one of the rarest creatures in the world: 
# although it is a mammal, it lays eggs; and it nurses its young but they do not have breasts." 

# Create a Platypus class that inherits from other classes: 
# Vertebrate, Fish, Reptile, Bird, and Mammal, such that you "build" an animal that has the following methods and attributes:

# - lay eggs()
# -has_beak = True
# -vertebrate = True
# - poisonous = True
# - swim()
# - walk()
# - breastfeed()

class Vertebrate:
     vertebrate = True

class Bird(Vertebrate):
     has_peak = True
     def lay_eggs(self):
         print("Laying eggs")

class Reptile(Vertebrate):
     poisonous = True

class Fish(Vertebrate):
     def swim(self):
         print("Swimming")
     def lay_eggs(self):
         print("Laying eggs")

class Mammal(Vertebrate):
     def walk(self):
         print("Walking")
     def breastfeed(self):
         print("Suckling young")

class Platypus(Bird,Reptile,Fish,Mammal):
     pass

# - lay eggs()
# -has_beak = True
# -vertebrate = True
# - poisonous = True
# - swim()
# - walk()
# - breastfeed()

Perry=Platypus()
Perry.lay_eggs()
print(Perry.has_peak)
print(Perry.vertebrate)
print(Perry.poisonous)
Perry.swim()
Perry.walk()
Perry.breastfeed()