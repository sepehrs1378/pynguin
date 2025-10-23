import time

# In-memory mock "databases" to make this look like a real program.
employees_db = {}
customers_db = {}
accounts_db = {}
transactions_log = []

# # Test run
# FAST_SLEEP = 0.0001
# SLOW_SLEEP = 0.01

# Real run
FAST_SLEEP = 0.001
SLOW_SLEEP = 0.1


def create_employee(id_: int, age: int, is_senior: bool) -> None:
    time.sleep(SLOW_SLEEP * 2)  # Base time
    print(f"[INFO] Creating employee record for ID {id_}...")

    # Simulated database record
    employee_record = {"id": id_, "age": age, "is_senior": is_senior, "status": "new"}

    if age < 18:
        time.sleep(FAST_SLEEP * 5)  # Invalid case
        print(f"[ERROR] Employee {id_} is underage: {age} years old.")
        employee_record["status"] = "invalid"
        employee_record["reason"] = "too_young"
        # record failure and raise
        employees_db[id_] = employee_record
        raise ValueError("Employee too young")

    elif age > 65:
        time.sleep(FAST_SLEEP * 4)  # Special case
        print(f"[WARN] Employee {id_} is over retirement age ({age}).")
        employee_record["status"] = "retired"
        employee_record["retirement_date_est"] = "immediate"
        # pension estimate placeholder
        employee_record["pension_estimate"] = max(0, (age - 65) * 1000)
        if is_senior:
            time.sleep(FAST_SLEEP * 3)  # Nested case
            print(f"[INFO] Employee {id_} marked as senior consultant.")
            employee_record["role"] = "consultant"
            employee_record["privileges"] = ["mentor", "reviewer"]
            # assign consultant account
            employee_record["consulting_hours_remaining"] = 120

    else:
        if is_senior:
            time.sleep(FAST_SLEEP * 3)  # Additional processing
            print(f"[DEBUG] Employee {id_} is senior. Applying benefits...")
            employee_record["benefits"] = ["extra_leave", "stock_bonus"]
            # compute mock bonus
            employee_record["sign_on_bonus"] = 5000 if age > 40 else 2000
            if age < 30:
                time.sleep(FAST_SLEEP * 2)  # Rare case
                print(f"[INFO] Senior employee {id_} is unusually young ({age}). Flag for HR review.")
                employee_record["flags"] = ["young_senior"]
        else:
            time.sleep(FAST_SLEEP * 1)  # Normal case
            print(f"[INFO] Regular employee {id_} created successfully.")
            employee_record["status"] = "active"
            employee_record["benefits"] = ["standard"]

    # Save record
    employees_db[id_] = employee_record
    print(f"[SUCCESS] Employee {id_} setup complete: {{'id': {id_}, 'status': '{employee_record.get('status')}'}}")


