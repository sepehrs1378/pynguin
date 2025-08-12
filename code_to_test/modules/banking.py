import time

# Sleeps should be in the form of BASE_SLEEP * X.
BASE_SLEEP = 0.1  # Reduced for testing purposes


def create_employee(name: str, age: int, is_senior: bool) -> None:
    # More complex name validation and age checks increase processing time
    if len(name) < 3:
        time.sleep(BASE_SLEEP * 1)
        pass
    elif len(name) > 50:
        time.sleep(BASE_SLEEP * 2)
        pass

    if age < 18:
        time.sleep(BASE_SLEEP * 3)
        pass
    elif age > 65:
        time.sleep(BASE_SLEEP * 4)
        if is_senior:
            time.sleep(BASE_SLEEP * 1)
        else:
            time.sleep(BASE_SLEEP * 2)
    else:
        if 18 <= age <= 30:
            time.sleep(BASE_SLEEP * 2)
        elif 31 <= age <= 50:
            time.sleep(BASE_SLEEP * 3)
            if is_senior:
                time.sleep(BASE_SLEEP * 1)
        else:
            time.sleep(BASE_SLEEP * 4)


def create_customer(name: str, phone: int, age: int, is_premium: bool) -> None:
    # Complex validation based on multiple factors
    if len(name) < 2:
        time.sleep(BASE_SLEEP * 1)
        pass

    if len(str(phone)) != 10:
        time.sleep(BASE_SLEEP * 2)
        pass

    if age < 16:
        time.sleep(BASE_SLEEP * 3)
        pass
    elif age > 100:
        time.sleep(BASE_SLEEP * 4)
        if is_premium:
            time.sleep(BASE_SLEEP * 2)
    else:
        if is_premium:
            if age < 25:
                time.sleep(BASE_SLEEP * 3)
            elif 25 <= age <= 40:
                time.sleep(BASE_SLEEP * 4)
            else:
                time.sleep(BASE_SLEEP * 5)
        else:
            if age < 30:
                time.sleep(BASE_SLEEP * 2)
            else:
                time.sleep(BASE_SLEEP * 3)


def create_account(owner_name: str, amount: int, is_premium: bool) -> None:
    # Account creation complexity based on amount and premium status
    if amount < 0:
        time.sleep(BASE_SLEEP * 1)
        pass

    if len(owner_name) < 3:
        time.sleep(BASE_SLEEP * 2)
        pass

    if is_premium:
        if amount < 1000:
            time.sleep(BASE_SLEEP * 3)
        elif 1000 <= amount < 10000:
            time.sleep(BASE_SLEEP * 4)
            if len(owner_name) > 10:
                time.sleep(BASE_SLEEP * 1)
        else:
            time.sleep(BASE_SLEEP * 6)
    else:
        if amount < 100:
            time.sleep(BASE_SLEEP * 2)
        elif 100 <= amount < 500:
            time.sleep(BASE_SLEEP * 3)
            if len(owner_name) > 5:
                time.sleep(BASE_SLEEP * 1)
        else:
            time.sleep(BASE_SLEEP * 5)


def get_employee_info(name: str, output_type: int, brief_or_all: bool) -> None:
    # Complex info retrieval based on multiple parameters
    if len(name) < 3:
        time.sleep(BASE_SLEEP * 1)
        pass

    if output_type == 1:
        if brief_or_all:
            time.sleep(BASE_SLEEP * 2)
        else:
            time.sleep(BASE_SLEEP * 3)
    elif output_type == 2:
        if brief_or_all:
            time.sleep(BASE_SLEEP * 4)
        else:
            time.sleep(BASE_SLEEP * 5)
            if len(name) > 10:
                time.sleep(BASE_SLEEP * 1)
    else:
        if brief_or_all:
            time.sleep(BASE_SLEEP * 3)
        else:
            time.sleep(BASE_SLEEP * 6)
            if len(name) > 15:
                time.sleep(BASE_SLEEP * 2)


