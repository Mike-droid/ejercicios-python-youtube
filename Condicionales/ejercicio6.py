nombre = input("Introduce tu nombre: ")
sexo = input("¿Eres hombre o mujer? (H o M): ")
grupo = ""

if ((nombre.lower() < 'm' and sexo == 'M') or (nombre.lower() > 'n' and sexo == 'H')):
    grupo = "A"
else:
    grupo = "B"


print(f"{nombre} perteneces al grupo {grupo}")