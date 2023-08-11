# Using the max(), min() and dictionary methods, get the minimum value from the following dictionary:

# dic_ages = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2 ,"Dario":49}

# Store this value in a variable called minimum_age.

# Also, get the name that comes last in alphabetical order, and store it in a variable named last_name.

dic_ages = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2 ,"Dario":49}

minimum_age = min(dic_ages.values())
print(minimum_age)

last_name= max(dic_ages)
print(last_name)