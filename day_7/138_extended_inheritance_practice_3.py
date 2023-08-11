# # A son has inherited all his characteristics from his father, however, they have different hobbies. 
# Make the Child class inherit all of its methods and attributes from Parent by overriding the hobby() method so that it returns

class Father():
     eye_color = "brown"
     hair_type = "curlers"
     height = "average"
     voice = "serious"
     favorite_sport = "tennis"
     def laugh(self):
         return "Hahaha"
     def hobby(self):
         return "I paint wood in my free time"
     def walk(self):
         return "Walking with long and fast steps"
        
class Son(Father):
     def hobby(self):
         return"I play video games in my free time"
     
TomSR=Father()
TomJR=Son()
print(TomSR.hobby())
print(TomJR.hobby())
