
#* Lista: Colección de elementos que podemos modificar (mutable)
#* Tupla: Colección  de elementos que NO podemos modificar (inmutable)

asignaturas_lista = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua'] #! Lista
asignaturas_tupla = ('Matemáticas', 'Física', 'Química', 'Historia', 'Lengua') #! Tupla

asignaturas_lista.append('Programación')
asignaturas_tupla.append('Programación')

print(f"La lista de las asignias es  {asignaturas_lista}")
print(f"La tupla de las asignaturas es {asignaturas_tupla}")