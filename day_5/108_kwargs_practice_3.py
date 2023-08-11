# Create a function called describe_person, which takes its name and then any number of arguments as its parameters. This function should display on the screen:

# Characteristics of {name}:
# {argument_name}: {argument_value}
# {argument_name}: {argument_value}
# etc...
# For example:

# describe_person("Mary", eye_color="blue", hair_color="blonde")

# It will display on the screen:

# Characteristics of Maria:
# eye_color: blue
# hair_color: blond


def describre_person(name,**kwargs):
    print(f"Characteristics of {name}")
    for argument_name,argument_value in kwargs.items():
       new_name= argument_name.replace("_"," ")
       print(f"{new_name}:{argument_value}")


describre_person("Roberto",eye_color="brown",hair_color="black",body_type="skinny")