import random
lifes=0

name=input("Hello, What is your name? ")

random_number= random.randint(1,100)
print(random_number)


while lifes < 10:
    number=int(input("Please type a number from 1 to 100 "))
    lifes += 1
    if number < random_number:
        print(f"{name} your number is smaller than the random number ")
    elif number > random_number:
        print(f"{name} your number is bigger than the random number ")
    elif number == random_number:
        print(f"{name} your number is the same than the random number.You Won!!! ")
        break

if number != random_number:
    print(f"Sorry {name} your didn't guess the number, the answer is {random_number}")

    
