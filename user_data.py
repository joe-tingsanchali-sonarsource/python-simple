import hashlib
import sqlite3
import os
import tempfile

# VULNERABILITY: Weak cryptographic hash — MD5 is broken (sonar: python:S4790)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # MD5 is cryptographically weak


# VULNERABILITY: SQL injection — user input concatenated directly into query (sonar: python:S3649)
def get_user(conn, username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"  # SQL injection
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchone()


# VULNERABILITY: Hard-coded credentials (sonar: python:S2068)
DB_PASSWORD = "admin123"  # Hard-coded secret
API_KEY = "sk-abc123supersecretkey"  # Hard-coded API key


# VULNERABILITY: Predictable temporary file — race condition (sonar: python:S5443)
def write_temp_data(data):
    tmp_path = "/tmp/calc_temp.txt"  # Predictable path, insecure
    with open(tmp_path, "w") as f:
        f.write(data)
    return tmp_path


# BUG: Null dereference — return value not checked before use (sonar: python:S2259)
def process_user(conn, username):
    user = get_user(conn, username)
    print(user["email"])  # KeyError / TypeError if user is None


# BUG: Identical conditions — second branch is unreachable (sonar: python:S1862)
def classify_score(score):
    if score > 90:
        return "A"
    elif score > 90:   # Dead condition — identical to the one above
        return "A+"
    elif score > 75:
        return "B"
    else:
        return "C"


# BUG: Empty function body with no-op pass (sonar: python:S1186)
def validate_input(value):
    pass  # Validation not implemented


# VULNERABILITY: Use of assert for security logic — stripped in optimised builds (sonar: python:S5905)
def transfer_funds(amount, account):
    assert amount > 0, "Amount must be positive"  # assert can be disabled with -O flag
    assert account is not None, "Account required"
    print(f"Transferring {amount} to {account}")
