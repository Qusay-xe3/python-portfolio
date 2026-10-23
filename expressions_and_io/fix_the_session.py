# fix_the_session.py
# This program reports a user's session time.

username = input("Username: ")

# Runtime error
total_seconds = int(input("Session length in seconds: "))

# Semantic error
minutes = total_seconds // 60
seconds = total_seconds % 60

print("=" * 30)

# Semantic error
print(f"User: {username}")

# Runtime error
print("Session: " + str(minutes) + " min " + str(seconds) + " s")

print("=" * 30)