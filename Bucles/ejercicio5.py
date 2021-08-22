monto = float(input("Monto: "))
interes = float(input("Interés: "))
anios = int(input("Años: "))

for i in range(anios):
    monto = monto * (1+interes)**anios
    print(f"Cantidad de dinero después de {i+1} años $ {monto}")