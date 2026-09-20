

balance = 0
def myBalance():
    global balance
    return balance

print(myBalance())

def deposit():
    global balance
    amount = input('enter amount to depist')
    balance = balance + float(amount)
    print("you have deposit "+ amount + " now balance is  " ,balance )


deposit()

def withdraw():
    global balance 
     
    amount = float(input(' enter amount withdraw '))
    balance = balance - amount 
    print('you have withdraw ', amount , "blance is ", balance)

withdraw()