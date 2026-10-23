# fix_the_record.py
# This program prints a short record about a network device.

# fix_the_record.py
# This program prints a short record about a network device.

device_name = "edge-router"

# syntax error
nd_ip = "192.0.2.1"

# syntax error
class_name = "router"

# runtime error
port = int(22)

# syntax error
print("Device:", device_name)

# runtime error
print("Backup IP:", nd_ip)

print("Type:", class_name)
print("Port:", port)

'''python discovery syntax error before runtime error because it checks
 the code grammar before running any lines. Runtime errors only appear when
   Python actually tries to execute that specific line.'''
