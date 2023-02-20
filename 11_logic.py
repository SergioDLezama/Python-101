#and
print('and')
print('True and True => ', True and True) #True
print('True and False => ', True and False) #False
print('False and True => ', False and True) #False
print('False and False => ', False and False) # False
print('*' *20)

print(10 > 5 and 5 < 10) #True
print(10 > 5 and 5 > 10) #False
print('*' *20)

'''
Caso hipotetico de que tnemos una tienda donde para vender
un producto nuestro stock debe cumplir con unos requisitos
de minimo y maximo de stock
'''
stock = int(input('Ingrese el numero de stock: '))
print(stock >= 100 and stock <= 1000)
print('*' *20)

# or
print('or')
print('True or True => ', True or True) #True
print('True or False => ', True or False) #True
print('False or True => ', False or True) #True
print('False or False => ', False or False) #False
print('*' *20)

role = input('Digita el rol: ')
print(role == 'admin' or role == 'seller')

