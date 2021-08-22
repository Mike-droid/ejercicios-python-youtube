def contar_palabras(cadena):
  cadena = cadena.split()
  palabras = {}
  for palabra in cadena:
    if palabra in palabras:
      palabras[palabra] += 1
    else:
      palabras[palabra] = 1
  return palabras
  #print(palabras)


def mas_repetida(cadena):
  palabra_mas_repetida = ''
  maxima_frecuencia = 0
  for palabra,frecuencia in cadena.items():
    if frecuencia > maxima_frecuencia:
      palabra_mas_repetida = palabra
      maxima_frecuencia = frecuencia
  return palabra_mas_repetida , maxima_frecuencia


print(contar_palabras("hola hola hola mundo desde python"))
print(mas_repetida(contar_palabras("hola hola hola mundo desde python")))
