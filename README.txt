# Murphy Bank Simulator — CSC 221 Final Project (Intro to Problem Solving and Programming)

## Overview

**Murphy Bank Simulator** is the final project for **CSC 221: Intro to Problem Solving and Programming**.  
This Python program simulates a simple banking system, allowing users to:

- Create a bank account with a secure password
- Deposit and withdraw funds
- Transfer money between accounts
- Check account balances

The project demonstrates core programming concepts learned in CSC 221, including control flow, functions, classes, error handling, and working with Python's `decimal` module for precise monetary calculations.

This project was implemented by **Edward Murphy**.

---

## Features

- Create new bank accounts with owner name, password, and initial deposit  
- Secure login system for multiple accounts  
- Deposit and withdraw funds with validation  
- Transfer funds between accounts  
- Transaction history stored per account  
- Clear console menus for a smooth user experience  

---

## Getting Started

### Prerequisites

- Python 3.x installed on your system  
- No external packages required  

You can check your Python version with:

```bash
python --version

---

## Installation & Running

git clone https://github.com/EddieM30/Murphy_Edward_Final_Project.git
cd Murphy_Edward_Final_Project

python main.py

---

### Usage Example

### Creating an account

$ python main.py
Welcome to Murphy
1. Create new account
2. Log in to account
3. Exit
> 1

Enter your name: Edward
Password: ******

Deposit ($00.00): $500.00

Edward successfully created an account with an initial deposit of: $500.00

Press enter to continue...


### Logging in and managing funds

1. Deposit
2. Withdraw
3. Transfer
4. Show Balance
5. Logout
> 1

How much would you like to deposit?
$250.00

Deposit successful! New balance: $750.00

---

### Code Structure

main.py — Entry point of the program; starts the main menu
screens.py — Handles all user interface menus and interactions
bank_account.py — Contains the BankAccount class with deposit, withdraw, transfer, and validation methods
accounts.py — Stores current accounts and the logged-in account
utils.py — Helper functions, e.g., clearing the console and handling input errors

### What I Learned

- This project helped me practice:

- Object-oriented programming with Python classes

- Handling user input and validation

- Implementing secure login and account management

- Designing a text-based user interface

- Applying precise arithmetic with Python’s decimal module

### Author

Edward Murphy
GitHub: https://github.com/EddieM30

### License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this code, as long as you include this license notice in all copies or substantial portions of the software.