#!/usr/bin/env python3
"""
Banking Management System
A desktop GUI application using Tkinter and SQLite.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import hashlib
import random
import datetime

# ── Database Setup ──────────────────────────────────────────────
DB_NAME = "bank.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            acc_num TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            pin_hash TEXT NOT NULL,
            balance REAL DEFAULT 0.0
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            acc_num TEXT NOT NULL,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            other_acc TEXT,
            timestamp TEXT NOT NULL,
            FOREIGN KEY (acc_num) REFERENCES accounts(acc_num)
        )
    """)
    # Create admin account if not exists
    admin_pin = hashlib.sha256("admin123".encode()).hexdigest()
    cur.execute("SELECT * FROM accounts WHERE acc_num='ADMIN'")
    if not cur.fetchone():
        cur.execute("INSERT INTO accounts VALUES ('ADMIN','Administrator',?,0.0)", (admin_pin,))
    conn.commit()
    conn.close()

def execute_query(query, params=(), fetch=False, commit=False):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(query, params)
    if commit:
        conn.commit()
    if fetch:
        result = cur.fetchall()
    else:
        result = None
    conn.close()
    return result

# ── Helper Functions ────────────────────────────────────────────
def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()

def generate_account_number():
    while True:
        acc_num = str(random.randint(1000000000, 9999999999))
        if not execute_query("SELECT * FROM accounts WHERE acc_num=?", (acc_num,), fetch=True):
            return acc_num

def record_transaction(acc_num, txn_type, amount, other_acc=None):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    execute_query(
        "INSERT INTO transactions (acc_num, type, amount, other_acc, timestamp) VALUES (?,?,?,?,?)",
        (acc_num, txn_type, amount, other_acc, timestamp),
        commit=True
    )

# ── GUI Styles ──────────────────────────────────────────────────
class AppStyle:
    BG = "#f0f2f5"
    PRIMARY = "#1a73e8"
    SECONDARY = "#5f6368"
    SUCCESS = "#0f9d58"
    DANGER = "#ea4335"
    CARD_BG = "#ffffff"

    @classmethod
    def apply(cls):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(".", font=("Segoe UI", 10), background=cls.BG)
        style.configure("TFrame", background=cls.BG)
        style.configure("TLabel", background=cls.BG, foreground=cls.SECONDARY)
        style.configure("Header.TLabel", font=("Segoe UI", 18, "bold"), foreground=cls.PRIMARY)
        style.configure("Balance.TLabel", font=("Segoe UI", 26, "bold"), foreground="#202124")
        style.configure("TButton", font=("Segoe UI", 10, "bold"), background=cls.PRIMARY)
        style.map("TButton",
                  background=[("active", cls.PRIMARY), ("disabled", "#c4c7cc")],
                  foreground=[("active", "white")])
        style.configure("Accent.TButton", background=cls.PRIMARY, foreground="white")
        style.map("Accent.TButton", background=[("active", "#1557b0")])
        style.configure("Danger.TButton", background=cls.DANGER, foreground="white")
        style.map("Danger.TButton", background=[("active", "#c5221f")])
        style.configure("TEntry", padding=6)
        style.configure("Treeview", rowheight=25, font=("Segoe UI", 9))
        style.configure("Treeview.Heading", font=("Segoe UI", 9, "bold"))

# ── Main Application ────────────────────────────────────────────
class BankingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Banking Management System")
        self.geometry("900x600")
        self.resizable(False, False)
        AppStyle.apply()
        self.current_user = None   # (acc_num, name)
        self.container = tk.Frame(self, bg=AppStyle.BG)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (LoginFrame, RegisterFrame, DashboardFrame, AdminFrame):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame("LoginFrame")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        # Refresh data when switching to Dashboard or Admin
        if page_name == "DashboardFrame":
            frame.load_data()
        elif page_name == "AdminFrame":
            frame.refresh()

    def login(self, acc_num, pin):
        user = execute_query(
            "SELECT acc_num, name, pin_hash FROM accounts WHERE acc_num=?",
            (acc_num,), fetch=True
        )
        if user and user[0][2] == hash_pin(pin):
            self.current_user = (user[0][0], user[0][1])
            if acc_num == "ADMIN":
                self.show_frame("AdminFrame")
            else:
                self.show_frame("DashboardFrame")
        else:
            messagebox.showerror("Login Failed", "Invalid account number or PIN.")

    def logout(self):
        self.current_user = None
        self.show_frame("LoginFrame")

