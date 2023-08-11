# Create a static method breathe() for the Pet class. When called, 
# it should print to the screen "Inhale...Exhale"

class Pet:
    @staticmethod
    def breathe():
        print("Inhale...Exhale")

pluto=Pet
pluto.breathe()