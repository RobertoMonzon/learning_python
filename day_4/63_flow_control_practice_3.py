# To access a certain job position, the candidate must be able to program in Python and have knowledge of English.
# Creates a conditional structure to evaluate a candidate given these conditions, and displays the corresponding message on the screen:
# "You meet the requirements to apply"
# "To apply, you need to know how to program in Python and have knowledge of English"
# "To apply, you need to have knowledge of English"
# "To apply, you need to know how to program in Python"
# It uses the already provided code base to set up the appropriate control flow structure and check those conditions. Evaluate a candidate who knows English, but doesn't program in Python.

speaks_english = True
knows_python = False





if speaks_english == True and knows_python == True:
    print("You meet the requirements to apply")
elif speaks_english == False and knows_python == False:
    print("To apply, you need to know how to program in Python and have knowledge of English")
elif speaks_english == False and knows_python == True:
    print("To apply, you need to have knowledge of English")
else:
    print("To apply, you need to know how to program in Python")