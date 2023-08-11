# Open the file called "my_file.txt", and change its content to the text "New text".

# Prints the entire content of "my_file.txt" when finished.

file = open("practice_2_txt.txt", "w")
file.write("New text")
file.close()
file = open("practice_2_txt.txt", "r")
print(file.read())