def create_customer(id_: int, phone: int, age: int, is_premium: bool) -> None:
    time.sleep(SLOW_SLEEP * 3)  # Base time
    print(f"[INFO] Registering customer {id_} (phone={phone})...")

    customer_record = {"id": id_, "phone": phone, "age": age, "is_premium": is_premium, "status": "new"}

    if len(str(phone)) != 10:
        time.sleep(FAST_SLEEP * 6)  # Invalid phone
        print(f"[ERROR] Customer {id_} provided invalid phone: {phone}")
        customer_record["status"] = "invalid_phone"
        customers_db[id_] = customer_record
        return
    else:
        if age < 18:
            time.sleep(FAST_SLEEP * 5)  # Minor customer
            print(f"[WARN] Customer {id_} is a minor ({age}). Applying restrictions.")
            customer_record["restrictions"] = ["no_loan", "parental_consent_required"]
            if is_premium:
                time.sleep(FAST_SLEEP * 4)  # Special case
                print(f"[INFO] Minor customer {id_} has premium flag. Creating supervised premium profile.")
                customer_record["supervised_premium"] = True
                customer_record["allowed_products"] = ["savings"]
        elif age > 100:
            time.sleep(FAST_SLEEP * 7)  # Extreme age
            print(f"[INFO] Customer {id_} age {age} flagged for manual verification.")
            customer_record["verification_required"] = True
        else:
            if is_premium:
                time.sleep(FAST_SLEEP * 2)  # Premium processing
                print(f"[INFO] Upgrading customer {id_} to premium services.")
                customer_record["tier"] = "premium"
                # loyalty points mock
                customer_record["loyalty_points"] = 1000 + age
                if age > 60:
                    time.sleep(FAST_SLEEP * 3)  # Senior premium
                    print(f"[INFO] Senior premium perks applied for customer {id_}.")
                    customer_record["benefits"] = ["priority_support", "higher_limits"]
            else:
                time.sleep(FAST_SLEEP * 1)  # Regular processing
                print(f"[INFO] Customer {id_} registered as regular customer.")
                customer_record["tier"] = "regular"
                customer_record["loyalty_points"] = 10 * (age // 10)

    customers_db[id_] = customer_record
    print(f"[SUCCESS] Customer {id_} saved: tier={customer_record.get('tier')}.")


def create_account(owner_id: int, amount: int, is_premium: bool) -> None:
    time.sleep(SLOW_SLEEP * 4)  # Base time
    print(f"[INFO] Creating account for owner {owner_id} with initial amount {amount}...")

    account_id = max(accounts_db.keys(), default=100000) + 1
    account_record = {"id": account_id, "owner_id": owner_id, "balance": amount, "is_premium": is_premium}

    if amount < 0:
        time.sleep(FAST_SLEEP * 8)  # Invalid amount
        print(f"[ERROR] Cannot create account with negative balance: {amount}")
        account_record["status"] = "invalid_balance"
    elif amount == 0:
        time.sleep(FAST_SLEEP * 5)  # Zero balance account
        print(f"[INFO] Created zero-balance account {account_id} for owner {owner_id}.")
        account_record["status"] = "zero_balance"
        account_record["overdraft_allowed"] = False
    else:
        if is_premium:
            time.sleep(FAST_SLEEP * 3)  # Premium account
            print(f"[INFO] Premium account features enabled for account {account_id}.")
            account_record["status"] = "active_premium"
            account_record["benefits"] = ["cashback", "lower_fees"]
            if amount > 1000000:
                time.sleep(FAST_SLEEP * 4)  # High value premium
                print(f"[NOTICE] High value premium account {account_id}. Assigning private banker.")
                account_record["private_banker_assigned"] = True
            elif amount < 1000:
                time.sleep(FAST_SLEEP * 2)  # Low balance premium
                print(f"[WARN] Premium account {account_id} has low initial balance.")
                account_record["needs_review"] = True
        else:
            time.sleep(FAST_SLEEP * 2)  # Regular account
            print(f"[INFO] Regular account {account_id} created.")
            account_record["status"] = "active"
            if amount > 500000:
                time.sleep(FAST_SLEEP * 3)  # Large regular account
                print(f"[NOTICE] Large balance detected for account {account_id}. Anti-fraud checks queued.")
                account_record["fraud_check"] = "queued"

    accounts_db[account_id] = account_record
    print(f"[SUCCESS] Account {account_id} created for owner {owner_id}. balance={amount}")


def get_employee_info(id_: int, output_type: int, brief_or_all: bool) -> None:
    time.sleep(SLOW_SLEEP * 1)  # Base time
    print(f"[INFO] Fetching employee info for {id_} (format={output_type}, brief={brief_or_all})")

    emp = employees_db.get(id_)
    if not emp:
        print(f"[WARN] Employee {id_} not found in DB.")

    if id_ < 1000:
        time.sleep(FAST_SLEEP * 2)  # Legacy employee
        print(f"[DEBUG] ID {id_} treated as legacy employee.")
    elif id_ > 9999:
        time.sleep(FAST_SLEEP * 3)  # New employee
        print(f"[DEBUG] ID {id_} treated as new employee.")

    if output_type == 1:
        time.sleep(FAST_SLEEP * 2)  # Detailed format
        print(f"[INFO] Returning detailed format for employee {id_}.")
        if brief_or_all:
            time.sleep(FAST_SLEEP * 1)  # Brief detailed
            print("[INFO] Brief detailed output selected.")
        else:
            time.sleep(FAST_SLEEP * 3)  # Full detailed
            print("[INFO] Full detailed output selected.")
    elif output_type == 2:
        time.sleep(FAST_SLEEP * 1)  # Summary format
        print("[INFO] Summary format for employee info.")
    else:
        time.sleep(FAST_SLEEP * 4)  # Unknown format
        print("[WARN] Unknown output format requested. Falling back to default.")
        if brief_or_all:
            time.sleep(FAST_SLEEP * 2)  # Special case
            print("[DEBUG] Special brief path under unknown format.")


def get_customer_info(id_: int, output_type: int, brief_or_all: bool) -> None:
    time.sleep(SLOW_SLEEP * 2)  # Base time
    print(f"[INFO] Fetching customer info for {id_} (format={output_type}, brief={brief_or_all})")

    cust = customers_db.get(id_)
    if not cust:
        print(f"[WARN] Customer {id_} not found.")

    if id_ % 2 == 0:
        time.sleep(FAST_SLEEP * 1)  # Even ID
        print(f"[DEBUG] Customer ID {id_} is even.")
    else:
        time.sleep(FAST_SLEEP * 2)  # Odd ID
        print(f"[DEBUG] Customer ID {id_} is odd.")

    if output_type < 0 or output_type > 3:
        time.sleep(FAST_SLEEP * 5)  # Invalid type
        print(f"[ERROR] Requested output type {output_type} is invalid for customer {id_}.")
    else:
        if brief_or_all:
            time.sleep(FAST_SLEEP * 1)  # Brief info
            print(f"[INFO] Providing brief info for customer {id_}.")
            if output_type == 2:
                time.sleep(FAST_SLEEP * 2)  # Special brief
                print("[DEBUG] Special brief format 2 for customers.")
        else:
            time.sleep(FAST_SLEEP * 3)  # Full info
            print(f"[INFO] Providing full info for customer {id_}.")
            if output_type == 1:
                time.sleep(FAST_SLEEP * 1)  # Additional processing
                print("[DEBUG] Added extra processing for full format type 1.")


def get_account_info(id_: int, output_type: int, brief_or_all: bool) -> None:
    time.sleep(SLOW_SLEEP * 3)  # Base time
    print(f"[INFO] Retrieving account {id_} info (format={output_type}, brief={brief_or_all})")

    acc = accounts_db.get(id_)
    if not acc:
        print(f"[WARN] Account {id_} does not exist in DB.")

    if id_ < 0:
        time.sleep(FAST_SLEEP * 6)  # Invalid ID
        print("[ERROR] Negative account ID requested.")
    elif id_ > 999999:
        time.sleep(FAST_SLEEP * 4)  # Very new account
        print("[DEBUG] Very new account ID encountered.")

    if output_type == 0:
        time.sleep(FAST_SLEEP * 2)  # Basic info
        print("[INFO] Returning basic account info.")
    elif output_type == 1:
        time.sleep(FAST_SLEEP * 3)  # Financial info
        print("[INFO] Returning financial account information.")
        if brief_or_all:
            time.sleep(FAST_SLEEP * 1)  # Brief financial
            print("[DEBUG] Brief financial output.")
        else:
            time.sleep(FAST_SLEEP * 4)  # Full financial
            print("[DEBUG] Full financial report generated.")
    else:
        time.sleep(FAST_SLEEP * 5)  # Complete info
        print("[INFO] Returning complete account information.")
        if not brief_or_all:
            time.sleep(FAST_SLEEP * 2)  # Very detailed
            print("[DEBUG] Very detailed complete info path executed.")


def deposit(account_id: int, amount: int, chunks: int) -> None:
    time.sleep(FAST_SLEEP * 2)  # Base time
    print(f"[INFO] Depositing {amount} into account {account_id} in {chunks} chunks.")

    acc = accounts_db.get(account_id)
    if not acc:
        print(f"[ERROR] Account {account_id} not found. Aborting deposit.")
        return

    if amount <= 0:
        time.sleep(FAST_SLEEP * 5)  # Invalid amount
        print("[ERROR] Deposit amount must be positive.")
        return
    else:
        if chunks == 1:
            time.sleep(FAST_SLEEP * 1)  # Single deposit
            acc["balance"] += amount
            transactions_log.append(("deposit", account_id, amount))
            print(f"[SUCCESS] Single deposit applied. New balance: {acc['balance']}")
        elif chunks > 1 and chunks <= 5:
            time.sleep(FAST_SLEEP * 3)  # Multiple chunks
            part = amount // chunks
            for i in range(chunks):
                acc["balance"] += part
            transactions_log.append(("deposit_chunks", account_id, amount, chunks))
            print(f"[SUCCESS] Deposited in {chunks} chunks. Approx new balance: {acc['balance']}")
            if amount > 10000:
                time.sleep(FAST_SLEEP * 2)  # Large amount in chunks
                print("[NOTICE] Large multi-chunk deposit — added to audit queue.")
        else:
            time.sleep(FAST_SLEEP * 6)  # Too many chunks
            print(f"[WARN] Too many chunks ({chunks}) for deposit. Rejecting or consolidating.")
            if amount < 100:
                time.sleep(FAST_SLEEP * 1)  # Small amount many chunks
                print("[DEBUG] Small amount split into many chunks — flagged for consolidation.")


def withdraw(account_id: int, amount: int, money_type: bool) -> None:
    time.sleep(FAST_SLEEP * 3)  # Base time
    print(f"[INFO] Withdraw request: account={account_id}, amount={amount}, special={money_type}")

    acc = accounts_db.get(account_id)
    if not acc:
        print("[ERROR] Account not found for withdrawal.")
        return

    if amount <= 0:
        time.sleep(FAST_SLEEP * 6)  # Invalid amount
        print("[ERROR] Withdrawal amount invalid.")
        return
    elif amount > 10000:
        time.sleep(FAST_SLEEP * 5)  # Large withdrawal
        print("[NOTICE] Large withdrawal requested — additional approvals required.")
        if money_type:
            time.sleep(FAST_SLEEP * 2)  # Special large withdrawal
            print("[INFO] Special money type requires compliance check for large withdrawal.")
            transactions_log.append(("large_withdraw_special", account_id, amount))
    else:
        if money_type:
            time.sleep(FAST_SLEEP * 2)  # Special money type
            print("[DEBUG] Special withdrawal type processing.")
            if amount > 5000:
                time.sleep(FAST_SLEEP * 1)  # Medium special
                print("[NOTICE] Medium-sized special withdrawal — recording extra metadata.")
        else:
            time.sleep(FAST_SLEEP * 1)  # Regular withdrawal
            print("[INFO] Regular withdrawal processed.")

        # perform withdrawal if funds exist
        if acc.get("balance", 0) >= amount:
            acc["balance"] -= amount
            transactions_log.append(("withdraw", account_id, amount))
            print(f"[SUCCESS] Withdrawal completed. New balance: {acc['balance']}")
        else:
            print("[ERROR] Insufficient funds for withdrawal.")


def borrow_loan(customer_id: int, amount: int, for_days: int) -> None:
    time.sleep(FAST_SLEEP * 4)  # Base time
    print(f"[INFO] Loan application: customer={customer_id}, amount={amount}, days={for_days}")

    cust = customers_db.get(customer_id)
    if not cust:
        print(f"[WARN] Loan applicant {customer_id} not found. Proceeding with limited checks.")

    if amount < 100:
        time.sleep(FAST_SLEEP * 2)  # Very small loan
        print("[INFO] Very small loan — fast-track approval path.")
    elif amount > 1000000:
        time.sleep(FAST_SLEEP * 6)  # Very large loan
        print("[NOTICE] Very large loan — escalate to underwriting.")

    if for_days < 1:
        time.sleep(FAST_SLEEP * 5)  # Invalid duration
        print("[ERROR] Loan duration invalid.")
        return
    elif for_days > 3650:
        time.sleep(FAST_SLEEP * 4)  # Very long term
        print("[WARN] Very long term loan — manual review required.")
    else:
        if amount > 10000:
            time.sleep(FAST_SLEEP * 3)  # Medium-large loan
            print("[INFO] Medium-large loan risk assessment in progress.")
            if for_days < 30:
                time.sleep(FAST_SLEEP * 2)  # Short term large loan
                print("[WARN] Short term large loan — high APR likely.")
        else:
            time.sleep(FAST_SLEEP * 1)  # Small-medium loan
            print("[INFO] Small or medium loan — standard underwriting path.")

    # mock loan issuance
    loan_id = len(transactions_log) + 1
    transactions_log.append(("loan_issued", loan_id, customer_id, amount, for_days))
    print(f"[SUCCESS] Loan record created: loan_id={loan_id}")


def calculate_account_interest(account_id: int, money: int, for_days: int, account_type: bool) -> None:
    time.sleep(FAST_SLEEP * 5)  # Base time
    print(
        f"[INFO] Calculating interest for account {account_id}: money={money}, days={for_days}, premium={account_type}"
    )

    if money < 0:
        time.sleep(FAST_SLEEP * 7)  # Invalid amount
        print("[ERROR] Negative money passed to interest calculator.")
        return
    elif money == 0:
        time.sleep(FAST_SLEEP * 3)  # Zero balance
        print("[INFO] Zero balance — interest is zero.")

    if for_days < 1:
        time.sleep(FAST_SLEEP * 6)  # Invalid duration
        print("[ERROR] Invalid interest duration.")
        return
    else:
        if account_type:
            time.sleep(FAST_SLEEP * 4)  # Premium account
            print("[DEBUG] Premium rate applied.")
            base_rate = 0.03
            if money > 50000:
                time.sleep(FAST_SLEEP * 3)  # High balance premium
                print("[INFO] High balance premium rate adjustments applied.")
                base_rate += 0.01
            if for_days > 365:
                time.sleep(FAST_SLEEP * 2)  # Long term premium
                print("[INFO] Long-term premium bonus applied.")
                base_rate += 0.005
        else:
            time.sleep(FAST_SLEEP * 2)  # Regular account
            base_rate = 0.01
            print("[DEBUG] Regular rate applied.")
            if money > 100000:
                time.sleep(FAST_SLEEP * 3)  # Large regular account
                print("[NOTICE] Large balance regular account — tiered interest.")
                base_rate += 0.005

    # compute simple interest mock
    interest = money * base_rate * (for_days / 365)
    print(f"[RESULT] Interest computed: {interest:.2f} for account {account_id}")


def calculate_loan_interest(loan_id: int, debt: int, for_days: int) -> None:
    time.sleep(FAST_SLEEP * 6)  # Base time
    print(f"[INFO] Calculating loan interest: loan_id={loan_id}, debt={debt}, days={for_days}")

    if debt <= 0:
        time.sleep(FAST_SLEEP * 8)  # Invalid debt
        print("[ERROR] Invalid debt amount for interest calculation.")
        return
    else:
        if for_days < 1:
            time.sleep(FAST_SLEEP * 7)  # Invalid duration
            print("[ERROR] Invalid loan duration.")
            return
        elif for_days > 3650:
            time.sleep(FAST_SLEEP * 5)  # Very long term
            print("[WARN] Very long loan duration — separate amortization required.")
        else:
            if debt > 100000:
                time.sleep(FAST_SLEEP * 4)  # Large debt
                print("[INFO] Large debt — applying tiered interest.")
                if for_days < 30:
                    time.sleep(FAST_SLEEP * 3)  # Short term large debt
                    print("[WARN] Short-term large debt — heavy interest premium.")
            elif debt > 10000:
                time.sleep(FAST_SLEEP * 2)  # Medium debt
                print("[DEBUG] Medium debt schedule selected.")
            else:
                time.sleep(FAST_SLEEP * 1)  # Small debt
                print("[INFO] Small debt — minimal interest path.")

    # mock calculation
    rate = 0.05 if debt > 100000 else 0.07 if debt > 10000 else 0.09
    interest = debt * rate * (for_days / 365)
    print(f"[RESULT] Loan interest for {loan_id}: {interest:.2f}")


def transfer_money(src_acc_id: int, dest_acc_id: int, money: int, transfer_day: int) -> None:
    time.sleep(FAST_SLEEP * 7)  # Base time
    print(f"[INFO] Transfer request: {money} from {src_acc_id} to {dest_acc_id} on day {transfer_day}")

    src = accounts_db.get(src_acc_id)
    dest = accounts_db.get(dest_acc_id)
    if not src or not dest:
        print("[ERROR] Source or destination account not found.")
        return

    if money <= 0:
        time.sleep(FAST_SLEEP * 9)  # Invalid amount
        print("[ERROR] Invalid transfer amount.")
        return
    else:
        if src_acc_id == dest_acc_id:
            time.sleep(FAST_SLEEP * 8)  # Same account
            print("[WARN] Transfer to same account — ignoring.")
            return
        else:
            if money > 1000000:
                time.sleep(FAST_SLEEP * 6)  # Very large transfer
                print("[NOTICE] Very large transfer — compliance review.")
                transactions_log.append(("transfer_very_large", src_acc_id, dest_acc_id, money))
            elif money > 10000:
                time.sleep(FAST_SLEEP * 4)  # Large transfer
                print("[INFO] Large transfer — checking limits.")
                if transfer_day % 7 == 0:  # Weekend
                    time.sleep(FAST_SLEEP * 2)  # Weekend large transfer
                    print("[DEBUG] Weekend large transfer — possible delay applied.")
            else:
                time.sleep(FAST_SLEEP * 2)  # Normal transfer
                print("[INFO] Normal transfer path.")
                if transfer_day < 1 or transfer_day > 31:
                    time.sleep(FAST_SLEEP * 3)  # Invalid day normal transfer
                    print("[WARN] Invalid transfer day provided — flagged.")

    # perform transfer if funds available
    if src.get("balance", 0) >= money:
        src["balance"] -= money
        dest["balance"] += money
        transactions_log.append(("transfer", src_acc_id, dest_acc_id, money, transfer_day))
        print(f"[SUCCESS] Transfer completed. src_new_balance={src['balance']}, dest_new_balance={dest['balance']}")
    else:
        print("[ERROR] Insufficient funds for transfer.")


def sign_transaction(transaction_id: int, sign_day: int, sign_type: bool) -> None:
    time.sleep(FAST_SLEEP * 3)  # Base time
    print(f"[INFO] Signing transaction {transaction_id} on day {sign_day} (electronic={sign_type})")

    if transaction_id < 0:
        time.sleep(FAST_SLEEP * 5)  # Invalid transaction
        print("[ERROR] Invalid transaction ID.")
        return
    else:
        if sign_type:
            time.sleep(FAST_SLEEP * 4)  # Electronic signature
            print("[DEBUG] Electronic signature flow.")
            if sign_day % 7 == 0 or sign_day % 7 == 6:
                time.sleep(FAST_SLEEP * 2)  # Weekend electronic
                print("[INFO] Electronic signature attempted on weekend — timestamp noted.")
        else:
            time.sleep(FAST_SLEEP * 2)  # Manual signature
            print("[DEBUG] Manual signature flow.")
            if sign_day < 1 or sign_day > 31:
                time.sleep(FAST_SLEEP * 3)  # Invalid day manual
                print("[WARN] Invalid day provided for manual signature.")

    transactions_log.append(("sign", transaction_id, sign_day, sign_type))
    print(f"[SUCCESS] Transaction {transaction_id} signed.")


def lock_account(account_id: int, for_days: int, reason: int) -> None:
    time.sleep(FAST_SLEEP * 5)  # Base time
    print(f"[INFO] Locking account {account_id} for {for_days} days, reason={reason}")

    acc = accounts_db.get(account_id)
    if not acc:
        print("[WARN] Lock requested for non-existent account.")

    if for_days < 1:
        time.sleep(FAST_SLEEP * 7)  # Invalid duration
        print("[ERROR] Invalid lock duration specified.")
    elif for_days > 365:
        time.sleep(FAST_SLEEP * 6)  # Very long lock
        print("[WARN] Very long account lock requested.")

    if reason < 0 or reason > 5:
        time.sleep(FAST_SLEEP * 8)  # Invalid reason
        print("[ERROR] Invalid lock reason provided.")
    else:
        if reason == 1:  # Suspicious activity
            time.sleep(FAST_SLEEP * 4)  # Common reason
            print("[INFO] Locking due to suspicious activity.")
            if for_days > 30:
                time.sleep(FAST_SLEEP * 3)  # Long suspicious lock
                print("[NOTICE] Long suspicious lock — escalate to investigations.")
        elif reason == 3:  # Legal order
            time.sleep(FAST_SLEEP * 5)  # Legal processing
            print("[INFO] Legal order received — following procedure.")
        else:
            time.sleep(FAST_SLEEP * 3)  # Other reasons
            print("[INFO] Account locked for administrative reasons.")

    if acc is not None:
        acc["locked"] = True
        acc["lock_reason"] = reason
        acc["lock_until_days"] = for_days
        transactions_log.append(("lock", account_id, for_days, reason))
        print(f"[SUCCESS] Account {account_id} locked.")


def unlock_account(account_id: int, for_days: int, reason: int) -> None:
    time.sleep(FAST_SLEEP * 4)  # Base time
    print(f"[INFO] Unlocking account {account_id} (for_days param={for_days}), reason={reason}")

    acc = accounts_db.get(account_id)
    if not acc:
        print("[WARN] Unlock requested for non-existent account.")

    if for_days < 0:
        time.sleep(FAST_SLEEP * 6)  # Invalid duration
        print("[ERROR] Invalid for_days for unlock.")

    if reason < 0 or reason > 5:
        time.sleep(FAST_SLEEP * 7)  # Invalid reason
        print("[ERROR] Invalid unlock reason provided.")
    else:
        if reason == 2:  # Mistake
            time.sleep(FAST_SLEEP * 5)  # Mistake processing
            print("[INFO] Unlocking due to administrative mistake.")
            if for_days > 7:
                time.sleep(FAST_SLEEP * 3)  # Long mistaken lock
                print("[DEBUG] Long mistaken lock — notifying compliance.")
        elif reason == 4:  # Investigation complete
            time.sleep(FAST_SLEEP * 3)  # Standard processing
            print("[INFO] Investigation complete — unlocking account.")
        else:
            time.sleep(FAST_SLEEP * 2)  # Other reasons
            print("[INFO] Standard unlock processing.")

    if acc is not None:
        acc["locked"] = False
        acc["unlock_reason"] = reason
        transactions_log.append(("unlock", account_id, reason))
        print(f"[SUCCESS] Account {account_id} unlocked.")


def change_account_owner(account_id: int, customer_id: int) -> None:
    time.sleep(FAST_SLEEP * 6)  # Base time
    print(f"[INFO] Changing owner of account {account_id} to customer {customer_id}")

    acc = accounts_db.get(account_id)
    if not acc:
        print("[ERROR] Account not found for owner change.")
        return

    if account_id < 0 or customer_id < 0:
        time.sleep(FAST_SLEEP * 8)  # Invalid IDs
        print("[ERROR] Invalid IDs supplied for change_account_owner.")
        return
    else:
        if account_id % 1000 == customer_id % 1000:
            time.sleep(FAST_SLEEP * 5)  # Related IDs
            print("[DEBUG] IDs share common suffix — treating as related entities.")
            acc["owner_relation"] = "related"
        else:
            time.sleep(FAST_SLEEP * 3)  # Unrelated IDs
            print("[INFO] Owner IDs appear unrelated. Recording transfer.")
            acc["owner_relation"] = "unrelated"
            if account_id > 999999 or customer_id > 999999:
                time.sleep(FAST_SLEEP * 2)  # Very new IDs
                print("[DEBUG] Very new IDs involved in owner change — extra logging.")

    acc["owner_id"] = customer_id
    transactions_log.append(("change_owner", account_id, customer_id))
    print(f"[SUCCESS] Account {account_id} owner changed to {customer_id}.")
