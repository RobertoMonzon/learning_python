# You have three classes of characters in a game, all of which have their specific defense methods.
# Create a function called character_defender(), which can receive an object 
# (an instance of your character classes), and call its defend() method regardless of what kind of character it is.

class Wizard():
     def defend(self):
         print("Magic Shield")

class Archer():
     def defend(self):
         print("Hide")

class Samurai():
     def defend(self):
         print("Lock")

def character_defend(character):
     character.defend()


