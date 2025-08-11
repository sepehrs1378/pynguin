# Banking simulator for MS thesis testing (visible execution)
# - Produces nested functions with configurable delays (time.sleep)
# - Generates test cases and measures execution time per transaction and per operation
# - Demonstrates slower functions and instrumentation for your algorithm benchmarking
# NOTE: This code runs a short demo. Adjust parameters for larger tests.

import time
import random
import uuid
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

random.seed(42)


class BankingSimulator:
    """
    BankingSimulator simulates processing of banking transactions.
    Key design choices:
    - process_transaction has nested functions (multi-level nesting)
    - Some nested functions are intentionally much slower (use time.sleep)
    - Configurable delays per operation to tune "hot" and "slow" functions
    - Instrumentation captures execution time per nested function and overall
    """

    def __init__(self, delays=None, enable_io_sleep=True):
        """
        delays: dict mapping operation name to delay in seconds (float)
                supported keys: 'validate', 'deep_validate', 'fraud_check',
                                'apply', 'persist', 'notify'
        enable_io_sleep: if False, sleep calls will be skipped (fast-mode)
        """
        # sensible defaults: make fraud_check and notify much slower
        default_delays = {
            "validate": 0.01,
            "deep_validate": 0.05,
            "fraud_check": 0.25,  # intentionally slow
            "apply": 0.005,
            "persist": 0.06,
            "notify": 0.18,  # slow-ish
        }
        self.delays = default_delays if delays is None else {**default_delays, **delays}
        self.enable_io_sleep = enable_io_sleep
        # simple in-memory ledger: account_id -> balance
        self.ledger = defaultdict(float)
        self.tx_log = []  # record of processed transactions

    def _sleep(self, sec):
        if self.enable_io_sleep and sec > 0:
            time.sleep(sec)

    def seed_accounts(self, accounts):
        """Initialize ledger with accounts: dict account_id -> balance"""
        for acc, bal in accounts.items():
            self.ledger[acc] = bal

    def generate_test_cases(self, num_accounts=10, num_transactions=100, amount_range=(1, 1000)):
        """
        Generate a list of transactions to feed the simulator.
        Each tx is a dict: {id, from_acct, to_acct, amount, currency, metadata}
        """
        accounts = [f"ACC{str(i).zfill(4)}" for i in range(num_accounts)]
        # give some accounts higher balances to create skew
        for i, acc in enumerate(accounts):
            self.ledger[acc] = 10000.0 if i < 2 else 1000.0  # first 2 are rich accounts

        txs = []
        for _ in range(num_transactions):
            a = random.choice(accounts)
            b = random.choice(accounts)
            # avoid same-account transfer sometimes
            if random.random() < 0.1:
                b = a
            tx = {
                "id": str(uuid.uuid4()),
                "from": a,
                "to": b,
                "amount": round(random.uniform(*amount_range), 2),
                "currency": "EUR",
                "metadata": {"priority": random.choice(["low", "normal", "high"])},
            }
            txs.append(tx)
        return txs

    def process_transaction(self, tx, skip_slow_checks=False):
        """
        Process a single transaction.
        Nested functions inside to emulate deep call stacks. The algorithm you're testing
        can call process_transaction with skip_slow_checks=True to emulate optimization.

        Returns a dict with timing breakdown and result status.
        """
        timings = {}
        start_all = time.perf_counter()

        # Level 1 nested: validation
        def validate(transaction):
            t0 = time.perf_counter()

            # Level 2 nested: deep validation (more expensive)
            def deep_validate(tr):
                t1 = time.perf_counter()
                # simulate checks: schema, business rules, KYC references, etc.
                self._sleep(self.delays["deep_validate"])
                t2 = time.perf_counter()
                timings["deep_validate"] = t2 - t1
                return True

            # quick checks
            self._sleep(self.delays["validate"])
            ok = True
            timings_local = {}
            if ok:
                deep_validate(transaction)
            t1 = time.perf_counter()
            timings["validate"] = t1 - t0
            return True

        # Level 1 nested: fraud detection (intentionally slow)
        def fraud_check(transaction):
            t0 = time.perf_counter()
            # deep/heuristic fraud check (very slow)
            self._sleep(self.delays["fraud_check"])
            # small probabilistic "flag" for demonstration
            flagged = transaction["amount"] > 900 and random.random() < 0.6
            t1 = time.perf_counter()
            timings["fraud_check"] = t1 - t0
            return not flagged  # return True if NOT fraudulent

        # Level 1 nested: apply transaction to ledger (fast)
        def apply(tr):
            t0 = time.perf_counter()
            self._sleep(self.delays["apply"])
            # simple transfer semantics: allow same-account transfers
            if self.ledger[tr["from"]] >= tr["amount"] or tr["from"] == tr["to"]:
                self.ledger[tr["from"]] -= tr["amount"]
                self.ledger[tr["to"]] += tr["amount"]
                res = True
            else:
                res = False  # insufficient funds
            t1 = time.perf_counter()
            timings["apply"] = t1 - t0
            return res

        # Level 1 nested: persist (moderate)
        def persist(tr, status):
            t0 = time.perf_counter()
            self._sleep(self.delays["persist"])
            # append to tx_log as "persistence"
            self.tx_log.append({"tx": tr, "status": status, "ts": time.time()})
            t1 = time.perf_counter()
            timings["persist"] = t1 - t0
            return True

        # Level 1 nested: notify (slow, e.g., external push/email)
        def notify(tr, status):
            t0 = time.perf_counter()
            self._sleep(self.delays["notify"])
            # pretend to send push/email; here we just return success
            t1 = time.perf_counter()
            timings["notify"] = t1 - t0
            return True

        # --- Execution flow ---
        ok = validate(tx)
        if not ok:
            result = "validation_failed"
            persist(tx, result)
            end_all = time.perf_counter()
            timings["total"] = end_all - start_all
            return {"txid": tx["id"], "result": result, "timings": timings}

        # Option to skip slow checks (simulates algorithm optimization)
        if not skip_slow_checks:
            ok_fraud = fraud_check(tx)
            if not ok_fraud:
                result = "fraud_detected"
                persist(tx, result)
                notify(tx, result)
                end_all = time.perf_counter()
                timings["total"] = end_all - start_all
                return {"txid": tx["id"], "result": result, "timings": timings}
        else:
            # record that fraud_check was skipped
            timings["fraud_check"] = 0.0

        applied = apply(tx)
        result = "applied" if applied else "rejected_insufficient_funds"
        persist(tx, result)
        # Optionally avoid notify to save time when not needed
        if tx["metadata"].get("priority", "normal") == "high":
            notify(tx, result)
        else:
            # normal priority: simulate deferred notification (we still account for small time)
            self._sleep(0.002)
            timings["notify"] = 0.002

        end_all = time.perf_counter()
        timings["total"] = end_all - start_all
        return {"txid": tx["id"], "result": result, "timings": timings}

    def run_batch(self, txs, skip_slow_checks_for=None, max_workers=1):
        """
        Process a batch of transactions.
        skip_slow_checks_for: a function(tx) -> bool; if True, skip slow checks for that tx.
        max_workers: if >1, uses ThreadPoolExecutor to simulate concurrent processing.

        Returns list of results (in order of completion) and aggregated metrics.
        """
        results = []

        # helper wrapper to pass skip flag per tx
        def _worker(tx):
            skip = False
            if skip_slow_checks_for:
                try:
                    skip = bool(skip_slow_checks_for(tx))
                except Exception:
                    skip = False
            return self.process_transaction(tx, skip_slow_checks=skip)

        if max_workers == 1:
            for tx in txs:
                results.append(_worker(tx))
        else:
            with ThreadPoolExecutor(max_workers=max_workers) as ex:
                futures = {ex.submit(_worker, tx): tx for tx in txs}
                for fut in as_completed(futures):
                    results.append(fut.result())
        # compute simple aggregate metrics
        agg = {
            "count": len(results),
            "avg_total_time": sum(r["timings"]["total"] for r in results) / max(1, len(results)),
            "avg_deep_validate": sum(r["timings"].get("deep_validate", 0) for r in results) / max(1, len(results)),
            "avg_fraud_check": sum(r["timings"].get("fraud_check", 0) for r in results) / max(1, len(results)),
        }
        return results, agg