# ── Login Frame ─────────────────────────────────────────────────
class LoginFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg=AppStyle.BG)

        # Center card
        card = tk.Frame(self, bg=AppStyle.CARD_BG, bd=0, highlightthickness=1,
                        highlightbackground="#dadce0")
        card.place(relx=0.5, rely=0.5, anchor="center", width=380, height=350)

        ttk.Label(card, text="Welcome to BMS", style="Header.TLabel",
                  background=AppStyle.CARD_BG).pack(pady=(30, 10))
        ttk.Label(card, text="Account Number", background=AppStyle.CARD_BG).pack(anchor="w", padx=40)
        self.acc_entry = ttk.Entry(card, width=30)
        self.acc_entry.pack(padx=40, pady=(0, 10))

        ttk.Label(card, text="PIN", background=AppStyle.CARD_BG).pack(anchor="w", padx=40)
        self.pin_entry = ttk.Entry(card, show="*", width=30)
        self.pin_entry.pack(padx=40, pady=(0, 20))

        ttk.Button(card, text="Login", style="Accent.TButton",
                   command=self.handle_login).pack(pady=5)
        ttk.Button(card, text="Create New Account",
                   command=lambda: controller.show_frame("RegisterFrame")).pack()

    def handle_login(self):
        acc = self.acc_entry.get().strip()
        pin = self.pin_entry.get().strip()
        if not acc or not pin:
            messagebox.showwarning("Missing Info", "Please enter both fields.")
            return
        self.controller.login(acc, pin)

# ── Register Frame ──────────────────────────────────────────────
class RegisterFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg=AppStyle.BG)

        card = tk.Frame(self, bg=AppStyle.CARD_BG, bd=0, highlightthickness=1,
                        highlightbackground="#dadce0")
        card.place(relx=0.5, rely=0.5, anchor="center", width=380, height=400)

        ttk.Label(card, text="Create Account", style="Header.TLabel",
                  background=AppStyle.CARD_BG).pack(pady=(30, 10))

        ttk.Label(card, text="Full Name", background=AppStyle.CARD_BG).pack(anchor="w", padx=40)
        self.name_entry = ttk.Entry(card, width=30)
        self.name_entry.pack(padx=40, pady=(0, 10))

        ttk.Label(card, text="PIN (4-6 digits)", background=AppStyle.CARD_BG).pack(anchor="w", padx=40)
        self.pin_entry = ttk.Entry(card, show="*", width=30)
        self.pin_entry.pack(padx=40, pady=(0, 10))

        ttk.Label(card, text="Initial Deposit", background=AppStyle.CARD_BG).pack(anchor="w", padx=40)
        self.dep_entry = ttk.Entry(card, width=30)
        self.dep_entry.pack(padx=40, pady=(0, 20))

        ttk.Button(card, text="Register", style="Accent.TButton",
                   command=self.register).pack(pady=5)
        ttk.Button(card, text="Back to Login",
                   command=lambda: controller.show_frame("LoginFrame")).pack()

    def register(self):
        name = self.name_entry.get().strip()
        pin = self.pin_entry.get().strip()
        dep = self.dep_entry.get().strip()

        if not name or not pin:
            messagebox.showwarning("Missing Info", "Name and PIN are required.")
            return
        if not pin.isdigit() or len(pin) < 4 or len(pin) > 6:
            messagebox.showwarning("Invalid PIN", "PIN must be 4-6 digits.")
            return
        try:
            deposit = float(dep) if dep else 0.0
        except ValueError:
            messagebox.showwarning("Invalid Amount", "Enter a valid deposit amount.")
            return

        acc_num = generate_account_number()
        pin_hash = hash_pin(pin)
        execute_query(
            "INSERT INTO accounts (acc_num, name, pin_hash, balance) VALUES (?,?,?,?)",
            (acc_num, name, pin_hash, deposit), commit=True
        )
        if deposit > 0:
            record_transaction(acc_num, "Initial Deposit", deposit)
        messagebox.showinfo("Account Created",
                            f"Your Account Number: {acc_num}\nPlease save it securely.")
        self.controller.show_frame("LoginFrame")
        self.name_entry.delete(0, "end")
        self.pin_entry.delete(0, "end")
        self.dep_entry.delete(0, "end")

