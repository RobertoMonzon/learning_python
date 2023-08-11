# Join the following sets into one, called my_set_3:
# {1, 2, "three", "four"}
# {"three", 4, 5}

my_set_1= {1, 2, "three", "four"}
my_set_2= {"three", 4, 5}
my_set_3= my_set_1.union(my_set_2)
print(my_set_3)