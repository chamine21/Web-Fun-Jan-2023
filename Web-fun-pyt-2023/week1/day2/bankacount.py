class BankAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5

    def display_account_info(self):
        print("Balance: $", self.balance)

    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.interest_rate
            self.balance += interest
            

acc1 = BankAccount(200,0.02)
acc1.display_account_info()