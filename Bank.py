class Bank:
    def __init__(self, name, branch) -> None:
        self.name = name
        self.branch = branch
        self.accounts = []
        self.admins = []
        self.is_bankrupt = False
        self.loan_status = True
        self.total_balance = 90000
        self.total_loan = 0

    def create_account(self, account):
        self.accounts.append(account)

    def admin_create(self, account):
        self.admins.append(account)

    def find_account(self, account_no):
        for account in self.accounts:
            if account.account_no == account_no:
                return account
        return None
    
    def del_account(self,account_no):
        account = self.find_account(account_no)
        if account:
            self.accounts.remove(account)
            print("** Account deleted Successfully **")
        else:
            print("Account Not Found!!")

    def see_accounts(self):
        print("Account_No\tName\tEmail\tAddress\tBalance")
        for acc in self.accounts:
            print(f"{acc.account_no} {acc.name} {acc.email} {acc.address} {acc.get_balance()}")
    
    


