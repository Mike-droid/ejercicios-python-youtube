numeros_ganadores = []
for i in range(6):
  numeros_ganadores.append(int(input('Escribe un número ganador: ')))
  numeros_ganadores.sort() #*Ordena los números de menor a mayor
print(f'Los números ganadores son: {numeros_ganadores}')