
# Online Python - IDE, Editor, Compiler, Interpreter

import hashlib

# Security Hotspot: Using weak hashing algorithm (MD5) for sensitive data
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')

raise "Something went wrong"  # Noncompliant: a string is not a valid exception

def fun(a):
  i = 10
  return i + a       # Noncompliant
  i += 1             # this is never executed
