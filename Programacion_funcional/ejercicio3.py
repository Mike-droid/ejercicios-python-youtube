from functools import reduce

def run():
  #map -> map(funcion, objeto_iterable)
  """ def elevar_al_cuadrado(numero):
    return numero * numero

  lista = [1,2,3,4,5]
  resultado = list(map(elevar_al_cuadrado, lista))
  print(resultado) """

  #filter -> filter(funcion, objeto_iterable)
  """ def mayor_a_cinco(numero):
    return numero > 5

  lista = [46,1,2,3,7,8]
  resultado = list(filter(mayor_a_cinco, lista))
  print(resultado)

  def circulo(palabra):
    return palabra == 'circulo'

  tupla = ('hola','soy','un','circulo','circulo','circulo')
  resultado2 = tuple(filter(circulo, tupla))
  print(resultado2) """

  #reduce -> reduce(funcion, objeto_iterable)
  """ lista = [1,2,3,4]

  def funcion_acumulador(acumulador, elemento):
    return acumulador + elemento

  resultado = reduce(funcion_acumulador, lista)
  print(resultado) """

  lista = ['Python', 'JavaScript', 'C#','C++','Go','Swift','Kotlin']
  def funcion_acumulador(acumulador, elemento):
    return acumulador + " - " + elemento

  resultado = reduce(funcion_acumulador, lista)
  print(resultado)

if __name__ == '__main__':
  run()