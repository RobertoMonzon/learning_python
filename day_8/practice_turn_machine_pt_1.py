#perfumery
#pharmacy
#cosmetics

def perfumery():
    for n in range(1,1000):
        yield f"P-{n}"

def pharmacy():
   for n in range(1,1000):
        yield f"Ph-{n}"

def cosmetics():
   for n in range(1,1000):
        yield f"C-{n}"


p=perfumery()
ph=pharmacy()
c=cosmetics()

def interface(my_chose):
    print("_________________")
    print("Your turn is: ")
    if my_chose == "p":
        print(next(p))
    elif my_chose == "ph":
        print(next(ph))
    elif my_chose == "c":
        print(next(c))
    print("Wait until we call you please")
    print("_________________")

   
                             



# phar=0
# cosm=0