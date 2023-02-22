# Las tuplas pueden almacenar varios elementos, es inmutable
# Las tuplas son inmutables
# Es una estructura de datos solo de lectura

numbers = (1, 2, 3, 5)
strings = ('nico', 'zule', 'santi', 'nico')

print(numbers)
print('Index 0 = ', numbers[0])
print('Index -1 = ', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

# Buscar elemento en la tupla
print(strings.index('zule'))

# Buscar cuantas veces esta un elemento repetido
print(strings.count('nico'))

# Transformar tupla en lista
my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[1] = 'juli' 
print(my_list)

# Transformar una lista en tupla
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my))
