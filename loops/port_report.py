#port_report.py

start_port = int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: "))
ports_checked = 0
for port in range(start_port, end_port + 1):
    if 0 <= port <= 1023:
        print(f"{port}: system")
        ports_checked += 1
    elif 1024 <= port <= 49151:
        print(f"{port}: user")
        ports_checked += 1
    elif 49152 <= port <= 65535:
        print(f"{port}: dynamic")
        ports_checked += 1

print(f"Ports checked: {ports_checked}")