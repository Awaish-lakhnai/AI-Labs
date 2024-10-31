def login():
    correct_username = "admin"
    correct_password = 12345
    username = input("Enter username: ")
    try:
        password = int(input("Enter password: "))
    except ValueError:
        print("Password should be a numeric value.")
        return
    if username == correct_username and password == correct_password:
        print("Login Successful!")
    elif username != correct_username:
        print("Incorrect username")
    elif password != correct_password:
        print("Incorrect password")
login()
