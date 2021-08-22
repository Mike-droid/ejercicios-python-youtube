diccionario = {}

palabras = input("Escribe palabras en español:ingles separadas por ':' y cada par por coma: ")

#! hola:hello,adios:bye

for i in palabras.split(','):
  #!['hola:hello','adios:bye']
  clave,valor = i.split(":")
  diccionario[clave] = valor

frase_espanol = input("Escribe una frase en español: ")
#!hola mundo -> 'hola','mundo'
for palabra in frase_espanol.split():
  if palabra in diccionario:
    print(diccionario[palabra] , end = " ")
  else:
    print(palabra , end = " ")