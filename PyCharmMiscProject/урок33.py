class BankAccount:
    def __int__(self,login,balance,password):
        self.login =login
        self.balance = balance
        self.password =password

class VIPMember(BankAccount):
    def __init__(self):
