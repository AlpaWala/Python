print("Welcome to SBI ATM")

atm_balance = int(input("Enter your starting balance: "))
atm_pin = int(input("Set your ATM PIN: "))

print("\n---- LOGIN ----")
user_pin = int(input("Enter your ATM PIN: "))

if user_pin == atm_pin:

    while True:
        print("\nWelcome to Mira Road ATM")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            deposit_amount = int(input("Enter deposit amount: "))
            atm_balance = atm_balance + deposit_amount
            print("Updated balance:", atm_balance)

        elif choice == "2":
            withdraw_amount = int(input("Enter withdrawal amount: "))

            if withdraw_amount > atm_balance:
                print("Insufficient Balance")
            else:
                print("Withdrawal Successful")
                atm_balance = atm_balance - withdraw_amount
                print("Remaining balance:", atm_balance)

        elif choice == "3":
            print("Current Balance:", atm_balance)

        elif choice == "4":
            print("Thank you for using SBI ATM")
            break

        else:
            print("Invalid choice. Try again.")

else:
    print("Wrong PIN. Access Denied.")