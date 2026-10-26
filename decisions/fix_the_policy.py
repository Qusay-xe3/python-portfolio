# fix_the_policy.py
# Check a new password against an example policy and classify its length.
MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")
#SyntaxError: Because he did not add two vertical colons at the end of the condition.
if len(password) < MIN_LENGTH:
    print("- Too short.")
#SemanticError: 
    if password == username:
       print("- Same as the username.")

if len(password) >= MIN_LENGTH:
    strength = "acceptable"
#SemanticError:
    print (f"Length: {len(password)} ({strength})")
elif len(password) >= 16:
    strength = "long"
#SemanticError:
    print (f"Length: {len(password)} ({strength})")
else:
    strength = "short"
    print (f"Length: {len(password)} ({strength})")