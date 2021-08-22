numero = int(input("Escribe un número: "))

for i in range(numero+1): #!0 1 2 3 4 5
    print("*" * i)
    for j in range(numero+1):
        print(end="")