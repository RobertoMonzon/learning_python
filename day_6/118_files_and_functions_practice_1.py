# Create a function called open_read() that opens (open) a file indicated as a parameter, and returns its content (read).


def open_read(file):
    file = open(file,"r")
    return file.read()

print(open_read("def_practice_txt.txt"))
