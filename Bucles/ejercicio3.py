numero = int(input("Escribe un número: ")) #!10
#!0,1,2,3,4,5,6,7,8,9
for i in range(numero+1): #!10
    if i % 2 != 0: #?      != diferente              == comparar
        print(i , end=" , ")