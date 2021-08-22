coste_barra_pan = 3.49
descuento = 0.6
barras_vendidas = int(input("¿Cuántas barras de pan vendiste: ?"))
descuento_pan = barras_vendidas * coste_barra_pan * (1-descuento)
print(f"El precio con descuento por las barras de pan es de {descuento_pan}")