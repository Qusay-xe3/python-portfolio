#password_check.py

def long_enough(password, minimum=8):
    """Returns True if the password is long enough"""
    if len(password) >= minimum:
        return True
    else:
        return False

def differs_from_username(password, username):
     """Returns True if the password is different from the username"""
     if password != username:
            return True
     else:
            return False

def password_ok(password, username): 
    """Returns True if the password is long enough and different from the username"""
    if long_enough(password, minimum=8) and differs_from_username(password, username):
         return True
    else:
         return False

username = input("username: ")
password = input("Password: ")

password_ok(password, username)

if password_ok(password, username):
     print("Password accepted.")
else:
    print("Password rejected.")