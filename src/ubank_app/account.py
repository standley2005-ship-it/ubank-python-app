"""Account logic for the UBank desktop simulation."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


MONEY = Decimal("0.01")


@dataclass(frozen=True)
class Transaction:
    kind: str
    amount: Decimal
    resulting_balance: Decimal
    note: str


def parse_money(value: str) -> Decimal:
    """Convert user input into a positive two-decimal money value."""
    try:
        amount = Decimal(value.strip()).quantize(MONEY, rounding=ROUND_HALF_UP)
    except (AttributeError, InvalidOperation):
        raise ValueError("Enter a valid number.") from None

    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    return amount


class BankAccount:
    """Simple in-memory account for a desktop banking simulation."""

    def __init__(self, owner: str, starting_balance: str = "250.00") -> None:
        self.owner = owner
        self.balance = Decimal(starting_balance).quantize(MONEY)
        self.transactions: list[Transaction] = []

    def deposit(self, raw_amount: str) -> Transaction:
        amount = parse_money(raw_amount)
        self.balance += amount
        transaction = Transaction("deposit", amount, self.balance, "Deposit accepted")
        self.transactions.append(transaction)
        return transaction

    def withdraw(self, raw_amount: str) -> Transaction:
        amount = parse_money(raw_amount)
        if amount > self.balance:
            raise ValueError("Insufficient funds for this withdrawal.")

        self.balance -= amount
        transaction = Transaction("withdrawal", amount, self.balance, "Withdrawal accepted")
        self.transactions.append(transaction)
        return transaction

    def formatted_balance(self) -> str:
        return f"${self.balance:,.2f}"

    def history_rows(self) -> list[str]:
        rows = []
        for transaction in self.transactions:
            rows.append(
                f"{transaction.kind.title()}: ${transaction.amount:,.2f} "
                f"-> ${transaction.resulting_balance:,.2f}"
            )
        return rows

