# Prints sentences like the following on the screen:
# '{name} is found at index {index}'
# Where name should be each of the names in the list below, and the index, obtained by enumerate().
# list_names = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
# You can modify the print() line given as an example, but the sentences returned must be the same.


# list_names = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

# print(f'{name} is found at index {index}')


list_names = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for index,name in enumerate(list_names):
    print(f"{name} is found at index {index}")