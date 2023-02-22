numbers = [1, 2, 3, 4]
print(numbers)  # [1, 2, 3, 4]
# Igual que los strings puedo acceder a los elementos de las listas
print(numbers[0])  # 1
print(numbers[1])  # 2
print(numbers[2])  # 3
print(numbers[3])  # 4

tasks = ['make dishes', 'study platzi']
print(tasks)  # ['make dishes', 'study platzi']
print(tasks[0])  # 'make dishes'

types = [1, True, 'Hola']  # Las listas puedenen tener varios tipos de datos
print(types)
print(types[1])  # True

# Podemos modificar o mutar las listas
text = 'Hola'
tasks[0] = 'play outside'
print(tasks) # ['play outside', 'study platzi']

tasks[0] = 'do the dishes'
print(tasks) # ['do the dishes', 'study platzi']

# Tambien podemos hacer slicing igual que en los strings
print(numbers[:3]) # [1, 2, 3]
print(True in types) # True
print('Hola' in types) # True