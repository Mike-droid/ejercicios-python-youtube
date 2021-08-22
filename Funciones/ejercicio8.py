import statistics

lista = [1,2,3,4,5,6,7,8,9,10]

def crear_diccionario(muestra):
  media = statistics.mean(muestra)

  varianza = statistics.variance(muestra)

  desviacion_estandar = statistics.stdev(muestra)

  diccionario = {
    'Media': media,
    'Varianza': varianza,
    'Desviación estándar': desviacion_estandar
  }

  print(diccionario)

crear_diccionario(lista)