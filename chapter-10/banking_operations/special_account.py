# SpecialAccount inherits from Account and uses super() to call Account's methods
from account import Account
class SpecialAccount(Account):
    def __init__(self, clients, number, balance=0, limit = 0):
        super().__init__(clients, number, balance)
        self.limit = limit
    def sake(self, value):
        if self.balance + self.limit >= value:
            self.balance -= value
            self.operations.append(["SAKE", value])
    def extract(self):
        super().extract()
        print(f'Your limit is: {self.limit + self.balance}')
        

specialaccount = SpecialAccount('Joao',2139021, 300,200)
specialaccount.sake(400)
specialaccount.extract()