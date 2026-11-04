#lock_tools.py

def is_locked(failed, max_tries=3):
    """Returns True or False if the lock is locked or not"""
    if failed >= max_tries:
        return True
    else:
         return False

def tries_left(failed, max_tries=3):
    """Returns the number of trieds left"""
    if failed >= max_tries:
        return 0
    else:
        return max_tries - failed

def status(failed):
    """Returns the status of the lock"""
    tries_left(failed)
    left = tries_left(failed)
    if left == 0:
        return "Locked"
    else:
        return (f"active ({left} tries left)")

print(is_locked(2))
print(is_locked(3))
print(is_locked(3, 5))
print(tries_left(1))
print(tries_left(7))
print(status(1))
print(status(4))