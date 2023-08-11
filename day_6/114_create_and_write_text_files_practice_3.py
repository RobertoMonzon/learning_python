# Use the writelines method to write the values from the following list to the end of the "log.txt" file. Insert a tab between each list item to separate them.

# record_last_session = ["Federico", "20/12/2021", "08:17:32 hs", "No loading errors"]

# Prints the entire content of "registro.txt" upon completion.

register = ["Philip", "20/12/2021", "08:17:32 hs", "No loading errors"]
f=open("practice_4_txt.txt","a")
for i in register:
    f.writelines(i+"\t")
f.close()
f=open("practice_4_txt.txt","r")
print(f.read())