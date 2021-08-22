kilos = float(input("Ingresa tu peso en kilos, por favor: "))
estatura_metros = float(input("Ingresa tu estatura en metros, por favor: "))
imc = kilos/(estatura_metros**2)
print(f"Tu índice de masa corporal es {round(imc,2)}")