renta_anual = float(input("¿Cuánto tienes de renta anual?: "))
tipo_impositivo = ""

if renta_anual < 10000:
    tipo_impositivo = "5%"
elif renta_anual > 10000 and renta_anual < 20000:
    tipo_impositivo = "15%"
elif renta_anual > 20000 and renta_anual < 35000:
    tipo_impositivo = "20%"
elif renta_anual > 35000 and renta_anual < 60000:
    tipo_impositivo = "30%"
else:
    tipo_impositivo = "45%"


print(f"Para la renta anual de {renta_anual} el tipo impositivo es de {tipo_impositivo}")