#Los booleanos solo pueden tener dos valores verdaderos o falsos

is_single = True
print(type(is_single))
is_single = False
print(is_single)

#Una forma de invertir el valor de un booleano es con not
print(not False)
print(not True)

is_single = not is_single
print(is_single)