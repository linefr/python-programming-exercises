class Account:
    def __init__(self, clients, number, balance=0):
        self.balance = balance
        self.clients = list(clients)
        self.operations = []
        self.number = number
    def resum(self):
        print(f'checking account -- Number: {self.number} Balance: {self.balance}')
        for client in self.clients:
            print(f'Client: {client.name} -- Number Phone: {client.phone_number} \n')
    def sake(self, value):
        if self.balance >= value:
            self.balance -= value
            self.operations.append(["SAKE", value])
        else:
            print("insufficient funds".upper())
    def deposit(self, value):
        self.balance += value
        self.operations.append(["DEPOSIT", value])
    def extract(self):
        print(f'Extract account nº {self.number}\n')
        for operation in self.operations:
            print(f'{operation[0]:10s} {operation[1]:10.2f}')
        print(f'\n    Balance: {self.balance:8.2f}\n')


    
