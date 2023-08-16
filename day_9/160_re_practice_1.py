# Create a function called verify_email to check if an email address is correct, that checks if the email given as an argument contains "@" (between the username and the domain) and ends in ".com" (although also accepting cases that have an additional domain, such as ".com.br" in the case of a user from Brazil).

# If the pattern is found, the function must finish displaying the message "Ok" on the screen, but if it detects that the phrase does not contain the indicated elements, it must inform the user "The email address is incorrect" by printing the message.

import re


def verify_email(email):
    pattern= r'@\w+\.com'
    verify= re.search(pattern,email)
    if verify:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


verify_email("engineer.monzon@gmail.com")