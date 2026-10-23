# fix_the_rules.py
# This program checks a connection against three rules.

role = input("Role: ")
# runtime error: Because it did not convert the input value type to an integer
port = int(input("Port: "))

# syntax error: Because we want the output data type to be Boolean, but it loads the value as a string. 
is_admin = role == "admin"

# runtime error: Because he placed the < sign after the equals sign, not before it. 
is_system_port = port <= 1023

# semantic error: Because he did not place the second part of the "or" correctly.
is_web_port = port == 80 or port == 443

print(f"Admin: {is_admin}")

print(f"System port: {is_system_port}")

print(f"Web port: {is_web_port}")
