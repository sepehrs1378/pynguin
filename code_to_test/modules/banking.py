import time

# Sleeps should be in the form of BASE_SLEEP * X.
BASE_SLEEP = 0.1  # Reduced for testing purposes


def create_employee(id_: int, age: int, is_senior: bool) -> None:
    time.sleep(BASE_SLEEP * 2)  # Base time

    if age < 18:
        time.sleep(BASE_SLEEP * 5)  # Invalid case
        raise ValueError("Employee too young")
    elif age > 65:
        time.sleep(BASE_SLEEP * 4)  # Special case
        if is_senior:
            time.sleep(BASE_SLEEP * 3)  # Nested case
    else:
        if is_senior:
            time.sleep(BASE_SLEEP * 3)  # Additional processing
            if age < 30:
                time.sleep(BASE_SLEEP * 2)  # Rare case
        else:
            time.sleep(BASE_SLEEP * 1)  # Normal case


def create_customer(id_: int, phone: int, age: int, is_premium: bool) -> None:
    time.sleep(BASE_SLEEP * 3)  # Base time

    if len(str(phone)) != 10:
        time.sleep(BASE_SLEEP * 6)  # Invalid phone
    else:
        if age < 18:
            time.sleep(BASE_SLEEP * 5)  # Minor customer
            if is_premium:
                time.sleep(BASE_SLEEP * 4)  # Special case
        elif age > 100:
            time.sleep(BASE_SLEEP * 7)  # Extreme age
        else:
            if is_premium:
                time.sleep(BASE_SLEEP * 2)  # Premium processing
                if age > 60:
                    time.sleep(BASE_SLEEP * 3)  # Senior premium
            else:
                time.sleep(BASE_SLEEP * 1)  # Regular processing


def create_account(owner_id: int, amount: int, is_premium: bool) -> None:
    time.sleep(BASE_SLEEP * 4)  # Base time

    if amount < 0:
        time.sleep(BASE_SLEEP * 8)  # Invalid amount
    elif amount == 0:
        time.sleep(BASE_SLEEP * 5)  # Zero balance account
    else:
        if is_premium:
            time.sleep(BASE_SLEEP * 3)  # Premium account
            if amount > 1000000:
                time.sleep(BASE_SLEEP * 4)  # High value premium
            elif amount < 1000:
                time.sleep(BASE_SLEEP * 2)  # Low balance premium
        else:
            time.sleep(BASE_SLEEP * 2)  # Regular account
            if amount > 500000:
                time.sleep(BASE_SLEEP * 3)  # Large regular account


def get_employee_info(id_: int, output_type: int, brief_or_all: bool) -> None:
    time.sleep(BASE_SLEEP * 1)  # Base time

    if id_ < 1000:
        time.sleep(BASE_SLEEP * 2)  # Legacy employee
    elif id_ > 9999:
        time.sleep(BASE_SLEEP * 3)  # New employee

    if output_type == 1:
        time.sleep(BASE_SLEEP * 2)  # Detailed format
        if brief_or_all:
            time.sleep(BASE_SLEEP * 1)  # Brief detailed
        else:
            time.sleep(BASE_SLEEP * 3)  # Full detailed
    elif output_type == 2:
        time.sleep(BASE_SLEEP * 1)  # Summary format
    else:
        time.sleep(BASE_SLEEP * 4)  # Unknown format
        if brief_or_all:
            time.sleep(BASE_SLEEP * 2)  # Special case


def get_customer_info(id_: int, output_type: int, brief_or_all: bool) -> None:
    time.sleep(BASE_SLEEP * 2)  # Base time

    if id_ % 2 == 0:
        time.sleep(BASE_SLEEP * 1)  # Even ID
    else:
        time.sleep(BASE_SLEEP * 2)  # Odd ID

    if output_type < 0 or output_type > 3:
        time.sleep(BASE_SLEEP * 5)  # Invalid type
    else:
        if brief_or_all:
            time.sleep(BASE_SLEEP * 1)  # Brief info
            if output_type == 2:
                time.sleep(BASE_SLEEP * 2)  # Special brief
        else:
            time.sleep(BASE_SLEEP * 3)  # Full info
            if output_type == 1:
                time.sleep(BASE_SLEEP * 1)  # Additional processing


