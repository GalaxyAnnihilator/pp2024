import threading
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner 
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        print(f"New balance: {self.balance}")

acc1 = BankAccount("Alice",1000)
acc1.deposit(500)

class SavingsAccount(BankAccount):
    def __init__(self,owner,balance=0,interest_rate=0.02):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate
        self.lock = threading.Lock()

    def apply_interest(self):
        self.balance *= (1+self.interest_rate)

    def deposit(self,amount):
        self.balance += amount
        self.apply_interest()
        print("Deposit received. Interest will be applied.")

    def save_to_file(self,filename):
        try:
            with open(filename,'w') as f:
                f.write(f"Owner:{self.owner}\n")
                f.write(f"Balance:{self.balance}\n")
                f.write(f"Interest Rate: {self.interest_rate}\n")
        except Exception as e:
            print(e)
    
    def safe_deposit(self,amount):
        with self.lock:
            t = threading.Thread(target=self.deposit,args=(amount,))
            t.start()
            t.join()
            print(f"New balance: {self.balance}")

acc2 = SavingsAccount("Duong",10000,0.05)
acc2.safe_deposit(100)     
acc2.save_to_file("account_info.txt")       
