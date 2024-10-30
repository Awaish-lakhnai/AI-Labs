# Define correct username and password
correct_username = "Awaish"
correct_password = 1234

# Ask user to enter username and password
username = input("Enter username: ")
password = int(input("Enter password: "))

# Check if both username and password are correct
if username == correct_username and password == correct_password:
    print("Login successful")
elif username != correct_username:
    print("Incorrect username")
else:
    print("Incorrect password")