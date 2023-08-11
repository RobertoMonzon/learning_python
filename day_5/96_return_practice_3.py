# Create a function called reverse_word that takes the characters of a given word as an argument, reverses the order of its characters, and returns them that way and in uppercase.

# For example, if we give it the word "Python", it should return: "NOHTYP"

# Also, you must create a variable called word, which contains the string that you prefer, to supply it as an argument to the created function.

# Hint: inside the created function, you will have to use already seen string methods.


def reversed_word(word):
    list_=list(word.upper())
    reversed_list=list_[::-1]
    reversed="".join(reversed_list)
    return reversed

print(reversed_word("Roberto"))
