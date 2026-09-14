class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []
    def open_account(self, account):
        self.accounts.append(account)
    def account_lists(self):
        for ac in self.accounts:
            ac.resum()