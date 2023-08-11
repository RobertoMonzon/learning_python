# Create a function (all_positive) that takes a list of numbers as a parameter, and returns True if all the values in a list are positive, and False if at least one of the values is negative. Creates a list called list_numbers with positive and negative values.
 
number= [1,2,3,4,-5]



def all_positive(number):
       for element in number:
              if element < 0:
                     return False
              else:
                     pass
       return True
        
print(all_positive(number))
        