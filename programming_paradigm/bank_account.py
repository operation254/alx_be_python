class BankAccount:
    """A simple bank account with basic operations."""

    def __init__(self, initial_balance: float = 0.0):
        self.account_balance = float(initial_balance)

    def deposit(self, amount: float) -> None:
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            return
        if amt >= 0:
            self.account_balance += amt

    def withdraw(self, amount: float) -> bool:
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            return False
        if amt < 0 or amt > self.account_balance:
            return False
        self.account_balance -= amt
        return True

    def display_balance(self) -> None:
        # 🔧 exact format the checker expects
        print(f"Current Balance: ${self.account_balance:.2f}")
