palabra = input("Escribe una palabra: ")

contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

for letra in palabra:
  if letra == 'a' or letra == 'A':
    contador_a += 1
  elif letra == 'e' or letra == 'E':
    contador_e += 1
  elif letra == 'i' or letra == 'I':
    contador_i += 1
  elif letra == 'o' or letra == 'O':
    contador_o += 1
  elif letra == 'u' or letra == 'U':
    contador_u += 1

print(f'Le letra a aparece {contador_a} veces')
print(f'Le letra e aparece {contador_e} veces')
print(f'Le letra i aparece {contador_i} veces')
print(f'Le letra o aparece {contador_o} veces')
print(f'Le letra u aparece {contador_u} veces')