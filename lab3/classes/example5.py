class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, money):
            self.balance += money
            return f"You deposited {money}. New balance: {self.balance}"
       
    def withdraw(self, money):
        if money <= 0:
            return "Withdrawal amount must be greater than zero!"
        if self.balance < money:
            return "Insufficient funds!"
        else:
            self.balance -= money
            return f"You withdrew {money}. New balance: {self.balance}"

    def show_balance(self):
        return f"Owner: {self.owner}, Balance: {self.balance}"

bank = Account("Yrysty", 10000)
print(bank.show_balance())
print(bank.deposit(2500))  
print(bank.withdraw(3000))  
print(bank.withdraw(2000))  
print(bank.withdraw(15000)) 
print(bank.withdraw(-500))  

