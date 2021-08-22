def run():
  def funcion_booleana(numero):
    return numero % 2 == 0 # True

  lista = [1,2,3,4,5,6,7,8,9,10]
  resultado = list(filter(funcion_booleana, lista))
  print(resultado)

if __name__ == '__main__':
  run()