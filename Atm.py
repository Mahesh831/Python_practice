'''cash = int(input('Enter your cash here'))
Amount = 50000
totalBalance = Amount - cash
print('your bank balance',totalBalance,sep='->')
print('Thank You for using ATM')'''
pin,cash = input('enter ur pin and cash').split(",")
#print('urs pin nd cash r :',pin,cash)
#print('cash is {},pin is {}'.format(cash,pin))
print('cash is {1},pin is {0}'.format(cash,pin))

