"""Tkinter interface for the UBank banking simulation."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk

try:
    from .account import BankAccount
except ImportError:  # Allows running as: python src/ubank_app/main.py
    from account import BankAccount


class UBankApp(tk.Tk):
    """Small desktop UI for simulated banking actions."""

    def __init__(self) -> None:
        super().__init__()
        self.title("UBank Python App")
        self.geometry("460x420")
        self.resizable(False, False)

        self.account = BankAccount(owner="Demo User")
        self.amount_var = tk.StringVar()
        self.balance_var = tk.StringVar(value=self.account.formatted_balance())

        self._build_layout()

    def _build_layout(self) -> None:
        container = ttk.Frame(self, padding=24)
        container.pack(fill="both", expand=True)

        ttk.Label(container, text="UBank Simulation", font=("Segoe UI", 18, "bold")).pack(anchor="w")
        ttk.Label(
            container,
            text="Local student prototype. No real banking data is used.",
            foreground="#555555",
        ).pack(anchor="w", pady=(4, 18))

        balance_frame = ttk.LabelFrame(container, text="Account Balance", padding=16)
        balance_frame.pack(fill="x")
        ttk.Label(balance_frame, textvariable=self.balance_var, font=("Segoe UI", 24, "bold")).pack(anchor="w")

        form = ttk.Frame(container)
        form.pack(fill="x", pady=18)
        ttk.Label(form, text="Amount").pack(anchor="w")
        ttk.Entry(form, textvariable=self.amount_var).pack(fill="x", pady=(4, 10))

        actions = ttk.Frame(form)
        actions.pack(fill="x")
        ttk.Button(actions, text="Deposit", command=self.deposit).pack(side="left", expand=True, fill="x")
        ttk.Button(actions, text="Withdraw", command=self.withdraw).pack(
            side="left", expand=True, fill="x", padx=(8, 0)
        )

        ttk.Label(container, text="Session History", font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(10, 4))
        self.history = tk.Listbox(container, height=8)
        self.history.pack(fill="both", expand=True)

    def deposit(self) -> None:
        self._apply_transaction("deposit")

    def withdraw(self) -> None:
        self._apply_transaction("withdraw")

    def _apply_transaction(self, action: str) -> None:
        try:
            if action == "deposit":
                self.account.deposit(self.amount_var.get())
            else:
                self.account.withdraw(self.amount_var.get())
        except ValueError as error:
            messagebox.showerror("Transaction Error", str(error))
            return

        self.amount_var.set("")
        self.balance_var.set(self.account.formatted_balance())
        self._refresh_history()

    def _refresh_history(self) -> None:
        self.history.delete(0, tk.END)
        for row in self.account.history_rows():
            self.history.insert(tk.END, row)


if __name__ == "__main__":
    app = UBankApp()
    app.mainloop()

