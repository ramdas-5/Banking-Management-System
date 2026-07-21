# 🏦 Banking Management System

<div align="center">

### 💳 Secure Desktop Banking Application

*A modern Banking Management System built with **Python**, **Tkinter**, and **SQLite**.*

Developed as an academic project for **Brainware University** to demonstrate practical **Software Engineering**, **Database Management**, and **GUI Application Development** skills.

<br>

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-FF8C00?style=for-the-badge)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite)
![MIT License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)
![Brainware University](https://img.shields.io/badge/Brainware-University-blueviolet?style=for-the-badge)

</div>

---

# 📚 Table of Contents

- [✨ Features](#-features)
- [🛠 Tech Stack](#-tech-stack)
- [🏗 System Architecture](#-system-architecture)
- [🚀 Installation](#-installation)
- [📖 Usage Guide](#-usage-guide)
- [📂 Project Structure](#-project-structure)
- [📸 Screenshots](#-screenshots)
- [👥 Team & Roles](#-team--roles)
- [🗓 Development Roadmap](#-development-roadmap)
- [⚠ Risk Management](#-risk-management)
- [🧰 Tools & Resources](#-tools--resources)
- [🔮 Future Enhancements](#-future-enhancements)
- [📄 License](#-license)
- [🙏 Acknowledgements](#-acknowledgements)

---

# ✨ Features

### 👤 Account Management
- Create a new bank account
- Auto-generated **10-digit Account Number**
- Secure PIN registration

### 🔐 Authentication
- Secure Login System
- PIN encrypted using **SHA-256**
- No plain-text password storage

### 💰 Banking Operations
- Deposit Money
- Withdraw Money
- Fund Transfer
- Balance Validation
- Real-time Balance Updates

### 📊 Dashboard
- Current Balance
- Recent Transactions
- Quick Banking Actions

### 🛡 Admin Panel
- View all customer accounts
- Monitor balances
- Password-protected access

### 📝 Transaction History
- Complete audit trail
- Deposit records
- Withdraw records
- Transfer records

### 🎨 User Interface
- Modern Tkinter UI
- Responsive Layout
- ttk Widgets
- Easy Navigation

### 💾 Database
- SQLite Database
- Automatic Data Saving
- Persistent Storage

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| 💻 Language | Python 3 |
| 🖥 GUI | Tkinter (ttk) |
| 🗄 Database | SQLite3 |
| 🔒 Security | SHA-256 Hashing |
| 📦 Version Control | Git & GitHub *(Planned)* |

---

# 🏗 System Architecture

```text
                    ┌────────────────────┐
                    │    User / Admin    │
                    └─────────┬──────────┘
                              │
                              ▼
               ┌────────────────────────────┐
               │        Tkinter GUI         │
               │                            │
               │ • Login                    │
               │ • Registration             │
               │ • Dashboard                │
               │ • Admin Panel              │
               └────────────┬───────────────┘
                            │
                            ▼
               ┌────────────────────────────┐
               │      Business Logic        │
               │                            │
               │ • Authentication           │
               │ • Transactions             │
               │ • Validation               │
               │ • Account Management       │
               └────────────┬───────────────┘
                            │
                            ▼
               ┌────────────────────────────┐
               │       SQLite Database      │
               │                            │
               │ • accounts                 │
               │ • transactions             │
               └────────────────────────────┘
```

---

# 🚀 Installation

## Prerequisites

- Python **3.8+**
- Tkinter *(Included with Python)*
- SQLite *(Included with Python)*

---

## Clone Repository

```bash
git clone https://github.com/your-username/banking-management-system.git

cd banking-management-system
```

---

## Run Application

```bash
python main.py
```

No additional packages are required.

---

## Database

The SQLite database (`bank.db`) is automatically created during the first run.

### Default Admin Login

| Field | Value |
|-------|-------|
| Account Number | `ADMIN` |
| PIN | `admin123` |

---

# 📖 Usage Guide

## 👤 1. Register

- Click **Create New Account**
- Enter Full Name
- Create a 4–6 digit PIN
- Optional Initial Deposit
- Save the generated Account Number

---

## 🔐 2. Login

Enter:

- Account Number
- PIN

### Access

| User Type | Destination |
|-----------|-------------|
| Customer | Dashboard |
| ADMIN | Admin Panel |

---

## 💰 3. Dashboard

Available Operations

- Deposit Money
- Withdraw Money
- Transfer Money
- View Balance
- Transaction History

The latest **20 transactions** are displayed.

---

## 🛡 4. Admin Panel

Administrator can:

- View all accounts
- View balances
- Refresh account list

---

# 📂 Project Structure

```text
banking-management-system/
│
├── main.py
│   └── Main Application
│
├── bank.db
│   └── SQLite Database (Auto Generated)
│
├── README.md
│   └── Documentation
│
└── screenshots/
    ├── login.png
    ├── register.png
    ├── dashboard.png
    ├── transfer.png
    └── admin.png
```

---

# 📸 Screenshots

| Screen | Image |
|---------|-------|
| Login | screenshots/login.png |
| Register | screenshots/register.png |
| Dashboard | screenshots/dashboard.png |
| Transfer | screenshots/transfer.png |
| Admin Panel | screenshots/admin.png |

> *(Replace with actual screenshots.)*

---

# 👥 Team & Roles

| Team Member | Responsibilities |
|--------------|------------------|
| **Ramdas Hembram** | Project Manager • Backend Developer • Database Developer • Documentation Lead |
| **Aditto Rudra** | Frontend Developer • UI Designer • Testing & Quality Assurance |

### 🎓 Institution

**Brainware University**

Department of Computer Science & Engineering

---

# 🗓 Development Roadmap

## 📌 Phase 1 — Project Planning *(Week 1)*

✔ Requirement Analysis

✔ Project Scope

✔ Proposal Documentation

**Lead:** Ramdas

---

## 🎨 Phase 2 — UI/UX Design *(Week 2)*

✔ Wireframes

✔ Login Design

✔ Dashboard Design

✔ Admin Panel Design

**Lead:** Aditto

---

## 🗄 Phase 3 — Backend Development *(Weeks 3–4)*

✔ Database Design

✔ Account Module

✔ Transaction Module

✔ PIN Encryption

**Lead:** Ramdas

---

## 🖥 Phase 4 — Frontend Integration *(Weeks 5–6)*

✔ GUI Development

✔ Backend Integration

✔ Functional Prototype

**Lead:** Ramdas & Aditto

---

## 🧪 Phase 5 — Testing *(Week 7)*

✔ Manual Testing

✔ Error Handling

✔ Security Validation

✔ Transaction Testing

**Lead:** Aditto

---

## 📑 Phase 6 — Documentation *(Week 8)*

✔ Report

✔ Presentation

✔ Live Demo

✔ Final Submission

**Lead:** Ramdas

---

# ⚠ Risk Management

| Risk | Mitigation |
|------|------------|
| Database Loss | Regular Backup |
| PIN Vulnerability | SHA-256 Encryption |
| Team Availability | Shared Knowledge |
| Integration Issues | Frequent Testing |

---

# 🧰 Tools & Resources

### 💬 Communication

- WhatsApp
- Discord

### 💻 Development

- Python
- Tkinter
- SQLite

### 📦 Version Control

- Git
- GitHub

### 🎨 Design

- Pen & Paper

### 🧪 Testing

- Manual Testing
- unittest *(Optional)*

### 📄 Documentation

- Microsoft Word
- Google Docs
- Markdown

---

# 🔮 Future Enhancements

- 🔐 Password Recovery
- 📄 Export Transaction History (PDF/CSV)
- 💹 Savings Interest Calculator
- 💳 Loan Management Module
- 🌐 Flask/Django Web Version
- ☁ Cloud Database Integration
- 📱 Mobile Application
- 📊 Financial Analytics Dashboard

---

# 📄 License

This project is licensed under the **MIT License**.

See the **LICENSE** file for more information.

---

# 🙏 Acknowledgements

Special thanks to:

- 🎓 Brainware University
- 🐍 Python Community
- 🖥 Tkinter Community
- 👨‍🏫 Our Faculty Guide
- ❤️ Everyone who contributed to this project

---

<div align="center">

## ⭐ If you found this project helpful, consider giving it a star!

**Made with ❤️ using Python**

</div>