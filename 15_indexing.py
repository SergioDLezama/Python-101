'''
Indexing es la posicion que tiene un caracter dentro 
de un String
Siempre se empieza a contar en cero
'''

text = 'Hola Mundo'
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])
print(text[6])
print(text[7])
print(text[8])
print(text[9])
print('-' * 25)
text = 'Ella sabe Python'

# Como acceder al ultimo caracter de texto

# Metodo 1
size = len(text)
print(text[size - 1])

#Metodo 2
print(text[-1])

# Slicing
# Cuando no hay nada Python asume que hay un cero
print(text[0:5])  # Ella
print(text[:5])  # Ella
print(text[5:10])  # sabe
print(text[10:16])  # Python
print(text[10:])  # Python
print(text[:])  # Ella sabe Python

# Numero de saltos
print(text[10:16])
print(text[10:16:2])

text_jumps = 'Hiokluai nmjuinydio'
print(text_jumps[::2]) # Hola mundo
