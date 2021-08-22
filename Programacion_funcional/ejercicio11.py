import statistics

def run():
  def valores_atipicos(muestra):
    media = statistics.mean(muestra)
    desviacion_estandar = statistics.stdev(muestra)
    valores = []
    for numero in muestra:
      valor_atipico = (numero - media) / desviacion_estandar
      if valor_atipico < -3 or valor_atipico > 3:
        valores.append(numero)
    return valores

  print(valores_atipicos([1,2,3,4,5,6,7,8,9,10,1000]))


if __name__ == '__main__':
  run()