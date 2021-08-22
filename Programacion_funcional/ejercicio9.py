import math

def run():
  v1 = [1,2,3] # -> [1,4,9] -> 14
  v2 = [4,5,6] # -> [16,25,36] -> 77
  v3 = [7,8,9] # -> [49,64,81] -> 194

  def eleva_al_cuadrado(vector):
    vector = [v**2 for v in vector] #list comprehension
    sumatoria = sum(vector)
    return sumatoria

  def calcula_modulo():
    newV1 = eleva_al_cuadrado(v1)
    newV2 = eleva_al_cuadrado(v2)
    newV3 = eleva_al_cuadrado(v3)
    modulo = math.sqrt(newV1+newV2+newV3)
    return modulo

  print(f'El módulo es: {calcula_modulo()}')

if __name__ == "__main__":
  run()
