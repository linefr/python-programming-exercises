from clients import Client
from account import Account

joao = Client("Joao da Silva", "777-1234")
maria = Client("Maria da Silva", "555-4321")

account = Account([joao,maria], "999-111")

account.resum()
account.deposit(10000)
account.sake(100000)
account.extract()