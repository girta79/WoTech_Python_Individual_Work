# Easy level:

print("Welcome to the Bank!")
balance = 0

while True:
    deposit = input("Please enter the amount of money(€) you want to deposit: ")

    # add to the balance 
    balance += int(deposit)

    put_deposit = input("Do you want to make another deposit? Type 'yes' to continue or 'no' to exit: ")

    if put_deposit.lower() != 'yes':
        print(f"Thank you! Your total balance is: {balance}€")
        break 



# Medium level:

print("Welcome to the Bank!")
balance = 0

while True:
    try:
        deposit = input("Please enter the amount of money(€) you want to deposit: ")
        balance += int(deposit)
    except:
        print("Please enter a valid number/integer")

    put_deposit = input("Do you want to make another deposit? Type 'yes' to continue or 'no' to exit: ")

    if put_deposit.lower() != 'yes':
        print(f"Thank you! Your total balance is: {balance}€")
        break 



# Hard level:

print("Welcome to the Bank!")
balance = 0

while True:
    print("\nWhat would you like to do?")
    print("1. Deposit money")
    print("2. Withdraw money")
    print("3. Check balance")
    print("4. Exit")
    
    choice = input("Please enter a number between 1 and 4: ")

    if choice == '1':
        try:
            deposit = input("Please enter the amount of money(€) you want to deposit: ")
            balance += int(deposit)
            print(f"Deposit successful! Your new balance is: {balance}€")
        except:
            print("Please enter a valid number/integer")

    elif choice == '2':
        try:
            withdrawal = int(input("Please enter the amount of money(€) you want to withdraw: "))
            if balance >= withdrawal:
                balance -= withdrawal
                print(f"Withdrawal successful! Your new balance is: {balance}€")
            else:
                print("Insufficient funds! Withdrawal not possible")
        except:
            print("Please enter a valid number/integer")

    elif choice == '3':
        print(f"Your current balance is: {balance}€")

    elif choice == '4':
        print(f"Thank you! Your total balance is: {balance}€")
        break

    else:
        print("Invalid entry. Please enter a number between 1 and 4")


