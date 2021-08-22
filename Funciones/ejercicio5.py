import math

def calcula_area_circulo(radio):
  area_circulo = (math.pi * radio**2)
  print(f"El área del círculo con radio {radio}u es de {area_circulo}u^2")


def calcula_volumen_cilindro(radio,altura):
  volumen_cilindro = (math.pi * altura * radio**2)
  print(f"El volumen del cilindro con radio {radio}u y altura {altura}u es de {volumen_cilindro}u^3")

calcula_area_circulo(5)
calcula_volumen_cilindro(10,7)