"""
bankcore module: handles users and authentication.
"""
from typing import Dict, Optional, Tuple

# Fixed branch id per spec
branch_id: int = 2057

# In-memory "database"
_users_info: Dict[str, Dict[str, str]] = {}  # customer_id -> {"name": str, "password": str}
_user_counter: int = 0  # used to generate sequential user numbers


def generate_customer_id() -> str:
    """
    Generate a new customer_id using the format <branch_id>-<user number>.
    Example: "2057-1"
    """
    global _user_counter
    _user_counter += 1
    return f"{branch_id}-{_user_counter}"


def create_account(name: str, customer_id: str, password: str) -> str:
    """
    Register a new user using a provided customer_id (per assignment signature).
    Returns the customer_id on success.
    Raises ValueError if the id already exists or inputs are invalid.
    """
    if not name or not password:
        raise ValueError("Name and password are required.")
    if customer_id in _users_info:
        raise ValueError("Customer ID already exists.")

    _users_info[customer_id] = {"name": name.strip(), "password": password}
    return customer_id


def create_account_auto(name: str, password: str) -> str:
    """
    Convenience helper that auto-generates the customer_id, then creates the account.
    Returns the new customer_id.
    """
    cid = generate_customer_id()
    return create_account(name=name, customer_id=cid, password=password)


def login(customer_id: str, password: str) -> bool:
    """
    Validate credentials. Returns True if valid else False.
    Prints 'Invalid login' when credentials do not match (per spec).
    """
    record = _users_info.get(customer_id)
    if not record or record.get("password") != password:
        print("Invalid login")
        return False
    return True


def get_user_name(customer_id: str) -> Optional[str]:
    """Return the user's name if the customer exists."""
    rec = _users_info.get(customer_id)
    return rec["name"] if rec else None
