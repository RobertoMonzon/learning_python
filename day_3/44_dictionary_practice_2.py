#Create a print function that returns the second list item named points2, inside the following dictionary.

#If the value 300 were to change in the future, the code should work the same to return the value at that position. To do this, you must refer to the names of the keys and/or indexes as appropriate.

mi_dict = {"values_1":{"v1":3,"v2":6},"points":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["points"]["points2"][1])