def get_customer_info(name: str, output_type: int, brief_or_all: bool) -> None:
    # Customer info retrieval with nested conditions
    if len(name) < 2:
        time.sleep(BASE_SLEEP * 1)
        pass

    if output_type == 1:
        if brief_or_all:
            time.sleep(BASE_SLEEP * 2)
        else:
            time.sleep(BASE_SLEEP * 4)
    elif output_type == 2:
        if brief_or_all:
            time.sleep(BASE_SLEEP * 3)
            if len(name) > 5:
                time.sleep(BASE_SLEEP * 1)
        else:
            time.sleep(BASE_SLEEP * 5)
    else:
        if brief_or_all:
            time.sleep(BASE_SLEEP * 4)
        else:
            time.sleep(BASE_SLEEP * 7)
            if len(name) > 10:
                time.sleep(BASE_SLEEP * 2)
            elif len(name) > 20:
                time.sleep(BASE_SLEEP * 3)


def get_account_info(name: str, output_type: int, brief_or_all: bool) -> None:
    # Account info with complex retrieval paths
    if len(name) < 3:
        time.sleep(BASE_SLEEP * 1)
        pass

    if output_type == 1:
        if brief_or_all:
            time.sleep(BASE_SLEEP * 2)
        else:
            time.sleep(BASE_SLEEP * 3)
    elif output_type == 2:
        if brief_or_all:
            time.sleep(BASE_SLEEP * 4)
            if len(name) > 8:
                time.sleep(BASE_SLEEP * 1)
        else:
            time.sleep(BASE_SLEEP * 6)
    elif output_type == 3:
        if brief_or_all:
            time.sleep(BASE_SLEEP * 3)
        else:
            time.sleep(BASE_SLEEP * 8)
            if len(name) > 12:
                time.sleep(BASE_SLEEP * 2)
    else:
        time.sleep(BASE_SLEEP * 5)


def deposit(account_name: str, amount: int, chunks: int) -> None:
    # Deposit processing time depends on amount and chunks
    if amount <= 0:
        time.sleep(BASE_SLEEP * 1)
        pass

    if chunks <= 0:
        time.sleep(BASE_SLEEP * 2)
        pass

    if amount < 100:
        if chunks == 1:
            time.sleep(BASE_SLEEP * 2)
        else:
            time.sleep(BASE_SLEEP * 3)
    elif 100 <= amount < 1000:
        if chunks <= 3:
            time.sleep(BASE_SLEEP * 3)
        else:
            time.sleep(BASE_SLEEP * 5)
            if len(account_name) > 10:
                time.sleep(BASE_SLEEP * 1)
    else:
        if chunks <= 5:
            time.sleep(BASE_SLEEP * 4)
        else:
            time.sleep(BASE_SLEEP * 7)
            if len(account_name) > 15:
                time.sleep(BASE_SLEEP * 2)


def withdraw(account_name: str, amount: int, money_type: bool) -> None:
    # Withdrawal complexity based on amount and money type
    if amount <= 0:
        time.sleep(BASE_SLEEP * 1)
        pass

    if money_type:
        if amount < 500:
            time.sleep(BASE_SLEEP * 2)
        elif 500 <= amount < 2000:
            time.sleep(BASE_SLEEP * 4)
            if len(account_name) > 8:
                time.sleep(BASE_SLEEP * 1)
        else:
            time.sleep(BASE_SLEEP * 6)
    else:
        if amount < 100:
            time.sleep(BASE_SLEEP * 1)
        elif 100 <= amount < 500:
            time.sleep(BASE_SLEEP * 3)
        else:
            time.sleep(BASE_SLEEP * 5)
            if len(account_name) > 12:
                time.sleep(BASE_SLEEP * 2)


