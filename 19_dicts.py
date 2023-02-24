'''
Los diccionarios contienen una llave que es el index
y un valor o definicion

example = {Key: Value, Key2: Value2}
'''

my_dict = {}
print(type(my_dict))

my_dict = {
  'name': 'Sergio',
  'last_name': 'Lezama',
  'age': '20'
}

print(my_dict) # {'name': 'Sergio', 'last_name': 'Lezama', 'age': '20'}
print(len(my_dict)) # 4

print(my_dict['age']) # '20'
print(my_dict['name']) # 'Sergio'

# Diferencia del get es que si el valor no existe dara None
print(my_dict.get('age')) # '20'

print('name' in my_dict) # True
print('hola' in my_dict) # False

