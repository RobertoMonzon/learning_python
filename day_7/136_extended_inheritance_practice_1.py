# If the Daughter class has inherited from their father the way of laughing, and from their mother the vocation, and today they have the same job in the Prosecutor's Office, create multiple inheritance that allows this class to correctly inherit from Father and Mother.

# Fill in the code provided below to achieve this.

class Father():
     def work(self):
         print("Working at the Hospital")

     def laugh(self):
         print("Ha ha ha!")

class Mother():
     def work(self):
         print("Working at the Prosecutor's Office")
        
class Daughter(Mother,Father):
     pass

Anna=Daughter()
Anna.work()