# ── Dashboard Frame ─────────────────────────────────────────────
class DashboardFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg=AppStyle.BG)

        # Top bar
        top = tk.Frame(self, bg=AppStyle.PRIMARY, height=50)
        top.pack(fill="x")
        ttk.Label(top, text="Banking Management System", font=("Segoe UI", 14, "bold"),
                  background=AppStyle.PRIMARY, foreground="white").pack(side="left", padx=20, pady=10)
        self.user_label = ttk.Label(top, text="", background=AppStyle.PRIMARY, foreground="white")
        self.user_label.pack(side="right", padx=20, pady=10)
        ttk.Button(top, text="Logout", command=controller.logout).pack(side="right", padx=10)

        # Balance card
        bal_card = tk.Frame(self, bg=AppStyle.CARD_BG, bd=0, highlightthickness=1,
                            highlightbackground="#dadce0")
        bal_card.pack(pady=20, padx=30, fill="x")
        ttk.Label(bal_card, text="Available Balance", background=AppStyle.CARD_BG,
                  foreground=AppStyle.SECONDARY).pack(anchor="w", padx=20, pady=(10, 0))
        self.balance_label = ttk.Label(bal_card, text="$0.00", style="Balance.TLabel",
                                       background=AppStyle.CARD_BG)
        self.balance_label.pack(anchor="w", padx=20, pady=(0, 10))

        # Action buttons
        btn_frame = tk.Frame(self, bg=AppStyle.BG)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Deposit", style="Accent.TButton",
                   command=self.deposit).grid(row=0, column=0, padx=10)
        ttk.Button(btn_frame, text="Withdraw", style="Accent.TButton",
                   command=self.withdraw).grid(row=0, column=1, padx=10)
        ttk.Button(btn_frame, text="Transfer", style="Accent.TButton",
                   command=self.transfer).grid(row=0, column=2, padx=10)

        # Transaction history
        hist_frame = tk.Frame(self, bg=AppStyle.BG)
        hist_frame.pack(pady=20, padx=30, fill="both", expand=True)
        ttk.Label(hist_frame, text="Recent Transactions", font=("Segoe UI", 12, "bold"),
                  background=AppStyle.BG).pack(anchor="w")
        columns = ("date", "type", "amount", "other")
        self.tree = ttk.Treeview(hist_frame, columns=columns, show="headings", height=8)
        self.tree.heading("date", text="Date")
        self.tree.heading("type", text="Type")
        self.tree.heading("amount", text="Amount")
        self.tree.heading("other", text="Recipient/Source")
        self.tree.column("date", width=150)
        self.tree.column("type", width=120)
        self.tree.column("amount", width=100)
        self.tree.column("other", width=150)
        self.tree.pack(fill="both", expand=True)

    def load_data(self):
        acc_num = self.controller.current_user[0]
        name = self.controller.current_user[1]
        self.user_label.config(text=f"{name} ({acc_num})")
        bal = execute_query("SELECT balance FROM accounts WHERE acc_num=?", (acc_num,), fetch=True)
        if bal:
            self.balance_label.config(text=f"${bal[0][0]:,.2f}")
        # Clear and reload tree
        for item in self.tree.get_children():
            self.tree.delete(item)
        txns = execute_query(
            "SELECT timestamp, type, amount, other_acc FROM transactions WHERE acc_num=? ORDER BY id DESC LIMIT 20",
            (acc_num,), fetch=True
        )
        for t in txns:
            self.tree.insert("", "end", values=t)

    def deposit(self):
        self._amount_dialog("Deposit", "deposit")

    def withdraw(self):
        self._amount_dialog("Withdraw", "withdraw")

    def transfer(self):
        dialog = tk.Toplevel(self)
        dialog.title("Transfer Funds")
        dialog.geometry("350x220")
        dialog.configure(bg=AppStyle.CARD_BG)
        dialog.grab_set()

        ttk.Label(dialog, text="Recipient Account", background=AppStyle.CARD_BG).pack(pady=(15, 5))
        acc_entry = ttk.Entry(dialog, width=25)
        acc_entry.pack()
        ttk.Label(dialog, text="Amount", background=AppStyle.CARD_BG).pack(pady=(10, 5))
        amt_entry = ttk.Entry(dialog, width=25)
        amt_entry.pack()

        def submit():
            recipient = acc_entry.get().strip()
            amt_str = amt_entry.get().strip()
            if not recipient or not amt_str:
                return
            try:
                amount = float(amt_str)
            except ValueError:
                messagebox.showwarning("Invalid", "Enter a valid amount.")
                return
            acc_num = self.controller.current_user[0]
            # Check balance
            bal = execute_query("SELECT balance FROM accounts WHERE acc_num=?", (acc_num,), fetch=True)[0][0]
            if amount <= 0 or amount > bal:
                messagebox.showwarning("Error", "Insufficient funds or invalid amount.")
                return
            # Check recipient exists
            rec = execute_query("SELECT acc_num FROM accounts WHERE acc_num=?", (recipient,), fetch=True)
            if not rec or recipient == acc_num:
                messagebox.showwarning("Error", "Invalid recipient account.")
                return
            # Perform transfer
            execute_query("UPDATE accounts SET balance=balance-? WHERE acc_num=?", (amount, acc_num), commit=True)
            execute_query("UPDATE accounts SET balance=balance+? WHERE acc_num=?", (amount, recipient), commit=True)
            record_transaction(acc_num, "Transfer Out", amount, recipient)
            record_transaction(recipient, "Transfer In", amount, acc_num)
            messagebox.showinfo("Success", "Transfer completed.")
            dialog.destroy()
            self.load_data()

        ttk.Button(dialog, text="Transfer", style="Accent.TButton", command=submit).pack(pady=20)

    def _amount_dialog(self, title, action):
        dialog = tk.Toplevel(self)
        dialog.title(title)
        dialog.geometry("300x180")
        dialog.configure(bg=AppStyle.CARD_BG)
        dialog.grab_set()

        ttk.Label(dialog, text=f"Enter amount to {action}", background=AppStyle.CARD_BG).pack(pady=(20, 10))
        amount_entry = ttk.Entry(dialog, width=20)
        amount_entry.pack()

        def submit():
            amt = amount_entry.get().strip()
            try:
                amount = float(amt)
            except ValueError:
                messagebox.showwarning("Invalid", "Enter a valid number.")
                return
            if amount <= 0:
                messagebox.showwarning("Invalid", "Amount must be positive.")
                return
            acc_num = self.controller.current_user[0]
            if action == "withdraw":
                bal = execute_query("SELECT balance FROM accounts WHERE acc_num=?", (acc_num,), fetch=True)[0][0]
                if amount > bal:
                    messagebox.showwarning("Error", "Insufficient balance.")
                    return
                execute_query("UPDATE accounts SET balance=balance-? WHERE acc_num=?", (amount, acc_num), commit=True)
                record_transaction(acc_num, "Withdraw", amount)
            else:  # deposit
                execute_query("UPDATE accounts SET balance=balance+? WHERE acc_num=?", (amount, acc_num), commit=True)
                record_transaction(acc_num, "Deposit", amount)
            messagebox.showinfo("Success", f"{title} of ${amount:.2f} completed.")
            dialog.destroy()
            self.load_data()

        ttk.Button(dialog, text="Confirm", style="Accent.TButton", command=submit).pack(pady=20)

