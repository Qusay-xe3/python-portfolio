#port_classifier.py
#

port = int(input("enter the port: "))

if port < 0 or port > 65535:
   print ("Invalid port: use a number from 0 to 65535.")
elif port >= 0 and port <= 1023:
   print ("Range: system")
elif port >= 1024 and port <= 49151:
   print ("Range: user")
elif port > 49151:
   print ("Range: dynamic or private")

if port == 20: 
   print("Service: ssh")
elif port == 80: 
   print("Service: http")
elif port == 443: 
   print("Service: https")