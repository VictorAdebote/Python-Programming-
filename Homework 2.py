import tkinter as tk
from datetime import datetime

class BankAccountApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Account Application")

        # Initialize variables
        self.account_balance = 0
        self.transaction_history = []

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Labels
        self.label_balance = tk.Label(self.root, text="Account Balance:")
        self.label_balance.grid(row=0, column=0, padx=10, pady=10)

        # Entry widget to display balance
        self.entry_balance = tk.Entry(self.root, state="readonly")
        self.entry_balance.grid(row=0, column=1, padx=10, pady=10)
        self.update_balance_display()

        # Entry widget for transaction amount
        self.entry_amount = tk.Entry(self.root)
        self.entry_amount.grid(row=1, column=0, padx=10, pady=10)

        # Buttons
        self.button_deposit = tk.Button(self.root, text="Deposit", command=self.deposit)
        self.button_deposit.grid(row=1, column=1, padx=10, pady=10)

        self.button_withdraw = tk.Button(self.root, text="Withdraw", command=self.withdraw)
        self.button_withdraw.grid(row=1, column=2, padx=10, pady=10)

        self.button_view_transactions = tk.Button(self.root, text="View Transactions", command=self.view_transactions)
        self.button_view_transactions.grid(row=2, column=0, columnspan=3, pady=10)

    def deposit(self):
        amount = float(self.entry_amount.get())
        if amount > 0:
            self.account_balance += amount
            self.update_balance_display()
            self.record_transaction("Deposit", amount)
        else:
            self.show_error("Invalid Amount", "Please enter a valid deposit amount.")

    def withdraw(self):
        amount = float(self.entry_amount.get())
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            self.update_balance_display()
            self.record_transaction("Withdrawal", amount)
        else:
            self.show_error("Invalid Amount", "Please enter a valid withdrawal amount.")

    def view_transactions(self):
        transactions = "\n".join(self.transaction_history)
        self.show_message("Transaction History", transactions)

    def record_transaction(self, action, amount):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = f"{timestamp} - {action}: {amount}"
        self.transaction_history.append(transaction)

    def update_balance_display(self):
        self.entry_balance.config(state="normal")
        self.entry_balance.delete(0, tk.END)
        self.entry_balance.insert(0, f"${self.account_balance:.2f}")
        self.entry_balance.config(state="readonly")

    def show_error(self, title, message):
        tk.messagebox.showerror(title, message)

    def show_message(self, title, message):
        tk.messagebox.showinfo(title, message)

if __name__ == "__main__":
    root = tk.Tk()
    app = BankAccountApp(root)
    root.mainloop()