# # ---------------- Demo run ----------------
# sim = BankingSimulator()
# txs = sim.generate_test_cases(num_accounts=8, num_transactions=30, amount_range=(1, 1200))

# # Define a simple strategy for skipping slow checks:
# # Skip fraud check if amount < 500 and priority is low
# def skip_strategy(tx):
#     return (tx['amount'] < 500 and tx['metadata'].get('priority') == 'low')

# print("Running baseline (no skip) with single-threaded execution...")
# results_baseline, agg_baseline = sim.run_batch(txs, skip_slow_checks_for=None, max_workers=1)
# print(f"Baseline aggregated metrics: {agg_baseline}")

# # Clear tx_log for next run but keep ledger state
# sim.tx_log = []

# print("\nRunning optimized (skip some slow checks) with same workload...")
# results_opt, agg_opt = sim.run_batch(txs, skip_slow_checks_for=skip_strategy, max_workers=1)
# print(f"Optimized aggregated metrics: {agg_opt}")

# # Show top 5 slowest transactions by total time in baseline
# sorted_baseline = sorted(results_baseline, key=lambda r: r['timings']['total'], reverse=True)
# print("\nTop 5 slowest transactions (baseline):")
# for item in sorted_baseline[:5]:
#     print(item['txid'], item['result'], f"total={item['timings']['total']:.3f}s",
#           f"fraud_check={item['timings'].get('fraud_check',0):.3f}s")

# # Return the simulator object for further interactive use if needed
# sim, results_baseline[:3], results_opt[:3], agg_baseline, agg_opt