# ── Admin Frame ─────────────────────────────────────────────────
class AdminFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg=AppStyle.BG)

        top = tk.Frame(self, bg="#202124", height=50)
        top.pack(fill="x")
        ttk.Label(top, text="Admin Panel", font=("Segoe UI", 14, "bold"),
                  background="#202124", foreground="white").pack(side="left", padx=20, pady=10)
        ttk.Button(top, text="Logout", command=controller.logout).pack(side="right", padx=10, pady=10)

        tree_frame = tk.Frame(self, bg=AppStyle.BG)
        tree_frame.pack(padx=30, pady=20, fill="both", expand=True)
        columns = ("acc_num", "name", "balance")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=15)
        self.tree.heading("acc_num", text="Account Number")
        self.tree.heading("name", text="Name")
        self.tree.heading("balance", text="Balance")
        self.tree.column("acc_num", width=180)
        self.tree.column("name", width=200)
        self.tree.column("balance", width=150)
        self.tree.pack(fill="both", expand=True)

        ttk.Button(self, text="Refresh", command=self.refresh).pack(pady=10)

    def refresh(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        accounts = execute_query("SELECT acc_num, name, balance FROM accounts WHERE acc_num != 'ADMIN'", fetch=True)
        for acc in accounts:
            self.tree.insert("", "end", values=acc)

# ── Run Application ─────────────────────────────────────────────
if __name__ == "__main__":
    init_db()
    app = BankingApp()
    app.mainloop()