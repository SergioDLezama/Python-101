name = 'Sergio'
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

print('Sergio' + ' Lezama')
print(10+20)
#error print('Sergio' + 10)
print('Sergio' + '10')

age = 20
#error print('Mi edad es' + age)
print('Mi edad es ' + str(age))
print(f'Mi edad es {age}')

age = input('Escribe tu edad: ')
print(type(age))
print(f'Tu edad en 10 anos sera {int(age) + 10}')
#or
age = int(age)
age += 10
print(f'Tu edad en 10 anos sera {age}')
