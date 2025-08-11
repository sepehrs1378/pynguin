from datetime import date

# Sleeps should be in the form of BASE_SLEEP * X.
BASE_SLEEP = 1


class Customer:
    def __init__(self, name: str, address: str, phone: str) -> None:
        self.name: str = name
        self.address: str = address
        self.phone: str = phone
        self.accounts: list[Account] = []

    def change_address(self, new_address: str) -> bool:
        pass

    def add_account(self, account: Account) -> None:
        pass


class Account:
    def __init__(self, id_: int, customer: Customer) -> None:
        self.id = id_
        self.balance: int = 0
        self.opening_date: date = date.today()
        self.is_open: bool = True
        self.customer: Customer = customer

    def deposit(self, amount: int) -> bool:
        pass

    def withdraw(self, amount: int) -> bool:
        pass

    def calc_interest(self, days: int) -> int:
        pass

    def get_info(self):
        pass

    def transfer_ownership(self, new_customer: Customer) -> bool:
        pass


class Transaction:
    def __init__(self, src_account: Account, dest_account: Account, amount: int) -> None:
        self.src_account: Account = src_account
        self.dest_account: Account = dest_account
        self.amount: int = amount

    def sign_transaction(self, sign_date: date) -> None:
        pass


class Loan:
    def __init__(self, account: Account, amount: int, days: int) -> None:
        self.account: Account = account
        self.amount: int = amount
        self.days: int = days
        self.is_delayed: bool = False

    def calc_penalty(self, for_days: int) -> int:
        pass

    def calc_remaining_debt(self) -> int:
        pass


class Bank:
    def __init__(self, name: str, address: str) -> None:
        self.name: str = name
        self.address: str = address
        self.customers = []
        self.accounts = []
        self.maintenance_mode = False

    def create_account(self, customer: Customer) -> Account:
        pass

    def create_customer(self, name: str, address: str, phone: str) -> Customer:
        pass

    def get_loan(self, account: Account, amount: int, for_days: int) -> Loan:
        pass

    def change_maintenance_mode(self, new_mode: bool) -> None:
        pass
