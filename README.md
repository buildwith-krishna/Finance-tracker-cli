<div align="center">

# 💰 Finance Tracker CLI

### *Know where every rupee goes.*

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20Windows-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active%20Development-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)
![Built On](https://img.shields.io/badge/Built%20On-Android%20Phone-red?style=for-the-badge&logo=android)

<br/>

> **A terminal-based personal finance tracker built in Python.**
> Track expenses, manage income, and take control of your money — right from your terminal.

<br/>

*Built entirely on Termux. No PC. No excuses.* 📱⚡

---

</div>

## 👨‍💻 Author

<table>
  <tr>
    <td align="center">
      <strong>Krishna Pandey</strong><br/>
      <sub>Aspiring Backend Developer | Python | CLI Tools | Termux</sub><br/><br/>
      <a href="https://github.com/buildwith-krishna">🐙 GitHub</a> •
      <a href="https://linkedin.com/in/krishnapandey">💼 LinkedIn</a>
    </td>
  </tr>
</table>

> *"Consistent progress > temporary motivation"* ⭐

---

## 🚧 Project Status

```
🟢 Active Development — Part of #100DaysOfCode Journey
```

This project is being built **live and in public** — every commit is a real step forward.
Watch the repo to follow the journey. 👀

---

## ✨ Features

| Status | Feature |
|--------|---------|
| ✅ Done | Add expense with amount, type, category, note |
| ✅ Done | Auto datetime stamp for every entry |
| ✅ Done | JSON persistence — data never lost |
| ✅ Done | Multi-file modular architecture |
| ✅ Done | View all transactions (income + expenses) |
| ✅ Done | Separated main.py entry point with full menu |
| ✅ Done | Add income tracking |
| 🔨 Building | Check current balance |
| 🔨 Building | Delete wrong entries |
| 📋 Planned | Monthly summary report |
| 📋 Planned | Category-wise breakdown |
| 📋 Planned | Budget limit warnings |
| 📋 Planned | FastAPI backend (Phase 2) |
| 📋 Planned | Web frontend (Phase 3) |

---

## 📁 Project Structure

```
finance_tracker/
│
├── 📄 main.py        ← Entry point — runs the app
├── 📄 tracker.py     ← Core logic and all functions
├── 📄 storage.py     ← JSON read/write operations
├── 📄 config.py      ← Constants and configuration
└── 📄 utils.py       ← Helper functions
```

---

## 🗃️ Data Structure

Every transaction is stored with a unique datetime key:

```json
{
    "2026-04-27 13:45:22": {
        "Type": "expense",
        "Amount": 899,
        "Category": "clothing",
        "Note": "bought new shirt"
    },
    "2026-04-27 14:00:10": {
        "Type": "income",
        "Amount": 45600
    }
}
```

---

## ▶️ How to Run

**Clone the repo:**
```bash
git clone https://github.com/buildwith-krishna/Finance-tracker-cli.git
cd Finance-tracker-cli
```

**Run the app:**
```bash
python main.py
```

**Requirements:**
```
Python 3.x
No external libraries needed — pure standard library
```

---

## 🗺️ Roadmap

```
Phase 1 — CLI (Current)
    ✅ Core expense and income tracking
    ✅ View all transactions
    ✅ Separated main.py entry point
    🔨 Full CRUD operations
    📋 Reports and summaries

Phase 2 — API (July 2026)
    📋 FastAPI backend
    📋 SQLite database
    📋 REST endpoints

Phase 3 — Full Stack (Sep 2026)
    📋 Web frontend
    📋 Dashboard with charts
    📋 Deploy online
```

---

## 💡 About This Project

This isn't just a finance tracker.

It's proof that **constraints don't stop progress.**

Built on a **Moto G72 phone** using **Termux** — no laptop, no fancy setup, no excuses. Just Python, determination, and a ceiling fan in 43° heat. 🌡️

Every line of code in this repo was written on a touchscreen keyboard.

---

## 📊 Part of My Journey

This is **Project #4** in my #100DaysOfCode challenge.

Previous projects:
- 📒 [Notes App CLI](https://github.com/buildwith-krishna/notes-app)
- 🔐 [Password Manager CLI](https://github.com/buildwith-krishna/password-manager-cli)
- 📇 [Contact Book CLI](https://github.com/buildwith-krishna/Contact-book-CLI)

---

<div align="center">

**If this project helped or inspired you, drop a ⭐ — it means a lot!**

*Made with 💪 and way too much determination by Krishna Pandey*

</div>
