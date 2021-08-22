numero = int(input("Introduce un número: "))

for i in range(1 , numero+1, 2):
    for j in range(i, 0, -2):
        print(j , end=" ")
    print("")

#! i = 1 | j = 1 - 2 = -1 -> no se toma en cuenta
#! i = 3 | j = 3 - 2 = 1
#! i = 5 | j = 5 - 2 = 3
#! i = 7 | j = 7 - 2 = 5
#! i = 9 | j = 9 - 2 = 7
#! i = 11 | j = 11 - 2 = 9