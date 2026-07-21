{# 🏦 Banking Management System

A secure, desktop-based Banking Management System built with Python, Tkinter, and SQLite.  
Developed as an academic project for **Brainware University** to demonstrate practical software engineering skills.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📑 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [System Architecture](#-system-architecture)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
- [Project Structure](#-project-structure)
- [Screenshots](#-screenshots)
- [Team & Roles](#-team--roles)
- [Project Roadmap](#-project-roadmap)
- [Risk Management](#-risk-management)
- [Tools & Resources](#-tools--resources)
- [Future Enhancements](#-future-enhancements)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)

---

## ✨ Features

- **User Account Management** – Register with auto-generated 10-digit account number.
- **Secure Login** – PIN hashed with SHA-256, no plain-text storage.
- **Dashboard** – Real-time balance, transaction history, quick actions.
- **Transactions**
  - Deposit money
  - Withdraw money (with balance validation)
  - Transfer funds to other accounts instantly
- **Admin Panel** – View all customer accounts and balances (password protected).
- **Transaction Logs** – Complete audit trail of every financial activity.
- **Modern GUI** – Clean, responsive interface built with themed `ttk` widgets.
- **Data Persistence** – SQLite database ensures data survives app restarts.

---

## 🛠 Tech Stack

| Layer        | Technology               |
|--------------|--------------------------|
| Language     | Python 3                  |
| GUI Library  | Tkinter (ttk)            |
| Database     | SQLite3                  |
| Security     | SHA-256 hashing          |
| Version Control | Git & GitHub (planned) |

---

## 🧱 System Architecture
[ User / Admin ]
│
▼
┌─────────────────┐
│ Tkinter GUI │ (Login, Register, Dashboard, Admin Panel)
└────────┬────────┘
│
┌────────▼────────┐
│ Logic Layer │ (Authentication, Transaction Processing)
└────────┬────────┘
│
┌────────▼────────┐
│ SQLite DB │ (accounts, transactions tables)
└─────────────────┘

text

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher (Tkinter and SQLite are included by default)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/banking-management-system.git
   cd banking-management-system
Run the application

bash
python main.py
No additional dependencies are required.

Initialise the database
The database bank.db is created automatically on the first run.
Default admin credentials:

Account Number: ADMIN

PIN: admin123

📘 Usage Guide
1. New User Registration
Click "Create New Account" on the login screen.

Enter your full name, a 4-6 digit PIN, and an optional initial deposit.

Save the auto-generated account number displayed after registration – you will need it to log in.

2. Login
Enter your account number and PIN.

Regular users are taken to the Dashboard; the admin account (ADMIN) opens the Admin Panel.

3. Dashboard
Balance is displayed at the top.

Deposit / Withdraw: Enter amount and confirm.

Transfer: Provide the recipient's account number and amount.
(Both accounts' balances are updated atomically.)

Transaction History: The last 20 transactions are shown in a table.

4. Admin Panel
Lists all non-admin accounts with their current balances.

Use the Refresh button to reload data.

📁 Project Structure
text
banking-management-system/
│
├── main.py                # Entry point – launches the application
├── bank.db                # SQLite database file (auto-generated)
├── README.md              # Project documentation
└── screenshots/           # (Optional) UI screenshots
The entire application is modularised within main.py using classes for each frame.

📸 Screenshots
Add your actual screenshots here. Suggested captures:

Screen	Placeholder
Login Screen	https://screenshots/login.png
Registration	https://screenshots/register.png
Dashboard	https://screenshots/dashboard.png
Transfer Dialog	https://screenshots/transfer.png
Admin Panel	https://screenshots/admin.png
👥 Team & Roles
Team Member	Role(s)
Ramdas Hembram	Project Manager, Backend Developer, Database Developer, Documentation Lead
Aditto Rudra	Frontend/UI Developer, Testing & Quality Assurance
Brainware University – Department of Computer Science

🗓 Project Roadmap
The following roadmap was followed over an 8‑week development cycle:

Phase 1: Initiation & Planning (Week 1)
Define project scope and functional requirements

Deliverable: Project proposal document

Lead: Ramdas (PM)

Phase 2: UI/UX Design (Week 2)
Sketch wireframes for Login, Dashboard, Admin Panel

Choose colour scheme and widget styles (AppStyle class)

Deliverable: Wireframe diagrams

Lead: Aditto

Phase 3: Database & Backend Core (Weeks 3‑4)
Design database schema (accounts, transactions tables)

Implement helper functions (hash PIN, generate account number, record transactions)

Deliverable: SQL script & backend module

Lead: Ramdas

Phase 4: Frontend Integration (Weeks 5‑6)
Build all GUI frames (Login, Register, Dashboard, Admin) – Aditto

Connect frontend to backend logic – Ramdas & Aditto (pair work)

Deliverable: Fully functional prototype

Dependency: Backend core must be completed

Phase 5: Testing & Quality Assurance (Week 7)
Unit testing (manual) for edge cases (negative amounts, invalid accounts)

UI responsiveness and error handling checks

Security review (PIN hashing, SQL injection prevention)

Deliverable: Test report

Lead: Aditto

Phase 6: Documentation & Presentation (Week 8)
Finalise project report (SRS, design, testing) – Ramdas

Prepare presentation slides and live demo script

Record a demo video if required

Deliverable: Final report & presentation

Lead: Ramdas

⚠️ Risk Management
Risk	Mitigation Strategy
Loss of database file (bank.db)	Regular backups; include DB creation script
PIN/security vulnerabilities	Use SHA-256 hashing; never store raw PIN
Team member unavailability	Cross‑skill tasks; clear documentation
Integration issues (frontend ↔ backend)	Daily sync meetings; frequent integration tests
🧰 Tools & Resources
Communication: WhatsApp / Discord

Version Control: Git & GitHub

Design / Wireframing: Figma or pen & paper

Testing: Manual test cases, Python's unittest (optional extension)

Documentation: Microsoft Word / Google Docs for report, Markdown for README

🔮 Future Enhancements
Add password recovery via security questions.

Export transaction history to CSV/PDF.

Implement interest calculation for savings accounts.

Introduce a loan/credit module.

Deploy as a web application using Flask/Django.

📄 License
This project is licensed under the MIT License – see the LICENSE file for details (if added).

🙏 Acknowledgements
Brainware University for providing the academic platform.

Python and Tkinter communities for excellent documentation.

Our faculty guide for continuous support and feedback.

}