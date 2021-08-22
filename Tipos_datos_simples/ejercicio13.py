interes = 0.04
inversion = float(input("Escribe tu inversión inicial: "))
balance1 = inversion * (1+interes)
print(f"Después de 1 año, tienes ${round(balance1,2)}")
balance2 = balance1 * (1+interes)
print(f"Después de 2 años, tienes ${round(balance2,2)}")
balance3 = balance2 * (1+interes)
print(f"Después de 3 años, tienes ${round(balance3,2)}")