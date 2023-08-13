import practice_turn_machine_pt_1

def ask():
    print("Welcome to my pharmacy")

    while True:
        print("[p] for parfumery")
        print("[ph] for pharmacy")
        print("[c] for cosmetics")
        try:
            chose=input("Chose the area: ")
            ["p","ph","c"].index(chose)
        except ValueError:
            print("Is not a valid option")
        else:
            break
        
    practice_turn_machine_pt_1.interface(chose)


def start():

    while True:
        ask()
        try:
            another_turn=input("You need something else [y][n] ")
            ["s","n"].index(another_turn)
        except ValueError:
            print(" is not a valid option")
        else:
            if another_turn == "n":
                print("Goodbye")
                break


start()