def binario_a_decimal(numero):
  numero = list(numero) #* 1,1,0
  numero.reverse() #* 0,1,1
  decimal = 0
  for i in range(len(numero)):
    decimal += int(numero[i]) * 2 ** i
  print(decimal)

binario_a_decimal('110')

def decimal_a_binario(numero):
  binario = []
  while numero >= 1:
    if numero % 2 == 0:
      binario.append(0)
    elif numero % 2 != 0:
      binario.append(1)
    numero //=2 #! solo número entero
  print(binario[::-1])

decimal_a_binario(5)