# test.py - intentionally vulnerable for scanner testing

import subprocess
import hashlib

# SQL Injection
query = "SELECT * FROM users WHERE id = " + user_input

# Hardcoded credentials
password = "supersecret123"
api_key = "sk-abc123456789"

# Weak crypto
hash = hashlib.md5(data).hexdigest()

# Command injection
subprocess.run(user_input, shell=True)

# Debug enabled
DEBUG = True
