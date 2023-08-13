# Implements an error handler for the following quotient() function:
# In the event of a type error (TypeError), the message must be printed on the screen: 
# "The arguments to be entered must be numbers"
# If a division by zero is generated (error of type ZeroDivisionError), the message displayed should be: 
# "The second argument must not be zero"
# If an error does not occur, 
# it should simply print the result of the quotient (division) between the two numbers given as argument.


def quotient(num1,num2):
    
     try:
         print(num1/num2)
     except TypeError:
         print("The arguments to be entered must be numbers")
     except ZeroDivisionError:
         print("The second argument must not be zero")