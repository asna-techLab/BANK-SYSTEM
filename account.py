class BankAccount:
    def __init__(self, acc_no, balance, acc_type):
        self.acc_no=acc_no
        self.balance=balance
        self.acc_type=acc_type
        
    def cheak_balance(self):
        print(self.balance)
    
    def deposit(self, amount):
        self.amount=amount
        self.balance += amount
    
    def withdraw(self, amount):
        self.amount=amount
        self.balance -= amount
    
    def transfer(self):
        print
    
acc1=BankAccount("001", 50000, "current")
acc2=BankAccount("002", 34000, "saving")
acc2.withdraw(3000)
acc2.cheak_balance()


