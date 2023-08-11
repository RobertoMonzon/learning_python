# Create a function called overwrite() that opens a file given as a parameter, and overwrites any previous content with the text "content removed"

def overwrite(file):
    file=open(file,"w")
    return file.write("Content removed")


overwrite("def_practice_2_txt.txt")

f=open("def_practice_2_txt.txt","r")
print(f.read())

