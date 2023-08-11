#Person: name,lastame
#Client: account_number, balance
#methods: print(), deposit(), retire()

class Person:
    def __init__(self,name,last_name):
        self.name=name
        self.last_name=last_name
        
class Client(Person):

    def __init__(self,name,last_name,account_number,balance =0):
        super().__init__(name,last_name)
        self.account_number=account_number
        self.balance=balance

    def __str__(self):
        return f"Cliente:  {self.name} {self.last_name} \nBalance de cuenta {self.account_number} : $ {self.balance}"
    
    def deposit(self,amount_money):
        self.balance +=amount_money
        print("Your deposit has been accepted")

    def retire(self,retire_money):
        if self.balance >= retire_money:
            self.balance -= retire_money
            print("Succesful transaction")
        else:
            print("Not enought money in your account")

def create_client():
    name_cl=input("Type your name: ")
    last_name_cl=input("Type your last name: ")
    account_number_cl=input("Type your account number: ")
    client= Client(name_cl,last_name_cl,account_number_cl)
    return client

def start():
    my_client = create_client()
    print(my_client)
    option=0

    while option != "e":
        print("Chose: Deposit(d),retire (r) or exit (e)")
        option=input()
        if option== "d":
            amount_dep = int(input("amount of money for the deposit: "))
            my_client.deposit(amount_dep)
        elif option == "r":
            amount_ret= int(input("Amount of money for the retirement: "))
            my_client.retire(amount_ret)
        print(my_client)
    
    print("Goodbye")

start()
    