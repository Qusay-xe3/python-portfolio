# fix_the_rules.py

# This program checks a connection against three rules.

role = input("Role: ")

port = input("Port: ")

#semantic error: Because we want the output data type to be Boolean, but it loads the value as a string. 
is_admin = role == "admin"

#syntax error: Because he placed the < sign after the equals sign, not before it. 
is_system_port = port <= 1023

is_web_port = port == 80 or 443

print(f"Admin: {is_admin}")

print(f"System port: {is_system_port}")

print(f"Web port: {is_web_port}")
