# Implement for the following function sum(), a simple error handler that in case of any error, 
# prints the message: "Unexpected error" on the screen. 
# Otherwise, it should limit itself to displaying the result of the sum between the two numbers

def sum(num1,num2):

    try:
        print(num1+num2)    
    except:
        print("Unexpected error")
        
sum(1,"3")
    