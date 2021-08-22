divisas = {
  'Euro':'€', #* clave : valor
  'Dollar':'$',
  'Yen':'¥'
}

divisa = input("Escribe una divisa: ")

if divisas.get(divisa): #!true or false
  print(divisas.get(divisa))
else:
  print("La divisa no se encuentra")
