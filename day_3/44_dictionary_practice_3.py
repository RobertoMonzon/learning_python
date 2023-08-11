# Updates the information in our dictionary called my_dic (reassigning new values to the keys as appropriate), and adds a new key called "country" (without tilde). The new data is:

# name: Karen
# surname: Jurgens
# age: 36
# occupation: editor
# Country Colombia

mi_dic = {"name":"Karen", "surname":"Jurgens", "age":35, "occupation":"journalist"}
mi_dic.update({"age":36,"ocuppation":"editor","country":"Colombia"})
# mi_dic["age"]=(36)
# mi_dic["occupation"]=("editor")
# mi_dic["country"]=("colombia")
print(mi_dic)