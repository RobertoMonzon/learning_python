# The postal code for a given region is formed from two alphanumeric characters and four numeric characters after it (example: XX1234). Create a function, called verify_zp to check if the zip code passed as an argument follows this pattern. If the pattern is correct, show the user the message "Ok", otherwise: "The entered postal code is not correct".

import re

def verificar_cp(cp):
    patron=r"\w\w\d\d\d\d"
    verif=re.search(patron,cp)
    if verif:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")


verificar_cp("XX1234")
verificar_cp("XXX123")
