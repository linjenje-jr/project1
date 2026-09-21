balance = 80

name = input('enter ur name ')
password = input('enter pass')

def verify_pass():
    if password == '1234':
        print('password verfyed')
    elif password != '1234' :
        print('Access Denide')
        exit()

def check_balance():
    return print(f"hello! {name} your balance is {balance} ")

def deposit():
    global balance
    amount = float(input("enter deposit amount "))
    balance = balance + amount

    print(f"congarts {name} your deposit {amount} tzs. new balance is {balance}" )

def withdraw():
    global balance
    amount_with = float(input('enter withdraw amaunt '))
    balance = balance - amount_with
    print(f'congrats {name}, you have withdraw {amount_with} tzs. your new balance is {balance} tzs ')
def log_in():
    verify_pass()
    services=['1.Balance','3.Withdraw','2.Deposit','4.to stop']
    while True:
        services.sort()
        print('select the service number below')
        for Service in services:
            print(f'\n{Service}')
        service = int(input())
        match service:
            case 1:
                check_balance()
                break
            case 2:
                deposit()
                break
            case 3 :
                withdraw()
                break
            case 4 :
                exit()
            case _ :
                print('unrecorgnized service')
        
        
while True:
    log_in()
    while True:
        again = input('to continue with other services press 1. to stop press 2\n')
        if again == '2':
            exit()
        elif again == '1':
            log_in()
        else:
            print('error')