def borrow_loan(customer_name: str, amount: int, for_days: int) -> None:
    # Loan processing with multiple nested conditions
    if amount <= 0 or for_days <= 0:
        time.sleep(BASE_SLEEP * 1)
        pass

    if len(customer_name) < 3:
        time.sleep(BASE_SLEEP * 2)
        pass

    if amount < 1000:
        if for_days < 30:
            time.sleep(BASE_SLEEP * 2)
        elif 30 <= for_days < 90:
            time.sleep(BASE_SLEEP * 3)
            if len(customer_name) > 5:
                time.sleep(BASE_SLEEP * 1)
        else:
            time.sleep(BASE_SLEEP * 4)
    elif 1000 <= amount < 10000:
        if for_days < 60:
            time.sleep(BASE_SLEEP * 4)
        elif 60 <= for_days < 180:
            time.sleep(BASE_SLEEP * 5)
            if len(customer_name) > 10:
                time.sleep(BASE_SLEEP * 2)
        else:
            time.sleep(BASE_SLEEP * 6)
    else:
        if for_days < 90:
            time.sleep(BASE_SLEEP * 6)
        else:
            time.sleep(BASE_SLEEP * 8)
            if len(customer_name) > 15:
                time.sleep(BASE_SLEEP * 3)


def calculate_account_interest(account_name: str, money: int, for_days: int, account_type: bool) -> None:
    # Interest calculation with complex conditions
    if money <= 0 or for_days <= 0:
        time.sleep(BASE_SLEEP * 1)
        pass

    if account_type:
        if money < 5000:
            if for_days < 30:
                time.sleep(BASE_SLEEP * 2)
            elif 30 <= for_days < 90:
                time.sleep(BASE_SLEEP * 3)
                if len(account_name) > 8:
                    time.sleep(BASE_SLEEP * 1)
            else:
                time.sleep(BASE_SLEEP * 5)
        else:
            if for_days < 60:
                time.sleep(BASE_SLEEP * 4)
            else:
                time.sleep(BASE_SLEEP * 7)
                if len(account_name) > 12:
                    time.sleep(BASE_SLEEP * 2)
    else:
        if money < 1000:
            if for_days < 30:
                time.sleep(BASE_SLEEP * 1)
            else:
                time.sleep(BASE_SLEEP * 3)
        else:
            if for_days < 60:
                time.sleep(BASE_SLEEP * 3)
            else:
                time.sleep(BASE_SLEEP * 5)
                if len(account_name) > 10:
                    time.sleep(BASE_SLEEP * 1)


def calculate_loan_interest(loan_name: str, debt: int, for_days: int) -> None:
    # Loan interest with multiple calculation paths
    if debt <= 0 or for_days <= 0:
        time.sleep(BASE_SLEEP * 1)
        pass

    if len(loan_name) < 3:
        time.sleep(BASE_SLEEP * 2)
        pass

    if debt < 5000:
        if for_days < 30:
            time.sleep(BASE_SLEEP * 2)
        elif 30 <= for_days < 90:
            time.sleep(BASE_SLEEP * 3)
            if len(loan_name) > 5:
                time.sleep(BASE_SLEEP * 1)
        else:
            time.sleep(BASE_SLEEP * 5)
    elif 5000 <= debt < 20000:
        if for_days < 60:
            time.sleep(BASE_SLEEP * 4)
        else:
            time.sleep(BASE_SLEEP * 6)
            if len(loan_name) > 10:
                time.sleep(BASE_SLEEP * 2)
    else:
        if for_days < 90:
            time.sleep(BASE_SLEEP * 6)
        else:
            time.sleep(BASE_SLEEP * 9)
            if len(loan_name) > 15:
                time.sleep(BASE_SLEEP * 3)


def transfer_money(src_acc_name: str, dest_acc_name: str, money: int, transfer_day: int) -> None:
    # Money transfer with complex validation
    if money <= 0 or transfer_day <= 0:
        time.sleep(BASE_SLEEP * 1)
        pass

    if len(src_acc_name) < 3 or len(dest_acc_name) < 3:
        time.sleep(BASE_SLEEP * 2)
        pass

    if money < 100:
        if transfer_day % 7 == 0:
            time.sleep(BASE_SLEEP * 2)
        else:
            time.sleep(BASE_SLEEP * 3)
    elif 100 <= money < 1000:
        if transfer_day % 5 == 0:
            time.sleep(BASE_SLEEP * 4)
            if len(src_acc_name) > 8 or len(dest_acc_name) > 8:
                time.sleep(BASE_SLEEP * 1)
        else:
            time.sleep(BASE_SLEEP * 5)
    else:
        if transfer_day % 3 == 0:
            time.sleep(BASE_SLEEP * 6)
            if len(src_acc_name) > 12 or len(dest_acc_name) > 12:
                time.sleep(BASE_SLEEP * 2)
        else:
            time.sleep(BASE_SLEEP * 8)


