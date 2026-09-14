from clients import Client
from account import Account

joao = Client("João da Silva", "777-1234")
jose = Client("José da Silva", "444-291")

account = Account([joao, jose],"111-921",500)

account.resum()
account.deposit(10000)
account.sake(2)
account.extract()