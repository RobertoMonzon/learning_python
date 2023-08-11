# Prints on the screen only the indices of those names in the list below, beginning with M:
# list_names = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
# You can solve it in different ways, but it will help to keep in mind all or some of the following elements:
# loops
# if conditionals
# The enumerate() method
# String or indexing methods

list_names = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for index,name in enumerate(list_names):
    if name[0] == "M":
        print(index)
