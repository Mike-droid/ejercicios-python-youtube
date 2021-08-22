peso_de_payaso = 112
peso_de_muneca = 75
payasos_vendidos = int(input("¿Cuántos payasos fueron vendidos?: "))
munecas_vendidas = int(input("¿Cuántas muñecas fueron vendidas: ?"))
peso_total = (peso_de_payaso * payasos_vendidos) + (peso_de_muneca * munecas_vendidas)
print(f"El peso total de los muñecos y muñecas es de {peso_total / 1000}kg")