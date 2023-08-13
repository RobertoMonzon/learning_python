# Implement an error handler inside the following function, open_file():

# In the event that the file you are trying to open cannot be found (FileNotFoundError), display the message: "The file was not found"

# In case another type of error occurs, display the message: "Unknown error"

# If no error occurs, print on screen: "Opening successfully"

# In all cases, when finished, print: "Finishing execution"


def open_file(file_name):
     try:
         file = open(file_name)
     except FileNotFoundError:
         print("The file was not found")
     except:
         print("Unknown error")
     else:
         print("Opening successfully")
     finally:
         print("Ending execution")