import uuid


class InsufficientFundsError(Exception):
    pass


class AccountNotFoundError(Exception):
    pass


class InvalidAmountError(Exception):
    pass


class Account:

    def __init__(self, owner, balance=0.0):
        self.account_id = str(uuid.uuid4())[:8]
        self.owner = owner
        self._balance = float(balance)
        self._history = []


    def deposit(self, amount):

        if amount <= 0:
            raise InvalidAmountError()

        self._balance += amount
        self._record("deposit", amount)

        return self._balance


    def withdraw(self, amount):

        if amount <= 0:
            raise InvalidAmountError()

        if amount > self._balance:
            raise InsufficientFundsError()

        self._balance -= amount
        self._record("withdrawal", amount)

        return self._balance


    def get_balance(self):
        return self._balance


    def get_history(self):
        return self._history


    def _record(self, transaction_type, amount):

        self._history.append(
            {
                "type": transaction_type,
                "amount": amount,
                "balance_after": self._balance
            }
        )


    def __str__(self):

        return (
            f"Account(id='{self.account_id}', "
            f"owner='{self.owner}', "
            f"balance={self._balance:.2f})"
        )



class SavingsAccount(Account):

    def __init__(self, owner, balance=0.0, interest_rate=0.05):

        super().__init__(owner, balance)
        self.interest_rate = interest_rate


    def apply_interest(self):

        interest_earned = self._balance * self.interest_rate

        self._balance += interest_earned

        self._record(
            "interest",
            interest_earned
        )

        return self._balance



class CheckingAccount(Account):

    def __init__(self, owner, balance=0.0, overdraft_limit=100.0):

        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit


    def withdraw(self, amount):

        if amount <= 0:
            raise InvalidAmountError()

        if amount > self._balance + self.overdraft_limit:
            raise InsufficientFundsError()

        self._balance -= amount

        self._record(
            "withdrawal",
            amount
        )

        return self._balance



class Bank:

    def __init__(self):

        self._accounts = {}


    def create_account(
        self,
        owner,
        account_type="checking",
        **kwargs
    ):

        if account_type == "savings":
            account = SavingsAccount(owner, **kwargs)

        else:
            account = CheckingAccount(owner, **kwargs)


        self._accounts[account.account_id] = account

        return account



    def get_account(self, account_id):

        if account_id not in self._accounts:
            raise AccountNotFoundError()

        return self._accounts[account_id]



    def deposit(self, account_id, amount):

        account = self.get_account(account_id)

        return account.deposit(amount)



    def withdraw(self, account_id, amount):

        account = self.get_account(account_id)

        return account.withdraw(amount)



    def transfer(self, from_id, to_id, amount):

        from_acc = self.get_account(from_id)
        to_acc = self.get_account(to_id)

        from_acc.withdraw(amount)
        to_acc.deposit(amount)

        return True



    def get_balance(self, account_id):

        account = self.get_account(account_id)

        return account.get_balance()



    def total_assets(self):

        return sum(
            account.get_balance()
            for account in self._accounts.values()
        )