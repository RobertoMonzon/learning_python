# The built-in function in Python len() has a polymorphic behavior, since it calculates the length of an object based on its type (strings, lists, tuples, among others), returning the number of items or characters that compose it.

# Create an iterator that loops through the following objects: word, list, tuple, and prints (print()) each of its lengths with the len() function.

word = "polymorphism"
list = ["Classes", "OOP", "Polymorphism"]
tuple = (1, 2, 3, 80)


for data in [word, list, tuple]:
     print(len(data))