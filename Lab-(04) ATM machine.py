def atm_program():
    correct_pin = 1234
    balance = 1000
    try:
        pin = int(input("Enter your PIN: "))
    except ValueError:
        print("Invalid input. PIN must be numeric.")
        return
    if pin == correct_pin:
        print("PIN accepted.\n")
        while True:
            print("ATM Menu:\n1. Check Balance\n2. Withdraw Money")
            try:
                choice = int(input("Select an option (1 or 2): "))
            except ValueError:
                print("Invalid option. Enter 1 or 2.")
                continue
            if choice == 1:
                print(f"Your balance is: ${balance}")
            elif choice == 2:
                try:
                    withdraw_amount = float(input("Enter amount to withdraw: $"))
                except ValueError:
                    print("Invalid amount.")
                    continue
                if 0 < withdraw_amount <= balance:
                    balance -= withdraw_amount
                    print(f"${withdraw_amount} withdrawn. New balance: ${balance}")
                else:
                    print("Insufficient balance or invalid amount.")
            else:
                print("Invalid option.")
    else:
        print("Incorrect PIN. Access denied.")
atm_program()