#from bank2 import account_
accounts={}
blocked_accounts={}
balance = {}

def check_balance():
    return print(f"hello! {name} your balance is {balance[name]} ")

def deposit():
    global balance
    global name
    amount = float(input("enter deposit amount "))
    balance[name] = balance[name] + amount

    print(f"congarts {name} your deposit {amount} tzs. new balance is {balance[name]}" )

def withdraw():
    global balance
    global name
    amount_with = float(input('enter withdraw amaunt '))
    balance[name] = balance[name] - amount_with

    print(f'congrats {name}, you have withdraw {amount_with} tzs. your new balance is {balance[name]} tzs ')

def register():
    global accounts
    global balance

    account_name = input('enter your name ')
    account_password = input('enter your password ')
    print(f'account created for {account_name}')
    accounts[account_name] = account_password
    balance[account_name] = 0

    while True:
        again = input('to continue with other services press 1. to stop press 2\n')
        if again == '2':
            break
        elif again == '1':
            log_in()
        else:
            print('error')


def open_account():
    account = input('press1 to create  account or press 2 to log in\n')
    match account:
        case '1':
            register()
            open_account()

        case'2':
            global name
            name = input('enter your account name')
                
        case _:
            print('unrecorgnized service')
            open_account()

        
    if name in accounts:
        print(f'account found for {name}')
    elif name in blocked_accounts:
        print('your account is blocked, please contact the bank costumer care for more details')
        open_account()
    else:
        print('account not found, please create an account')
        open_account()

    password = input('enter password')
    if password == accounts[name]:
        print(f'wellcome {name}, you have login your account')
    else:
        for times in range(3):
            print('inviald password')
            password = input('enter password')
            if password == accounts[name]:
                print(f'wellcome {name}, you have login your account')
                break
            
            print('access denide, youe account is blocked, please contact the bank costumer care for more details')
            blocked_accounts[name] = accounts.pop(name)
            open_account()
                
def log_in():
    services=['1.Balance','3.Withdraw','2.Deposit','4.to stop']
    while True:
        services.sort()
        print('select the service number below')
        for Service in services:
            print(f'\n{Service}')
        service = input()
        match service:
            case '1':
                check_balance()
                break
            case '2':
                deposit()
                break
            case '3':
                withdraw()
                break
            case '4':
                print('thank you for using our services')
                open_account()
            case _ :
                print('unrecorgnized service')
    print('welcome again to our bank') 

while True:
    open_account()
    log_in()


