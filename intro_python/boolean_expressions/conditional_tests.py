#conditional_tests.py

user = "analyst"
role = "viewer"
failed = 3
port = 22

print ("\nIs port >= 22? I predict True.")
print (port >= 22)

print ("\nIs user == analyst? I predict True.")
print (user == "analyst")

print ("\nIs port <= 22? I predict True.")
print (port <= 22)

print ("\nIs failed > 2? I predict True.")
print (failed > 2)

print ("\nIs role != admin? I predict True. ")
print (role != "admin")

print ("\nIs port < 20? I predict False.")
print (port < 20)

print ("\nIs port == 3 and failed >=3? I predict False")
print (port == 3 and failed >=3)

print ("\nIs not port ==22? I predict False")
print (not port ==22)

print ("\nIs not user == analyst or port > 23? I predict False")
print (not user == "analyst" or port > 23)

print ("\nIs failed == 235? I predict False")
print (failed == 235)