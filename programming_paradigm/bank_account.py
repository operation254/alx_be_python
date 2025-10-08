class BankAccount:
    """A simple bank account with basic operations."""

    def __init__(self, initial_balance: float = 0.0):
        self.account_balance = float(initial_balance)

    def deposit(self, amount: float) -> None:
        """Add amount to balance (ignores negative amounts)."""
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            return
        if amt >= 0:
            self.account_balance += amt

    def withdraw(self, amount: float) -> bool:
        """Withdraw amount if funds are sufficient; return True/False."""
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            return False
        if amt < 0:
            return False
        if amt <= self.account_balance:
            self.account_balance -= amt
            return True
        return False

    def display_balance(self) -> None:
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance}")
