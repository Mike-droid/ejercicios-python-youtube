edad = int(input("¿Cuántos años tienes?: "))
ingresos_mensuales = float(input("¿Cuánto es de tus ingresos mensuales?: "))

if edad > 15 and ingresos_mensuales >= 1000: #compuerta lógica
    print("Tienes que tributar")
else:
    print("No tienes que tributar")