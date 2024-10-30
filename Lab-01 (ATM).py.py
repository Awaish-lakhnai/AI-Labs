correct_username = "Awaish"
   correct_password = 1234
username = input("Enter username: ")
   password = int(input("Enter password: "))
         if username == correct_username and password == correct_password:
    print("Login successful")
elif username != correct_username:
    print("Incorrect username")
else:
    print("Incorrect password")