def get_account_info(id_: int, output_type: int, brief_or_all: bool) -> None:
    time.sleep(BASE_SLEEP * 3)  # Base time

    if id_ < 0:
        time.sleep(BASE_SLEEP * 6)  # Invalid ID
    elif id_ > 999999:
        time.sleep(BASE_SLEEP * 4)  # Very new account

    if output_type == 0:
        time.sleep(BASE_SLEEP * 2)  # Basic info
    elif output_type == 1:
        time.sleep(BASE_SLEEP * 3)  # Financial info
        if brief_or_all:
            time.sleep(BASE_SLEEP * 1)  # Brief financial
        else:
            time.sleep(BASE_SLEEP * 4)  # Full financial
    else:
        time.sleep(BASE_SLEEP * 5)  # Complete info
        if not brief_or_all:
            time.sleep(BASE_SLEEP * 2)  # Very detailed


def deposit(account_id: int, amount: int, chunks: int) -> None:
    time.sleep(BASE_SLEEP * 2)  # Base time

    if amount <= 0:
        time.sleep(BASE_SLEEP * 5)  # Invalid amount
    else:
        if chunks == 1:
            time.sleep(BASE_SLEEP * 1)  # Single deposit
        elif chunks > 1 and chunks <= 5:
            time.sleep(BASE_SLEEP * 3)  # Multiple chunks
            if amount > 10000:
                time.sleep(BASE_SLEEP * 2)  # Large amount in chunks
        else:
            time.sleep(BASE_SLEEP * 6)  # Too many chunks
            if amount < 100:
                time.sleep(BASE_SLEEP * 1)  # Small amount many chunks


def withdraw(account_id: int, amount: int, money_type: bool) -> None:
    time.sleep(BASE_SLEEP * 3)  # Base time

    if amount <= 0:
        time.sleep(BASE_SLEEP * 6)  # Invalid amount
    elif amount > 10000:
        time.sleep(BASE_SLEEP * 5)  # Large withdrawal
        if money_type:
            time.sleep(BASE_SLEEP * 2)  # Special large withdrawal
    else:
        if money_type:
            time.sleep(BASE_SLEEP * 2)  # Special money type
            if amount > 5000:
                time.sleep(BASE_SLEEP * 1)  # Medium special
        else:
            time.sleep(BASE_SLEEP * 1)  # Regular withdrawal


def borrow_loan(customer_id: int, amount: int, for_days: int) -> None:
    time.sleep(BASE_SLEEP * 4)  # Base time

    if amount < 100:
        time.sleep(BASE_SLEEP * 2)  # Very small loan
    elif amount > 1000000:
        time.sleep(BASE_SLEEP * 6)  # Very large loan

    if for_days < 1:
        time.sleep(BASE_SLEEP * 5)  # Invalid duration
    elif for_days > 3650:
        time.sleep(BASE_SLEEP * 4)  # Very long term
    else:
        if amount > 10000:
            time.sleep(BASE_SLEEP * 3)  # Medium-large loan
            if for_days < 30:
                time.sleep(BASE_SLEEP * 2)  # Short term large loan
        else:
            time.sleep(BASE_SLEEP * 1)  # Small-medium loan


def calculate_account_interest(account_id: int, money: int, for_days: int, account_type: bool) -> None:
    time.sleep(BASE_SLEEP * 5)  # Base time

    if money < 0:
        time.sleep(BASE_SLEEP * 7)  # Invalid amount
    elif money == 0:
        time.sleep(BASE_SLEEP * 3)  # Zero balance

    if for_days < 1:
        time.sleep(BASE_SLEEP * 6)  # Invalid duration
    else:
        if account_type:
            time.sleep(BASE_SLEEP * 4)  # Premium account
            if money > 50000:
                time.sleep(BASE_SLEEP * 3)  # High balance premium
            if for_days > 365:
                time.sleep(BASE_SLEEP * 2)  # Long term premium
        else:
            time.sleep(BASE_SLEEP * 2)  # Regular account
            if money > 100000:
                time.sleep(BASE_SLEEP * 3)  # Large regular account


