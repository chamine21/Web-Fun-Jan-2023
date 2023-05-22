from bankacount import BankAccount
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount( 500, 0.1)

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def display_user_info(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("Account Balance:", self.account.balance)
        
user1 = User('hsin','zekri@gmail.com')
user1.account.display_account_info()
