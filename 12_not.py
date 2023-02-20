print(not True) #False
print(not False) #True
print('*' *20)

print('not and')
print('not True or True => ', not (True or True)) #False
print('not True or False => ', not (True or False)) #False
print('not False or True => ', not (False or True)) #False
print('not False or False => ',  not (False or False)) #True
print('*' *20)

stock = int(input('Ingrese el numero de stock: '))
print(not(stock >= 100 and stock <= 1000))
print('*' *20)