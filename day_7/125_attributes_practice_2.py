# Create a class called Cube, and assign it the class attribute:
# heads = 6
# and the instance attribute:
# color
# Creates a red_cube instance of that color.


class Cube:
    heads=6
    def __init__(self,color):
        self.color=color
    
red_cube=Cube("red")

print(red_cube.heads)
print(red_cube.color)