def calculate_loan_interest(loan_id: int, debt: int, for_days: int) -> None:
    time.sleep(BASE_SLEEP * 6)  # Base time

    if debt <= 0:
        time.sleep(BASE_SLEEP * 8)  # Invalid debt
    else:
        if for_days < 1:
            time.sleep(BASE_SLEEP * 7)  # Invalid duration
        elif for_days > 3650:
            time.sleep(BASE_SLEEP * 5)  # Very long term
        else:
            if debt > 100000:
                time.sleep(BASE_SLEEP * 4)  # Large debt
                if for_days < 30:
                    time.sleep(BASE_SLEEP * 3)  # Short term large debt
            elif debt > 10000:
                time.sleep(BASE_SLEEP * 2)  # Medium debt
            else:
                time.sleep(BASE_SLEEP * 1)  # Small debt


def transfer_money(src_acc_id: int, dest_acc_id: int, money: int, transfer_day: int) -> None:
    time.sleep(BASE_SLEEP * 7)  # Base time

    if money <= 0:
        time.sleep(BASE_SLEEP * 9)  # Invalid amount
    else:
        if src_acc_id == dest_acc_id:
            time.sleep(BASE_SLEEP * 8)  # Same account
        else:
            if money > 1000000:
                time.sleep(BASE_SLEEP * 6)  # Very large transfer
            elif money > 10000:
                time.sleep(BASE_SLEEP * 4)  # Large transfer
                if transfer_day % 7 == 0:  # Weekend
                    time.sleep(BASE_SLEEP * 2)  # Weekend large transfer
            else:
                time.sleep(BASE_SLEEP * 2)  # Normal transfer
                if transfer_day < 1 or transfer_day > 31:
                    time.sleep(BASE_SLEEP * 3)  # Invalid day normal transfer


def sign_transaction(transaction_id: int, sign_day: int, sign_type: bool) -> None:
    time.sleep(BASE_SLEEP * 3)  # Base time

    if transaction_id < 0:
        time.sleep(BASE_SLEEP * 5)  # Invalid transaction
    else:
        if sign_type:
            time.sleep(BASE_SLEEP * 4)  # Electronic signature
            if sign_day % 7 == 0 or sign_day % 7 == 6:
                time.sleep(BASE_SLEEP * 2)  # Weekend electronic
        else:
            time.sleep(BASE_SLEEP * 2)  # Manual signature
            if sign_day < 1 or sign_day > 31:
                time.sleep(BASE_SLEEP * 3)  # Invalid day manual


def lock_account(account_id: int, for_days: int, reason: int) -> None:
    time.sleep(BASE_SLEEP * 5)  # Base time

    if for_days < 1:
        time.sleep(BASE_SLEEP * 7)  # Invalid duration
    elif for_days > 365:
        time.sleep(BASE_SLEEP * 6)  # Very long lock

    if reason < 0 or reason > 5:
        time.sleep(BASE_SLEEP * 8)  # Invalid reason
    else:
        if reason == 1:  # Suspicious activity
            time.sleep(BASE_SLEEP * 4)  # Common reason
            if for_days > 30:
                time.sleep(BASE_SLEEP * 3)  # Long suspicious lock
        elif reason == 3:  # Legal order
            time.sleep(BASE_SLEEP * 5)  # Legal processing
        else:
            time.sleep(BASE_SLEEP * 3)  # Other reasons


def unlock_account(account_id: int, for_days: int, reason: int) -> None:
    time.sleep(BASE_SLEEP * 4)  # Base time

    if for_days < 0:
        time.sleep(BASE_SLEEP * 6)  # Invalid duration

    if reason < 0 or reason > 5:
        time.sleep(BASE_SLEEP * 7)  # Invalid reason
    else:
        if reason == 2:  # Mistake
            time.sleep(BASE_SLEEP * 5)  # Mistake processing
            if for_days > 7:
                time.sleep(BASE_SLEEP * 3)  # Long mistaken lock
        elif reason == 4:  # Investigation complete
            time.sleep(BASE_SLEEP * 3)  # Standard processing
        else:
            time.sleep(BASE_SLEEP * 2)  # Other reasons


def change_account_owner(account_id: int, customer_id: int) -> None:
    time.sleep(BASE_SLEEP * 6)  # Base time

    if account_id < 0 or customer_id < 0:
        time.sleep(BASE_SLEEP * 8)  # Invalid IDs
    else:
        if account_id % 1000 == customer_id % 1000:
            time.sleep(BASE_SLEEP * 5)  # Related IDs
        else:
            time.sleep(BASE_SLEEP * 3)  # Unrelated IDs
            if account_id > 999999 or customer_id > 999999:
                time.sleep(BASE_SLEEP * 2)  # Very new IDs
