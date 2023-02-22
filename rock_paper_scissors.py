'''
El proyecto es hacer un juego de consola de 
Piedra, Papel o Tijera
'''

user_option = input('Piedra, papel o tijera?: ').lower()
# Por ahora la computadora tendra una opcion fija
computer_option = 'papel'

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

      