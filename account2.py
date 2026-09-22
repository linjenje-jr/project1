def account2():
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
    password_verfication()



