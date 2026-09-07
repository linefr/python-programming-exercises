class Account:
    def __init__(self, clients, number, balance=0):
        self.balance = balance
        self.clients = clients
        self.number = number
    def resum(self):
        print(f'checking account -- Number: {self.number} Balance: {self.balance}')
    def sake(self, value):
        if self.balance >= value:
            self.balance -= value
    def deposit(self, value):
        self.balance += value
