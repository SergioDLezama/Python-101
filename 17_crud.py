# CRUD Create, Read, Update & Delete
numbers = [1, 2, 3, 4, 5]

print(numbers[2])  # 3
numbers[-1] = 10
print(numbers)  # [1, 2, 3, 4, 10]

# .append(elemento) para anadir un elemento a la ista
numbers.append(700)
print(numbers)  # [1, 2, 3, 4, 10, 700]

# .insert(posicion,elemento)
numbers.insert(0, 'hola')
print(numbers)  # ['hola', 1, 2, 3, 4, 10, 700]
numbers.insert(3, 'change')
print(numbers)  # ['hola', 1, 2, 'change', 3, 4, 10, 700]

tasks = ['all 1', 'all 2', 'all 3']
new_list = numbers + tasks
print(new_list)
# ['hola', 1, 2, 'change', 3, 4, 10, 700, 'all 1', 'all 2', 'all 3']

# .index() Para saber en que posicion esta cierto elemento de una lista
print(new_list.index('all 2'))  # 9
index = new_list.index('all 2')
new_list[index] = 'new all'
print(new_list)
# ['hola', 1, 2, 'change', 3, 4, 10, 700, 'all 1', 'new all', 'all 3']

#Metodos para remover

new_list.remove('all 1')
print(new_list)
# ['hola', 1, 2, 'change', 3, 4, 10, 700, 'all 1', 'new all', 'all 3']

# .pop elimina el ultimo elemento de esa lista
new_list.pop()
print(new_list)  # ['hola', 1, 2, 'change', 3, 4, 10, 700, 'new all']

new_list.pop(0)
print(new_list)  # [1, 2, 'change', 3, 4, 10, 700, 'new all']

# Revierte la lista lo vuelve alreves
new_list.reverse()
print(new_list) # ['new all', 700, 10, 4, 3, 'change', 2, 1]

# Sort para acomodar en orden numerico o alfabetico
numbers_a = [1, 4, 6, 3]
print(numbers_a) # [1, 4, 6, 3]
numbers_a.sort()
print(numbers_a) # [1, 3, 4, 6]

strings = ['re', 'ab', 'ed']
print(strings) # ['re', 'ab', 'ed']
strings.sort()
print(strings) # ['ab', 'ed', 're']

# El sort no funcionara al tener distintos tipos de datos
