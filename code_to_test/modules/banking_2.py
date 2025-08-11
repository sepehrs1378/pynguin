import time
import math
from typing import List, Dict, Optional
from dataclasses import dataclass

MUL = 10


@dataclass
class Transaction:
    amount: float
    type: str  # 'deposit', 'withdrawal', 'transfer'
    timestamp: float
    description: str


class BankAccount:
    def __init__(self, account_number: str, account_holder: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history: List[Transaction] = []
        self.risk_score = 0  # Simulated risk profile

    def _calculate_deposit_delay(self, amount: float) -> float:
        """More delay for larger deposits and risky accounts"""
        base_delay = 0.01
        amount_factor = min(amount / 100000, 0.2)  # Up to 2 seconds for very large deposits
        risk_factor = self.risk_score / 1000
        return base_delay + amount_factor + risk_factor

    def deposit(self, amount: float, description: str = "") -> bool:
        if amount <= 0:
            return False

        # Delay based on amount and account risk
        delay = self._calculate_deposit_delay(amount)
        time.sleep(delay * MUL)

        self.balance += amount
        self.transaction_history.append(Transaction(amount, "deposit", time.time(), description))

        # Increase risk score for large deposits
        if amount > 5000:
            self.risk_score += amount / 1000
            time.sleep(0.02 * MUL)  # Additional security check

        return True

    def _calculate_withdrawal_delay(self, amount: float) -> float:
        """More delay when withdrawing large amounts or overdraft attempts"""
        base_delay = 0.015
        amount_factor = math.log10(max(amount, 1)) * 0.03  # Logarithmic scaling
        overdraft_penalty = 0.05 if amount > self.balance else 0
        return base_delay + amount_factor + overdraft_penalty

    def withdraw(self, amount: float, description: str = "") -> bool:
        if amount <= 0:
            return False

        # Significant delay if this would overdraft
        if amount > self.balance:
            time.sleep(0.1 * MUL)  # Special overdraft consideration delay
            return False

        delay = self._calculate_withdrawal_delay(amount)
        time.sleep(delay * MUL)

        self.balance -= amount
        self.transaction_history.append(Transaction(amount, "withdrawal", time.time(), description))

        # Large withdrawals trigger additional checks
        if amount > 3000:
            time.sleep(0.05 * MUL)  # Fraud verification

        return True

    def get_balance(self, detailed: bool = False) -> float:
        """More delay for detailed balance checks"""
        if detailed:
            time.sleep(0.03 * MUL)  # Detailed verification
            return round(self.balance, 2)
        else:
            time.sleep(0.005 * MUL)  # Quick check
            return self.balance

    def get_transaction_history(self, days: int = 30) -> List[Transaction]:
        """Delay scales with requested time period and transaction count"""
        if days <= 0:
            return []

        # Base delay plus time-based scaling
        delay = 0.02 + (days / 30) * 0.05
        time.sleep(min(delay, 0.3) * MUL)  # Cap at 3 seconds

        # Simulate processing more transactions takes longer
        relevant_txs = [t for t in self.transaction_history if time.time() - t.timestamp <= days * 86400]
        processing_delay = len(relevant_txs) * 0.001
        time.sleep(min(processing_delay, 0.1) * MUL)

        return relevant_txs


class Bank:
    def __init__(self):
        self.accounts: Dict[str, "BankAccount"] = {}
        self.maintenance_mode = False

    def _generate_account_number(self) -> str:
        """Delay increases with number of existing accounts"""
        time.sleep((len(self.accounts) * 0.001 + 0.01) * MUL)
        return f"ACCT{len(self.accounts) + 100000:06d}"

    def create_account(self, account_holder: str, initial_balance: float = 0.0) -> Optional[BankAccount]:
        """More delay for high initial balances"""
        if self.maintenance_mode:
            time.sleep(0.5 * MUL)  # Extended delay during maintenance
            return None

        # Initial validation delay
        time.sleep(0.02 * MUL)

        # Additional checks for large initial deposits
        if initial_balance > 10000:
            time.sleep(0.2 * MUL)  # Compliance check
        elif initial_balance > 5000:
            time.sleep(0.1 * MUL)

        account_number = self._generate_account_number()
        new_account = BankAccount(account_number, account_holder, initial_balance)
        self.accounts[account_number] = new_account

        # Risk scoring for new accounts
        if initial_balance > 20000:
            new_account.risk_score = 50
            time.sleep(0.05 * MUL)  # Enhanced due diligence

        return new_account

    def transfer(self, from_acct: str, to_acct: str, amount: float, description: str = "") -> bool:
        """Transfer delay depends on amount, accounts, and risk profiles"""
        if from_acct not in self.accounts or to_acct not in self.accounts:
            time.sleep(0.03 * MUL)  # Account lookup delay
            return False

        from_account = self.accounts[from_acct]
        to_account = self.accounts[to_acct]

        # Base transfer delay
        time.sleep(0.04 * MUL)

        # Amount-based delay (logarithmic scaling)
        amount_delay = math.log10(max(amount, 1)) * 0.04
        time.sleep(amount_delay * MUL)

        # Risk-based delays
        risk_delay = (from_account.risk_score + to_account.risk_score) / 1000
        time.sleep(risk_delay * MUL)

        # International transfer simulation
        if description and "international" in description.lower():
            time.sleep(0.2 * MUL)  # Additional compliance checks

        # Perform the actual transfer
        if not from_account.withdraw(amount, f"Transfer to {to_acct}: {description}"):
            return False

        if not to_account.deposit(amount, f"Transfer from {from_acct}: {description}"):
            # Rollback if deposit fails
            from_account.deposit(amount, "Transfer rollback")
            return False

        return True

    def calculate_interest(self, account_number: str, days: int = 30) -> float:
        """Interest calculation with computational delay"""
        if account_number not in self.accounts:
            return 0.0

        account = self.accounts[account_number]

        # Delay based on transaction history size
        history_size = len(account.transaction_history)
        delay = min(history_size * 0.0005, 0.15)
        time.sleep(delay * MUL)

        # Simulate complex interest calculation
        balance = account.get_balance()
        if balance < 1000:
            time.sleep(0.01 * MUL)
            return 0.0
        elif balance < 5000:
            time.sleep(0.03 * MUL)
            return balance * 0.01 * (days / 365)
        else:
            # Tiered interest calculation
            time.sleep(0.05 * MUL)
            tier1 = min(balance, 5000) * 0.015
            tier2 = max(balance - 5000, 0) * 0.02
            return (tier1 + tier2) * (days / 365)

    def generate_statement(self, account_number: str, detailed: bool = False) -> Dict:
        """Statement generation with quality-of-service delay"""
        if account_number not in self.accounts:
            return {}

        account = self.accounts[account_number]

        # Base delay
        time.sleep(0.03 * MUL)

        # Detailed statements take longer
        if detailed:
            time.sleep((0.05 + len(account.transaction_history) * 0.002) * MUL)

            return {
                "account": account_number,
                "holder": account.account_holder,
                "balance": account.get_balance(True),
                "transactions": account.get_transaction_history(30),
                "risk_score": account.risk_score,
                "generated_at": time.time(),
            }
        else:
            time.sleep(0.02 * MUL)
            return {
                "account": account_number,
                "holder": account.account_holder,
                "balance": account.get_balance(),
                "transaction_count": len(account.transaction_history),
                "generated_at": time.time(),
            }
