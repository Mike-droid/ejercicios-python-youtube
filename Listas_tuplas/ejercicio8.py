palabra = list(input("Escribe una palabra: "))

if palabra[::] == palabra[::-1]:
  print(f"es palíndroma")
else:
  print(f"NO es palíndroma")