# Create a class called House, and assign it attributes: color, number_floors.

# Creates a House instance, called white_house, with color "white" and number of floors equal to 4.

class house:

    def __init__(self,color,number_of_floors):
        self.color=color
        self.number_of_floors=number_of_floors


white_house=house("white",4)

print(white_house.number_of_floors)