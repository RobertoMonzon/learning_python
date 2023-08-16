# Create a function called check_greeting to check if a sentence passed as an argument starts with the word "Hello". If the pattern is found, the function should terminate by displaying the message "Ok", but if it detects that the sentence does not contain "Hello", it should inform the user "You didn't say hello" by printing the message on the screen.

import re

def verificar_saludo(frase):
    patron = r'^Hola'
    verify=re.match(patron,frase)
    if verify:
        print("Ok")
    else:
        print("You didn't say hello")

verificar_saludo("Hola,como estas")





