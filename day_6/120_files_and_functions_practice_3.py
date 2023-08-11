# Create a function called error_log() that opens (open) a file specified as a parameter, and updates it by adding a line at the end that says "an execution error has been logged". Finally, you should close the open file.


def overwrite(file):
    file=open(file,"a")
    return file.write("an execution error has been logged \n")


overwrite("def_practice_3_txt.txt")

f=open("def_practice_3_txt.txt","r")
print(f.read())