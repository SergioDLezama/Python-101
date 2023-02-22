if True:
  print('Deberia ejecutarse')

if False:
  print('No deberia ejecutarse')


pet = input('Cual es tu mascota favorita?: ').lower()

if pet == 'perro':
  print('Genial! tienes buen gusto')
elif pet == 'gato':
  print('Tambien me gustan los gatos')
elif pet == 'pez':
  print('Eres lo maximo')
else:
  print('No tienes ningina mascota de las que tengo en base da datos')


'''
stock = int(input('Digita el stock: '))

if stock >= 100 and stock <= 1000:
  print('El stock es el correcto, es mayor de 100 y menor de 1000')
else:
  print('El stock es incorrecto')

'''

'''
RETO UN SCRIPT QUE ME DIGA SI UN NUMERO ES PAR O IMPAR
'''

digit = int(input('Dime un numero y te dire si es par o impar: '))

if digit % 2 == 0:
  print(f'El numero {digit} es par.')
else:
  print(f'El numero {digit} es impar')