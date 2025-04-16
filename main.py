
### build the rest of it tomorrow. 
#good job 

balance_amount = 0

def deposit():
    while True:
        amount  = input('What would you like to deposit? --- $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0')
        else:
            print('Please enter a number.')
    return amount
    
def acknowledge_deposit(amount):
    print(f'${amount} has been successfully deposited')


def show_balance(amount):
    global balance_amount
    balance_amount += amount
    print(f'Your new balance is ${balance_amount}')

# ** Withdraw option***

def withdraw():
    global balance_amount

    while True:
        withdraw_inquiry = input('Would you like to withdraw money? y/n ').lower()
        if withdraw_inquiry == 'y':
            amount = input('How much would like to withdraw? $ ')
            if amount.isdigit():
                amount = int(amount)
                if amount <= balance_amount:
                    balance_amount -= amount
                    print(f'${amount} has been withdrawn. New balance is ${balance_amount}')
                    break
                else:
                    print(f'Insufficient balance. Your balance is ${balance_amount}')
        elif withdraw_inquiry == 'n':
                print('Thank you for banking with us today!')
                break
        else: 
            print("Please respond with 'y' or 'n'.")

# def withdraw():
#     global balance_amount

#     while True:
#         withdraw_inquiry = input('Would you like to withdraw money? y/n ').lower()
#         if withdraw_inquiry == 'y':
#             amount = input('How much would you like to withdraw? $ ')
#             if amount.isdigit():
#                 amount = int(amount)
#                 if amount <= balance_amount:
#                     balance_amount -= amount
#                     print(f'${amount} has been withdrawn. New balance is ${balance_amount}')
#                     break
#                 else:
#                     print(f'Insufficient funds. Your balance is ${balance_amount}.')
#                     # Loop back to ask if they still want to withdraw
        
#             else:
#                 print('Please enter a valid number!')
        
#         elif withdraw_inquiry == 'n':
#             print('Thank you for banking with us today!')
#             break

#         else:
#             print("Please respond with 'y' or 'n'.")



# ****Running the program***
amount = deposit()
acknowledge_deposit(amount)
show_balance(amount)
withdraw()

    

