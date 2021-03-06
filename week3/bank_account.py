class BankAccount:
    def __init__(self, name, balance, currency):
        if balance < 0:
            raise ValueError
        self._name = name
        self._balance = balance
        self._currency = currency
        self._history = ["Account was created"]

    def __str__(self):
        message = "Bank account for {} with balance of {}{}"
        return message.format(self._name, self._balance, self._currency)

    def __int__(self):
        self._history.append("__int__ check -> {}$".format(self._balance))
        return int(self._balance)

    def deposit(self, amount):
        if amount < 0:
            raise ValueError()
        else:
            self._balance += amount
            self._history.append(
                "Deposited {}{}".format(amount, self._currency))

    def balance(self):
        self._history.append("Balance check -> {}$".format(self._balance))
        return self._balance

    def withdraw(self, amount):
        if self._balance < amount:
            self._history.append(
                "Withdraw for {}{} failed".format(amount, self._currency)
            )
            return False
        else:
            self._balance -= amount
            self._history.append(
                "{}{} was withdrawed".format(amount, self._currency)
            )
            return True

    def transfer_to(self, account, amount):
        if self._currency == account._currency:
            self.withdraw(amount)
            account.deposit(amount)
        else:
            print("Transaction is not possible.")

    def history(self):
        return self._history

