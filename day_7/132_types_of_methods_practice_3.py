# Create a throw_arrow() instance method that subtracts by -1 the number of arrows a Character instance 
#has, which has an instance attribute of type number called number_arrows.

class Character:
    def __init__(self,number_arrows):
        self.number_arrows=number_arrows
        print(f"You have {number_arrows} arrows")

    def throw_arrow(self):
        self.number_arrows=self.number_arrows-1
        print(f"Now you have {self.number_arrows} arrows")


me=Character(14).throw_arrow()

