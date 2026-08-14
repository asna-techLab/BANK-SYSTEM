class BankAccount:
    def __init__(self, acc_id, balance, acc_type,customer_id):
        self.acc_id=acc_id
        self.balance=balance
        self.acc_type=acc_type
        self.customer_id=customer_id
        
    def cheak_balance(self):
        print("\nCurrent Balance:", self.balance)
        
    def show_account_type(self):
        print("Account Type:", self.account_type)
    
    def deposit(self, amount):
        if amount <= 0:
            print("invalid amount.")
            return
        self.balance += amount
        print("Deposit successful.")
        print("New balance:", self.balance)
    
    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid amount.")

        elif amount > self.balance:
            print("Insufficient balance.")

        else:
            self.balance -= amount
        print("Withdrawal successful.")
        print("Remaining balance:", self.balance)
    
    def __gt__(self, other):
        return self.balance > other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __eq__(self, other):
        return self.balance == other.balance
    
acc1 = BankAccount("001", 50000, "current", 21)
acc2 = BankAccount("002", 67000, "current", 14)
print(acc1>acc2)
    



