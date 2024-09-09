# ATM Simulation

import time

def atm_machine():
    # Display a message and wait for 5 seconds to simulate card insertion
    print("Please insert your CARD")
    time.sleep(5)
    
    # Initial setup: password, balance, and transaction history
    password = 1234
    balance = 25000
    transaction_history = []
    
    
    try:
        pin = int(input("Enter your ATM PIN: ")) # Request the user to enter their PIN
    except ValueError:
        # Handle case where PIN is not a valid number
        print("Invalid PIN format. Please enter a numeric PIN.")
        return
    
    # Check if the entered PIN is correct
    if pin != password:
        print("Wrong PIN. Please try again.")
        return

    # Main loop for ATM operations
    while True:
        # Display the menu options to the user
        print("""
            1 - Check balance
            2 - Withdraw balance
            3 - Deposit balance
            4 - View transaction history
            5 - Change PIN
            6 - Exit
        """)
        
       
        try:
            option = int(input("Please enter your choice: "))  # Request user to select an option
        except ValueError:
            # Handle case where input is not a valid number
            print("Invalid option. Please enter a number between 1 and 6.")
            continue
        
        
        if option == 1: # Option 1: Check balance
            print(f"Your current balance is ${balance:.2f}")
        
        
        elif option == 2: # Option 2: Withdraw funds
            try:
                withdraw_amount = float(input("Please enter amount to withdraw: "))
                # Check if withdrawal amount is valid
                if withdraw_amount > balance:
                    print("Insufficient funds.")
                elif withdraw_amount <= 0:
                    print("Invalid withdrawal amount. Please enter a positive number.")
                else:
                    balance -= withdraw_amount
                    transaction_history.append(f"Withdrawn: ${withdraw_amount:.2f}")
                    print(f"${withdraw_amount:.2f} has been debited from your account.")
                    print(f"Your updated balance is ${balance:.2f}")
            except ValueError:
                # Handle case where withdrawal amount is not a valid number
                print("Invalid amount. Please enter a numeric value.")
        
        # Option 3: Deposit funds
        elif option == 3: # Option 3: Deposit funds
            try:
                deposit_amount = float(input("Please enter amount to deposit: "))
                # Check if deposit amount is valid
                if deposit_amount <= 0:
                    print("Invalid deposit amount. Please enter a positive number.")
                else:
                    balance += deposit_amount
                    transaction_history.append(f"Deposited: ${deposit_amount:.2f}")
                    print(f"${deposit_amount:.2f} has been credited to your account.")
                    print(f"Your updated balance is ${balance:.2f}")
            except ValueError:
                # Handle case where deposit amount is not a valid number
                print("Invalid amount. Please enter a numeric value.")
        
    
        elif option == 4: # Option 4: View transaction history
            print("Transaction History:")
            if not transaction_history:
                print("No transactions have been made.")
            else:
                # Display each transaction from history
                for transaction in transaction_history:
                    print(transaction)
        
        
        elif option == 5: # Option 5: Change PIN
            try:
                new_pin = int(input("Enter new PIN: "))
                # Check if new PIN is different from the old PIN
                if new_pin == password:
                    print("New PIN cannot be the same as the old PIN.")
                else:
                    password = new_pin
                    print("PIN successfully changed.")
            except ValueError:
                # Handle case where new PIN is not a valid number
                print("Invalid PIN format. Please enter a numeric PIN.")
        
        
        elif option == 6: # Option 6: Exit the program
            print("Thank you for using our ATM. Have a great day!")
            break
        
        # Handle invalid menu options
        else:
            print("Invalid option. Please select a valid choice from the menu.")

# Call the ATM machine function to start the program
atm_machine()
