# Create a class called Vehicle, 
# which contains the accelerate() and brake() methods 
# (you can leave the code of the methods blank with pass). 
# Create a class called Car that inherits these methods from Car.

class Vehicle():
    def accelerate(self):
        print("accelerate")
    def brake(self):
        print("brake")

class Car(Vehicle):
    pass

vw=Car
print(vw.accelerate)
print(vw.brake)