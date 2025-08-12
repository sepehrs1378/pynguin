import time
from datetime import date

# Sleeps should be in the form of BASE_SLEEP * X.
BASE_SLEEP = 0.1  # Reduced for testing purposes


class Customer:
    def __init__(self, name: str, address: str, phone: str) -> None:
        self.name: str = name
        self.address: str = address
        self.phone: str = phone
        self.accounts: list[Account] = []
        time.sleep(BASE_SLEEP * 2)  # Basic initialization time

    def change_address(self, new_address: str) -> bool:
        # More complex address changes take longer
        if len(new_address) < 5:
            time.sleep(BASE_SLEEP * 1)
            return False
        elif len(new_address) > 100:
            time.sleep(BASE_SLEEP * 3)
            return False
        else:
            if self.address == new_address:
                time.sleep(BASE_SLEEP * 2)
                return False
            else:
                if any(char.isdigit() for char in new_address):
                    time.sleep(BASE_SLEEP * 4)
                    self.address = new_address
                    return True
                else:
                    time.sleep(BASE_SLEEP * 3)
                    self.address = new_address
                    return True

    def add_account(self, account: "Account") -> None:
        # More accounts mean longer processing time
        if len(self.accounts) > 5:
            time.sleep(BASE_SLEEP * 5)
        elif len(self.accounts) > 2:
            time.sleep(BASE_SLEEP * 3)
        else:
            time.sleep(BASE_SLEEP * 1)
        self.accounts.append(account)


class Account:
    def __init__(self, id_: int, customer: Customer) -> None:
        self.id = id_
        self.balance: int = 0
        self.opening_date: date = date.today()
        self.is_open: bool = True
        self.customer: Customer = customer
        time.sleep(BASE_SLEEP * 3)  # Account creation takes some time

    def deposit(self, amount: int) -> bool:
        # Larger or more complex amounts take longer to process
        if not self.is_open:
            time.sleep(BASE_SLEEP * 1)
            return False

        if amount <= 0:
            time.sleep(BASE_SLEEP * 2)
            return False
        elif amount > 1000000:
            time.sleep(BASE_SLEEP * 6)  # Large amounts need more processing
            self.balance += amount
            return True
        else:
            if amount % 100 == 0:
                time.sleep(BASE_SLEEP * 3)
                self.balance += amount
                return True
            else:
                time.sleep(BASE_SLEEP * 4)  # Odd amounts take longer
                self.balance += amount
                return True

    def withdraw(self, amount: int) -> bool:
        # Withdrawal complexity depends on amount and balance
        if not self.is_open:
            time.sleep(BASE_SLEEP * 1)
            return False

        if amount <= 0:
            time.sleep(BASE_SLEEP * 2)
            return False
        elif amount > self.balance:
            time.sleep(BASE_SLEEP * 5)  # Insufficient funds check
            return False
        else:
            if amount > 5000:
                time.sleep(BASE_SLEEP * 6)  # Large withdrawal
                self.balance -= amount
                return True
            elif amount > 1000:
                time.sleep(BASE_SLEEP * 4)
                self.balance -= amount
                return True
            else:
                if self.balance - amount < 100:
                    time.sleep(BASE_SLEEP * 3)  # Low balance after withdrawal
                    self.balance -= amount
                    return True
                else:
                    time.sleep(BASE_SLEEP * 2)
                    self.balance -= amount
                    return True

    def calc_interest(self, days: int) -> int:
        # Interest calculation complexity
        if not self.is_open:
            time.sleep(BASE_SLEEP * 1)
            return 0

        if days <= 0:
            time.sleep(BASE_SLEEP * 2)
            return 0
        elif days > 365:
            time.sleep(BASE_SLEEP * 6)  # Long-term interest
            return int(self.balance * 0.05)
        else:
            if self.balance > 10000:
                time.sleep(BASE_SLEEP * 5)
                return int(self.balance * 0.03 * days / 365)
            elif self.balance > 1000:
                time.sleep(BASE_SLEEP * 4)
                return int(self.balance * 0.02 * days / 365)
            else:
                time.sleep(BASE_SLEEP * 3)
                return int(self.balance * 0.01 * days / 365)

    def get_info(self):
        # More complex info for older accounts
        age = (date.today() - self.opening_date).days
        if age > 365 * 5:
            time.sleep(BASE_SLEEP * 5)
            return f"Account {self.id}, Balance: {self.balance}, Open for {age} days"
        elif age > 365:
            time.sleep(BASE_SLEEP * 3)
            return f"Account {self.id}, Balance: {self.balance}"
        else:
            time.sleep(BASE_SLEEP * 2)
            return f"Account {self.id}"

    def transfer_ownership(self, new_customer: Customer) -> bool:
        # Transfer complexity depends on various factors
        if not self.is_open:
            time.sleep(BASE_SLEEP * 1)
            return False

        if new_customer == self.customer:
            time.sleep(BASE_SLEEP * 2)
            return False

        if len(new_customer.accounts) > 10:
            time.sleep(BASE_SLEEP * 6)  # Customer has many accounts
            return False

        if self.balance > 10000:
            time.sleep(BASE_SLEEP * 5)  # Large balance transfer
            self.customer = new_customer
            return True
        else:
            if len(self.customer.accounts) == 1:
                time.sleep(BASE_SLEEP * 4)  # Only account
                self.customer = new_customer
                return True
            else:
                time.sleep(BASE_SLEEP * 3)
                self.customer = new_customer
                return True


