print('hello, welcome to payphone service')
print('price:200 shillings per minutes')
time=int(input('how many minutes?\n'))
total_price=time*200
print('\nso it is '+str(total_price)+' shillings for '+str(time)+' minutes')
payment=input('cash or credit\n')
if payment=='cash':
    print('place it here')
elif payment=='credit':
    print('code:20675')
else:
    print('we do not have thjat service')
print('thank you and welcome again')
print('by zilch')