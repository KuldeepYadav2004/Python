class Account:
    def __init__(self,account_number,name):
        self.account_number=account_number
        self.name = name
        self.balance = 0
    def print_account_details(self):
        print(f"Account Number:{self.account_number}")
        print(f"Name:{self.name}")
        print(f"Balance:{self.balance}")

class Transaction(Account):
    def __init__(self, account_number, name):
        super().__init__(account_number,name)     #Account.__init__(self,account_number,name)
    def deposit(self):
        amount=int(input("Enter thr amount to deposit: Rs."))
        if amount>0:
            self.balance += amount          #self.balance= self.balance+amount
            print(f"{amount} is deposited succesfully")
            print(f"New Balance: Rs{self.balance}")
        else:
            print("Invalid amount")
    def withdraw(self):
        if self.balance >0:
            amount=int(input("Enter thr amount to withdraw: Rs."))
            if amount>0:
                if amount<= self.balance:
                    self.balance-=amount  #self.balance=self.balance-amount
                    print(f"Rs.{amount} is withdrawn succesfully ")
                    print(f"New Balance: Rs.{self.balance}")
                else:
                    print("Insufficent Balance")
                
            else:
                print("Invalid amount")

            
        
        else:
            print("No balance")

t=Transaction(1224,"Vijay Verma")
t.print_account_details()
t.withdraw()
t.deposit()
t.withdraw()




        




        