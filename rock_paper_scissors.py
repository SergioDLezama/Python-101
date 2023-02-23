import random
'''
El proyecto es hacer un juego de consola de 
Piedra, Papel o Tijera

Cap 28 anadi tuplas al proyecto y random
'''

jumpline = '\n'
options = ('piedra', 'papel', 'tijera')
user_option = input('\nPiedra, papel o tijera?: ').lower()
computer_option = random.choice(options)

# Esta linea confirma que el user de una de las opciones posibles
if not user_option in options:
  print('\nEsa opcion no es valida')

print(jumpline ,'User options: ', user_option.title())
print('Computer uption: ', computer_option.title(), jumpline)


if user_option == computer_option:
  print(f'"{user_option.upper()}", Empate!!')

elif user_option == 'piedra':
  if computer_option == 'tijera':
    print('"TIJERA", Ganaste!')
  else:
    print('"PAPEL, Perdiste!"')

elif user_option == 'papel':
  if computer_option == 'piedra':
    print('"PIEDRA", Ganaste!')
  else:
    print('"TIJERA", Perdiste!')

elif user_option == 'tijera':
  if computer_option == 'papel':
    print('"PAPEL", Ganaste!')
  else:
    print('"PIEDRA", Perdiste!')

      