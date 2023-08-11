# Create a revive() class method that acts on the alive class attribute of the Player class,
#  setting it to True each time it is called. The default value of the live attribute must be False.

class PLayer:
    live=False
    @classmethod
    def revive(cls):
        cls.live=True

