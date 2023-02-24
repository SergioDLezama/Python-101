'''
Los ciclos anidados son ciclos dentro de los ciclos
por ejemplo un if dentro de otro if

if condition_1:
  if condition_2:
    code
'''
jumpline = '-' * 25

# Una lista de listas
matriz = [
    [1,2,3], 
    [4,5,6],
    [7,8,9]
]

print(matriz[0]) # [1,2,3]
print(matriz[0][2]) # 3
print(jumpline)

for i in matriz:
  print(i)
  '''
  [1, 2, 3]
  [4, 5, 6]
  [7, 8, 9]
  '''
print(jumpline)

#Al hacer un ciclo anidado hay que usar diferentes variables
for row in matriz:
  print(row)
  for colum in row:
    print(colum)
  '''
  [1, 2, 3]
  1
  2
  3
  [4, 5, 6]
  4
  5
  6
  [7, 8, 9]
  7
  8
  9
  '''
  