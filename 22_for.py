'''
Estructra de un ciclo for

for element in range:
  code

for element in range(20):
  print(element) # print numeros del 0 al 19

or element in range(1, 21):
  print(element) # print numeros del 1 al 20

'''
jumpline = '-' * 25

# Puedo recorrer una lista con for

my_list = [23, 45, 57, 89, 43]

for element in my_list:
  print(element) 
  '''
  23
  45
  57
  89
  43
  '''
print(jumpline)

# Puedo recorrer una tupla con for
my_tuple = ('sergio', 'sebas', 'moi')
for element in my_tuple:
  print(element)
  '''
  sergio
  sebas
  moi
  '''
print(jumpline)

# Puedo recorrer un diccionario

product = {
  'name': 'Camisa',
  'price': 100,
  'stock': 89
}

# De esta forma solo me dara las llaves mas no los valores
for element in product:
  print(element)
  '''
  name
  price
  stock
  '''
print(jumpline)
  
# Asi puedo recibir las llaves y el valor
for element in product:
  print(product[element])
  '''
  Camisa
  100
  89
  '''
print(jumpline)
  
# Asi puedo recibir tanto la llave como el valor
for element in product:
  print(element, ' -> ', product[element])
  '''
  name  ->  Camisa
  price  ->  100
  stock  ->  89
  '''
print(jumpline)
  
# Tambien puedo asignar dos elementos para tener llave y valor
# Uso el .items() Para volver el dict en una tupla y pueda ser recorrido
for key, value in product.items():
  print(key, ' -> ', value)
print(jumpline)

# Es muy normal en el mundo del desarrollo una lista de dict
people = [
  {
    'name': 'sergio',
    'age': 20
  },
  {
    'name': 'sebas',
    'age': 15
  },
  {
    'name': 'mathias',
    'age': 12
  },
  {
    'name': 'moi',
    'age': 10
  },
  {
    'name': 'maxi',
    'age': 9
  }
]

for person in people:
  print(person)
  '''
  {'name': 'sergio', 'age': 20}
  {'name': 'sebas', 'age': 15}
  {'name': 'mathias', 'age': 12}
  {'name': 'moi', 'age': 10}
  {'name': 'maxi', 'age': 9}
  '''

for person in people:
  print('name ->' ,person['name'])
  '''
  name -> sergio
  name -> sebas
  name -> mathias
  name -> moi
  name -> maxi
  '''

for person in people:
  print('name ->' ,person['name'])