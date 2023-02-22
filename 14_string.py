text = 'El sabe programar en Python'
'''
print('JavaScript' in text) # False
print('Python' in text) # True

if 'Python' in text:
  print('Elegiste bien!')
else:
  print('Tambien elegiste bien')
'''
size = len('Vida') # len es para ver cuantos caracteres hay
print(size)
print(len(text))

print(text.upper()) # .upper para pasar todo en mayuscula
print(text)
print(text.lower()) # .lower para pasar todo en minusculas
print(text)

print(text.count('a')) # .count() Para contar cuantas veces aparece un caracter

print(text.swapcase()) # Letras mayuc a minus y viceversa

print(text.startswith('El')) # Saber si un texto comienza de x forma
print(text.startswith('el')) # False
print(text.endswith('thon')) # True
print(text.endswith('Python')) #True

print(text.replace('Python', 'Go'))

text_2 = 'este es un titulo'
print(text_2)
print(text_2.capitalize())
print(text_2.title())
print(text_2.isdigit())
print('55'.isdigit())