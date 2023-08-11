# You have three classes of characters in a game, which have their specific attack methods.

# Create an iterator that achieves a conjugate attack in the following order: Archer, Mage, Samurai, by calling the attack() method of each character. 
# You will need to create instances of each of the above classes to build an iterable (a list called characters) that can be traversed in that order.

class Wizard():
     def attack(self):
         print("Magic attack")

class Archer():
     def attack(self):
         print("Arrow release")

class Samurai():
     def attack(self):
         print("Attack with katana")

Wizard1=Wizard()
Archer1=Archer()
Samurai1=Samurai()
Warriors=[Wizard1,Archer1,Samurai1]

for warrior in Warriors:
     warrior.attack()
