"""
accounts module: handles balances and transactions.
"""
from typing import Dict

# In-memory balance record: customer_id -> balance
balance_record: Dict[str, float] = {}


def _ensure_account(customer_id: str) -> None:
    """Initialize balance to 0.0 if the account is not present."""
    if customer_id not in balance_record:
        balance_record[customer_id] = 0.0


def check_balance(customer_id: str) -> float:
    """Return the current balance for the given customer_id."""
    _ensure_account(customer_id)
    return balance_record[customer_id]


def deposit(customer_id: str, amount: float) -> float:
    """
    Add amount to the user's balance. Returns updated balance.
    Raises ValueError on invalid amount.
    """
    if amount <= 0:
        raise ValueError("Deposit amount must be positive.")
    _ensure_account(customer_id)
    balance_record[customer_id] += float(amount)
    return balance_record[customer_id]


def withdraw(customer_id: str, amount: float) -> float:
    """
    Deduct amount from the user's balance if sufficient funds.
    Returns updated balance. Prints 'Insufficient balance' if not enough funds (per spec)
    and leaves balance unchanged.
    Raises ValueError on invalid amount.
    """
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")
    _ensure_account(customer_id)
    if balance_record[customer_id] < amount:
        print("Insufficient balance")
        return balance_record[customer_id]
    balance_record[customer_id] -= float(amount)
    return balance_record[customer_id]
