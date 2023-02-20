x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
'''
Vemos que python trabaja con distintas precisiones deimales
con x solo nos da un decimal
con y nos da varios
Al momento de compararlo nos dara un False por la diferencia
de presicion
'''
print(x == y)

# Soluciones
# Solucionando con str
y_str = format(y, '.2g')
print('str => ', y_str)
print(str(x) == y_str)

print('*' * 15)

# Solucion matematicas
print(x, y)
tolerance = 0.00001
print(abs(x - y) < tolerance)

print(x, y)
y = round(2.2 + 1.1, 1)
print(x == y)
