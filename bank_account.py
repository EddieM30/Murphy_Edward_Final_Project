import utils
from decimal import Decimal, InvalidOperation


class BankAccount:

    """Represents a single bank account with secure password and precise Decimal balance. 
    All monetary values use Decimal to avoid floating-point errors."""

    def __init__(self, owner, balance=0.0, password=""):

        self.owner = owner.strip().title()  # john DOE -> John Doe
        self.balance = Decimal(str(balance)).quantize(Decimal('0.01'))
        self.password = password
        self.acc_number = None
        self.route_number = None
        self.transaction_history = {}

    def deposit(self, amount: Decimal) -> None:
        """deposits money into account"""
        utils.clear_console()
        try:
            if amount <= 0:
                input('Declined. Not enough for a deposit\nPress enter to continue...')
            elif amount > 0:
                print(f'Previous Balance: ${self.balance:,.2f}')
                self.balance += amount
                print(f'Current Balance: ${self.balance:,.2f}')
                input('\nPress enter to continue...')
        except ValueError:
            utils.val_error()

    def withdraw(self, amount: Decimal) -> None:
        '''withdraw money from account'''
        utils.clear_console()
        try:
            if amount > self.balance:
                input(
                    "Sorry, you don't have the funds for this withdraw.\nPress enter to continue...")
            if amount <= self.balance:
                print(f'Previous balance: ${self.balance:,.2f}')
                self.balance -= amount
                print(f'Current Balance: ${self.balance:,.2f}')
                input('\nPress enter to continue...')
        except ValueError:
            utils.val_error()

    def transfer(self, name, accounts, amount: Decimal) -> None:
        '''transfer money amongst bank account objects'''
        if amount > self.balance or amount <= 0:
            input('Insufficient funds.\nPress enter to continue...')
            return False

        for account in accounts:
            if name.lower() == account.owner.lower():
                self.balance -= amount
                account.balance += amount
                return True
        return False

    def show_balance(self):
        '''Print owner and current balance'''
        print(f'{self.owner}\'s current balance is: {self.balance:,.2f}')
        input('Press enter to continue...')

    def print_account(self):
        print(
            f'\n{self.owner} successfully created an account with an initial deposit of: ${self.balance:,.2f}\n')

    def validate_money(self, amount: str) -> Decimal | None:
        '''takes string input for deposit, withdraw and transfer 
        and validates it. only accepts 2 decimal values, 
        then turns it into a float if possible'''
        if '.' in amount:
            whole, cents = amount.split('.')
            if len(cents) > 2:
                print('Cents cannot have a greater value than .99')
                input('Press enter to continue...')
                return None

        try:
            amount = Decimal(amount)
            if amount < 0:
                print('Negative amounts not allowed.')
                input('Press enter to continue...')
                return None
            return amount.quantize(Decimal('0.01'))
        except InvalidOperation:
            print(
                'Please only use numbers, decimals, and commas when entering a deposit.')
            input('Press enter to continue...')
            return None
