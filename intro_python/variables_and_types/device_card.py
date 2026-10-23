#device_card.py
#A log that displays the device status.

MAX_CONNECTIONS = 5
device_name = "Qusay_pc"
device_ip = "192.0.2.28"
service = "HTTPS"
open_port = 234
print ("Device_Name:",device_name)
print ("Device_IP:",device_ip)
print ("Service:",service)
print ("Max_Connections:",MAX_CONNECTIONS)
print ("Port:",open_port)

service = "SSH"
open_port = 22
print ("Updated service:",service,"on port",open_port)
