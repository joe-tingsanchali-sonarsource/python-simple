import subprocess
import pickle
import random

# BUG: Division by zero — no guard for empty list (sonar: python:S2190)
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num

    average = total / len(numbers)  # ZeroDivisionError when numbers is empty
    return average


# VULNERABILITY: OS command injection — user input passed directly to shell (sonar: python:S2076)
def run_calculator_command(user_input):
    result = subprocess.run(user_input, shell=True, capture_output=True)  # Injection risk
    return result.stdout


# VULNERABILITY: Insecure deserialization — pickle.loads on untrusted data (sonar: python:S5135)
def load_calculation_state(data):
    return pickle.loads(data)  # Arbitrary code execution risk


# BUG: Resource leak — file handle never closed (sonar: python:S2095)
def save_result(filename, result):
    f = open(filename, "w")
    f.write(str(result))
    # f.close() intentionally omitted — resource leak


# BUG: Dead code / useless assignment — result assigned but never used (sonar: python:S1854)
def add(a, b):
    result = a - b   # Wrong operation; value is overwritten immediately
    result = a + b
    return result


# BUG: Broad exception clause swallows all errors silently (sonar: python:S110)
def divide(a, b):
    try:
        return a / b
    except:  # Too broad — catches BaseException including SystemExit
        pass


# SECURITY HOTSPOT: Weak PRNG used for sensitive token generation (sonar: python:S2245)
# random.random() is not cryptographically secure — use secrets module instead
def generate_calculation_token():
    token = random.randint(100000, 999999)
    return token


my_list = []  # The bug is triggered here
result = calculate_average(my_list)
print(f"The average is: {result}")
print(f"Token: {generate_calculation_token()}")
