ci = float(input("Ingresa tu capital inicial: "))
i = float(input("¿Cuál es la tasa de interés?: "))
n = float(input("¿Cuántos años vas a invertir el dinero?: "))
cf = ci * (1+i)**n
print(f"Con un capital inicial de ${ci}, una tasa de interés del {i}%, e inviertiendo {n} años, tu capital final es de ${cf}")