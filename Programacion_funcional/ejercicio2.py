import math

def run():
  def calcular(funcion, valor):
    total = []
    for i in range(valor+1):
      total.append(funcion(i))
    return total


  menu = """
  ¿Qué función deseas aplicar?
  1. Seno
  2. Coseno
  3. Tangente
  4. Exponencial
  5. Logaritmo neperiano/natural
  """
  print(menu)
  funcion_trigonometrica = int(input('Opción: '))
  valor = int(input('Desde 0 hasta qué valor deseas calcular?: '))

  if funcion_trigonometrica == 1:
    print(calcular(math.sin, valor))
  elif funcion_trigonometrica == 2:
    print(calcular(math.cos, valor))
  elif funcion_trigonometrica == 3:
    print(calcular(math.tan, valor))
  elif funcion_trigonometrica == 4:
    print(calcular(math.exp, valor))
  elif funcion_trigonometrica == 5:
    print(calcular(math.log, valor))
  else:
    print('Opción incorrecta')


if __name__ == '__main__':
  run()