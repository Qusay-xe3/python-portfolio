#access_check.py

MAX_FAILED = 5

role = input("role:")
mfa_passed = input("mfa passed (yes/no):")
failed_attempts = int(input("failed attempts:"))

mfa_ok = mfa_passed == "yes"
privileged_role = role == "admin" or "root"
can_log_in = mfa_passed == "yes" and failed_attempts < MAX_FAILED

print (f"Role:{role}")
print (f"MFA passed(yes/no): {mfa_passed}")
print (f"Failed attempts: {failed_attempts}")
print (f"MFA ok: {mfa_ok}")
print (f"Privileged role: {privileged_role}")
print (f"Can log in: {can_log_in}")