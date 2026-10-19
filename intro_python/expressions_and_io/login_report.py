# login_report.py
# print report about status login

MAX_LOGIN_ATTEMPTS = 5
print()
username = input("Username: ")
failed = int(input("enter number of faild attempts"))
print()
remaining_attempts = MAX_LOGIN_ATTEMPTS - failed
print()
print ("=" *30)
print ("LOGIN REPORT")
print ("=" *30)
print()

print(f"User:\t\t{username}")
print(f"Failed:\t\t{failed}")
print(f"remaining attempts:\t{remaining_attempts}")
