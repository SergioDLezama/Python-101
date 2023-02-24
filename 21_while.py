'''
Ciclos while

ctrl + c para cortar un ciclo

while condicion:
  codigo
'''

counter = 0

while counter < 10:
  counter += 1
  print(counter)
print('-' * 25)

counter = 0

# Puedo interrumpir un ciclo con break
while counter < 20:
  counter += 1
  if counter == 15:
    break
  print(counter)
print('-' * 25)

counter = 0

# Puedo continuar una operacion con continue
while counter < 20:
  counter += 1
  if counter < 15:
    continue
  print(counter) # 15 16 17 18 19 20
