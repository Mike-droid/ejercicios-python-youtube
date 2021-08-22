lista = [1,2,3,4,5,6,7,8,9,10]

def eleva_al_cuadrado(lista):
  cuadrados = []
  for i in lista:
    i = i**2
    cuadrados.append(i)
  print(cuadrados)

eleva_al_cuadrado(lista)