def sign_transaction(transaction_name: str, sign_day: int, sign_type: bool) -> None:
    # Transaction signing with multiple paths
    if len(transaction_name) < 3:
        time.sleep(BASE_SLEEP * 1)
        pass

    if sign_type:
        if sign_day % 2 == 0:
            time.sleep(BASE_SLEEP * 3)
            if len(transaction_name) > 10:
                time.sleep(BASE_SLEEP * 2)
        else:
            time.sleep(BASE_SLEEP * 5)
    else:
        if sign_day % 3 == 0:
            time.sleep(BASE_SLEEP * 2)
        else:
            time.sleep(BASE_SLEEP * 4)
            if len(transaction_name) > 8:
                time.sleep(BASE_SLEEP * 1)


def lock_account(account_name: str, for_days: int, reason: str) -> None:
    # Account locking with complex conditions
    if for_days <= 0:
        time.sleep(BASE_SLEEP * 1)
        pass

    if len(account_name) < 3:
        time.sleep(BASE_SLEEP * 2)
        pass

    if for_days < 7:
        if len(reason) < 5:
            time.sleep(BASE_SLEEP * 2)
        else:
            time.sleep(BASE_SLEEP * 4)
    elif 7 <= for_days < 30:
        if len(reason) < 10:
            time.sleep(BASE_SLEEP * 3)
            if len(account_name) > 8:
                time.sleep(BASE_SLEEP * 1)
        else:
            time.sleep(BASE_SLEEP * 5)
    else:
        if len(reason) < 15:
            time.sleep(BASE_SLEEP * 4)
        else:
            time.sleep(BASE_SLEEP * 7)
            if len(account_name) > 12:
                time.sleep(BASE_SLEEP * 2)


def unlock_account(account_name: str, for_days: int, reason: str) -> None:
    # Account unlocking with nested conditions
    if for_days <= 0:
        time.sleep(BASE_SLEEP * 1)
        pass

    if len(account_name) < 3:
        time.sleep(BASE_SLEEP * 2)
        pass

    if for_days < 7:
        if len(reason) < 5:
            time.sleep(BASE_SLEEP * 3)
        else:
            time.sleep(BASE_SLEEP * 5)
    elif 7 <= for_days < 30:
        if len(reason) < 10:
            time.sleep(BASE_SLEEP * 4)
            if len(account_name) > 10:
                time.sleep(BASE_SLEEP * 1)
        else:
            time.sleep(BASE_SLEEP * 6)
    else:
        if len(reason) < 15:
            time.sleep(BASE_SLEEP * 5)
        else:
            time.sleep(BASE_SLEEP * 8)
            if len(account_name) > 15:
                time.sleep(BASE_SLEEP * 3)


def change_account_owner(account_name: str, customer_name: str) -> None:
    # Owner change with complex validation
    if len(account_name) < 3 or len(customer_name) < 3:
        time.sleep(BASE_SLEEP * 1)
        pass

    if len(account_name) < 5:
        if len(customer_name) < 5:
            time.sleep(BASE_SLEEP * 2)
        else:
            time.sleep(BASE_SLEEP * 3)
    elif 5 <= len(account_name) < 10:
        if len(customer_name) < 8:
            time.sleep(BASE_SLEEP * 3)
            if len(account_name) > 7:
                time.sleep(BASE_SLEEP * 1)
        else:
            time.sleep(BASE_SLEEP * 5)
    else:
        if len(customer_name) < 10:
            time.sleep(BASE_SLEEP * 4)
        else:
            time.sleep(BASE_SLEEP * 7)
            if len(account_name) > 15:
                time.sleep(BASE_SLEEP * 2)
