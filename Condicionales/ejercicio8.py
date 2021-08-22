puntuacion = float(input("Escribe tu puntación: "))
sueldo_base = 2400
beneficio = (puntuacion * sueldo_base) + sueldo_base
nivel = ""

if puntuacion == 0 or puntuacion == 0.0:
    nivel = "inaceptable"
    print(f"Tu beneficio es de ${beneficio} y tienes un nivel de {nivel}")
elif puntuacion == 0.4:
    nivel = "aceptable"
    print(f"Tu beneficio es de ${beneficio} y tienes un nivel de {nivel}")
elif puntuacion >= 0.6:
    nivel = "meteorito"
    print(f"Tu beneficio es de ${beneficio} y tienes un nivel de {nivel}")