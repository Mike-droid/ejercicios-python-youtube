def factorial(numero):
  base = 1
  for i in range(numero): #*desde 0 hasta el número
    base *= i+1
    print(f"Valor de i: {i+1}")
    print(f"Valor de base: {base}")
  print(f"{numero}! = {base}")

factorial(6)

#! Recursividad