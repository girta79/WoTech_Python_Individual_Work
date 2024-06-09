# INDIVIDUAL TASK

# Create a program where the user can input deposits into a bank account. The program should use if-else statements,
# input(), int() and while True loop to keep track of deposits.

# Instructions:
# Easy level:
# 1. Welcome the user to the bank
# 2. Initiate balance = 0
# 3. Ask the user to input the amount of money they want to deposit.
# 4. Add the deposit amount to the total balance
# 5. Ask the user if they want to make another deposit or exit the bank.
# 6. If they choose to make another deposit, repeat the process (while True).
# 7. If not, print the total amount deposited and exit the bank.

# Medium level:
# 1. Use try and except to handle non-integer inputs for deposits.

# Hard level:
# 1. Add bank withdrawal (if user wants to withdraw money the balance decreases)
# 2. If the balance becomes negative, withdrawal is not possible.
# 3. Add check balance optionality Example for hard level: print("\nWhat would you like to do?") print("1. Deposit money") print("2. Withdraw money") print("3. Check balance") print("4. Exit")


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


