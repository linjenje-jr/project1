#from bank2 import account_
accounts=[]
def register():
    while True:
        global accounts
        account_name = input('enter your name ')
        account_password = input('enter your password ')
        print(f'account created for {account_name}')
        accounts.append({account_name:account_password})
        another_account = input('press1 to create another account or press 2 to log in\n')
        if another_account == '2':
            break

def account():
    balance = 0
    name = input('enter your account name')
def password_verfication():
    global name
    global accounts
    password = input('enter password')
    if password == accounts[name]:
        print(f'wellcome {name}, you have login your account')
    else:
        for times in range(2):
            print('inviald password')
            password = input('enter password')
            if password == accounts[name]:
                print(f'wellcome {name}, you have login your account')
                break
        print('access denide')
        exit()
    

register()
account()
password_verfication()



