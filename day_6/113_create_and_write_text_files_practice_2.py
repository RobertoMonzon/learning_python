# Open the file called "practice_3_txt.txt", and add a line to the end of it that says:
# "New login".
# Prints the entire content of "practice_3_txt.txt" when finished.

f=open("practice_3_txt.txt","a")
f.write(f"New Login\n")
f.close()
f=open("practice_3_txt.txt","r")
print(f.read())