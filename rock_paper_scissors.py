import random
import os
'''
El proyecto es hacer un juego de consola de 
Piedra, Papel o Tijera

Cap 28 anadi tuplas al proyecto y random
Cap 37 anadiendo ciclos
       anadiendo mas rondas
       
'''

draws = [
  "\n   _       ,/'\n  (_).  ,/'\n   _  ::\n  (_)'  `\.\n           `\.",
  
]

jumpline = '\n'
options = ('piedra', 'papel', 'tijera')
counter = 1
computer_wins = 0
user_wins = 0
line = '=' * 25

os.system('clear')
print(input(line + '\nBIENVENIDO A PIEDRA PAPEL O TIJERA!!!\nQUE GANE EL MEJOR DE 3!!\nPRESIONA [ENTER] PARA EMPEZAR\n' + line + jumpline))
while counter < 6:

  os.system('clear')
  print('='*25)
  print(f'ROUND {counter}')
  print('='*25)
  print(f'PUNTOS\nUSUARIO {user_wins}\nCOMPUTER {computer_wins}')
  print('='*25)
  
  
  user_option = input('\nPiedra, papel o tijera?: ').lower()
  computer_option = random.choice(options)
  
  if user_option == 'exit':
    break
  
  # Esta linea confirma que el user de una de las opciones posibles
  if not user_option in options:
    print(input('\nEsa opcion no es valida\nPRESIONA [ENTER] PARA REINTENTAR'))
    continue
  
  #print(jumpline ,'User options: ', user_option.title())
  #print('Computer uption: ', computer_option.title(), jumpline)
  
  
  if user_option == computer_option:
    print(f'\n"{user_option.upper()}", Empate!!')
  
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('\n"TIJERA", Ganaste!')
      user_wins += 1
    else:
      print('\n"PAPEL", Perdiste!')
      computer_wins += 1
  
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('\n"PIEDRA", Ganaste!\n')
      user_wins += 1
    else:
      print('\n"TIJERA", Perdiste!\n')
      computer_wins += 1
  
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('\n"PAPEL", Ganaste!\n')
      user_wins += 1
    else:
      print('\n"PIEDRA", Perdiste!\n')
      computer_wins += 1
  print(input('\nSiguiente ronda! Presiona ENTER\n'))

  if counter == 5:
    if user_wins > computer_wins:
      print(input('USUARIO GANA!!!!!\n'))
    elif user_wins == computer_wins:
      print(input('EMPATE!!!!\n'))
    else:
      print(input('COMPUTER GANA!!!!!\n'))
    
  counter += 1 
  
      