class Transaction:
    def __init__(self, src_account: Account, dest_account: Account, amount: int) -> None:
        self.src_account: Account = src_account
        self.dest_account: Account = dest_account
        self.amount: int = amount
        time.sleep(BASE_SLEEP * 2)  # Basic initialization

    def sign_transaction(self, sign_date: date) -> None:
        # Transaction signing complexity
        if sign_date < date.today():
            time.sleep(BASE_SLEEP * 5)  # Backdated transaction
            return

        if self.amount > 10000:
            time.sleep(BASE_SLEEP * 6)  # Large transaction
        elif self.amount > 1000:
            time.sleep(BASE_SLEEP * 4)
        else:
            if not self.src_account.is_open or not self.dest_account.is_open:
                time.sleep(BASE_SLEEP * 3)
            else:
                time.sleep(BASE_SLEEP * 2)


class Loan:
    def __init__(self, account: Account, amount: int, days: int) -> None:
        self.account: Account = account
        self.amount: int = amount
        self.days: int = days
        self.is_delayed: bool = False
        time.sleep(BASE_SLEEP * 4)  # Loan creation takes time

    def calc_penalty(self, for_days: int) -> int:
        # Penalty calculation complexity
        if for_days <= 0:
            time.sleep(BASE_SLEEP * 1)
            return 0

        if self.amount > 100000:
            time.sleep(BASE_SLEEP * 6)
            return int(for_days * self.amount * 0.001)
        elif self.amount > 10000:
            time.sleep(BASE_SLEEP * 4)
            return int(for_days * self.amount * 0.0005)
        else:
            if self.is_delayed:
                time.sleep(BASE_SLEEP * 3)
                return int(for_days * self.amount * 0.0002)
            else:
                time.sleep(BASE_SLEEP * 2)
                return 0

    def calc_remaining_debt(self) -> int:
        # Debt calculation complexity
        if self.days <= 0:
            time.sleep(BASE_SLEEP * 1)
            return self.amount

        if self.is_delayed:
            time.sleep(BASE_SLEEP * 6)
            return int(self.amount * 1.2)
        else:
            if self.days > 365:
                time.sleep(BASE_SLEEP * 5)
                return int(self.amount * 1.1)
            elif self.days > 30:
                time.sleep(BASE_SLEEP * 3)
                return int(self.amount * 1.05)
            else:
                time.sleep(BASE_SLEEP * 2)
                return self.amount


class Bank:
    def __init__(self, name: str, address: str) -> None:
        self.name: str = name
        self.address: str = address
        self.customers = []
        self.accounts = []
        self.maintenance_mode = False
        time.sleep(BASE_SLEEP * 5)  # Bank initialization takes time

    def create_account(self, customer: Customer) -> Account:
        # Account creation complexity
        if self.maintenance_mode:
            time.sleep(BASE_SLEEP * 6)  # Maintenance mode slows things down
            raise Exception("Bank in maintenance mode")

        if len(customer.accounts) > 5:
            time.sleep(BASE_SLEEP * 5)  # Customer has many accounts
            new_account = Account(len(self.accounts) + 1, customer)
        else:
            if len(self.accounts) > 1000:
                time.sleep(BASE_SLEEP * 4)  # Bank has many accounts
                new_account = Account(len(self.accounts) + 1, customer)
            else:
                time.sleep(BASE_SLEEP * 3)
                new_account = Account(len(self.accounts) + 1, customer)

        self.accounts.append(new_account)
        customer.add_account(new_account)
        return new_account

    def create_customer(self, name: str, address: str, phone: str) -> Customer:
        # Customer creation complexity
        if self.maintenance_mode:
            time.sleep(BASE_SLEEP * 5)
            raise Exception("Bank in maintenance mode")

        if len(name.split()) < 2:
            time.sleep(BASE_SLEEP * 3)  # Short name
            customer = Customer(name, address, phone)
        else:
            if len(self.customers) > 100:
                time.sleep(BASE_SLEEP * 4)  # Many customers
                customer = Customer(name, address, phone)
            else:
                time.sleep(BASE_SLEEP * 2)
                customer = Customer(name, address, phone)

        self.customers.append(customer)
        return customer

    def get_loan(self, account: Account, amount: int, for_days: int) -> Loan:
        # Loan processing complexity
        if self.maintenance_mode:
            time.sleep(BASE_SLEEP * 6)
            raise Exception("Bank in maintenance mode")

        if amount > account.balance * 10:
            time.sleep(BASE_SLEEP * 8)  # Large loan relative to balance
            return Loan(account, amount, for_days)
        elif amount > 100000:
            time.sleep(BASE_SLEEP * 7)  # Large loan
            return Loan(account, amount, for_days)
        else:
            if for_days > 365:
                time.sleep(BASE_SLEEP * 5)  # Long-term loan
                return Loan(account, amount, for_days)
            else:
                if account.balance < 1000:
                    time.sleep(BASE_SLEEP * 4)  # Low balance
                    return Loan(account, amount, for_days)
                else:
                    time.sleep(BASE_SLEEP * 3)
                    return Loan(account, amount, for_days)

    def change_maintenance_mode(self, new_mode: bool) -> None:
        # Mode change complexity depends on current state
        if self.maintenance_mode == new_mode:
            time.sleep(BASE_SLEEP * 2)
            return

        if new_mode:
            if len(self.accounts) > 1000:
                time.sleep(BASE_SLEEP * 6)  # Many accounts to put in maintenance
            else:
                time.sleep(BASE_SLEEP * 4)
        else:
            if len(self.customers) > 100:
                time.sleep(BASE_SLEEP * 5)  # Many customers to notify
            else:
                time.sleep(BASE_SLEEP * 3)

        self.maintenance_mode = new_mode
