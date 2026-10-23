# access_check.py
# This file takes user inputs and checks their permissions and security status to determine login eligibility.
MAX_FAILED = 5

role = input("role: ")
mfa_passed = input("MFA passed (yes/no): ")
failed_attempts = int(input("failed attempts: "))

mfa_ok = mfa_passed == "yes"
is_privileged = role == "admin" or role == "root"
can_log_in = mfa_ok and failed_attempts < MAX_FAILED

print(f"MFA OK: {mfa_ok}\nPrivileged role: {is_privileged}\nCan log in: {can_log_in}")