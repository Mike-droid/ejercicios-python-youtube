numero = int(input("Escribe un número para saber si es primo o no: "))
i = 2
while numero % i != 0:
    i += 1
    #i = i + 1
if i == numero:
    print(f"El numero {numero} es primo")
else:
    print(f"El numero {numero} NO es primo")