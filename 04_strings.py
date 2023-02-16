name = 'Sergio'
last_name = 'Lezama Arroyave'
print(name)
print(last_name)

#concatenacion de strings
full_name = name + ' ' + last_name
print(full_name)

quote = "I'm Sergio"
print(quote)

quote_2 = 'She said "Hello"'
print(quote_2)

#Format
age = '20'
template = "Hola mi nombre es: " + name + " y mi apellido es " + last_name + " y mi edad es " + age
print(template)

template = "Hola, mi nombre es {} y mi apelllido es {} y mi edad es {}".format(
  name, last_name, age)
print('v2 ' + template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name} y mi edad es {age}"
print('v3 ' + template)
