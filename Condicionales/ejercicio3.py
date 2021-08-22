numerador = int(input("Escribe un numerador: "))
denominador = int(input("Escribe un denominador: "))

if denominador == 0: #indentanción
    print("¡Error! No puedes dividir entre 0")
else:
    print(f"La división de {numerador} entre {denominador} es {numerador/denominador}")