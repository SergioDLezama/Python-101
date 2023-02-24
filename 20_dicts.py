person = {
  'name' : 'sergio',
  'last_name' : 'lezama',
  'langs' : ['python' , 'javascript'],
  'age' : 20
  
}

print(person) # {'name': 'sergio', 'last_name': 'lezama', 'langs': ['python', 'javascript'], 'age': 20}

# Para actualizar una llave
person['name'] = 'sebas'
print(person)  # {'name': 'sebas', 'last_name': 'lezama', 'langs': ['python', 'javascript'], 'age': 20}
person['age'] += 15
print(person) # {'name': 'sebas', 'last_name': 'lezama', 'langs': ['python', 'javascript'], 'age': 35}
person['langs'].append('rust')
print(person) # {'name': 'sebas', 'last_name': 'lezama', 'langs': ['python', 'javascript', 'rust'], 'age': 35}

# Eliminar un elemento con del
del person['last_name']
print(person) # {'name': 'sebas', 'langs': ['python', 'javascript', 'rust'], 'age': 35}

# Eliminar con el metodo pop
person.pop('age')
print(person) # {'name': 'sebas', 'langs': ['python', 'javascript', 'rust']}

# .items, me devuelve los key: values en pares en forma de tuplas
print('\nItems\n', person.items())

# .keys =, me devuelve las llaves
print('\nKeys\n', person.keys())

# .values me devuelve los valores
print('\nValue\n', person.values())