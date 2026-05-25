import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ubank_app.account import BankAccount, parse_money  # noqa: E402


class AccountTests(unittest.TestCase):
    def test_deposit_updates_balance(self):
        account = BankAccount("Tester", "100.00")

        account.deposit("25")

        self.assertEqual(account.formatted_balance(), "$125.00")

    def test_withdraw_rejects_insufficient_funds(self):
        account = BankAccount("Tester", "10.00")

        with self.assertRaises(ValueError):
            account.withdraw("25")

    def test_parse_money_rejects_negative_amount(self):
        with self.assertRaises(ValueError):
            parse_money("-1")


if __name__ == "__main__":
    unittest.main()

