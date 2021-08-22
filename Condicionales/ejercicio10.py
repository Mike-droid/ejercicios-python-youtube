pizza = int(input("Escoge un tipo de pizza; 1. Vegetariana 2. No vegetariana  :  "))
ingrediente = ""
opcion_ingrediente = 0

if pizza == 1:
    opcion_ingrediente = int(input(("Escoge un ingrediente; 1.Pimiento  2.Tofu  :  ")))
    if opcion_ingrediente == 1:
        print(f"Tu pizza es vegetariana y tiene mozzarella, tomate y pimiento")
    elif opcion_ingrediente == 2:
        print(f"Tu pizza es vegetariana y tiene mozzarella, tomate y tofu")
    else:
        print("Opción no válida")
elif pizza == 2:
    opcion_ingrediente = int(input(("Escoge un ingrediente; 1.Peperoni  2.Jamón  3.Salmón  :  ")))
    if opcion_ingrediente == 1:
        print(f"Tu pizza es no vegetariana y tiene mozzarella, tomate y peperoni")
    elif opcion_ingrediente == 2:
        print(f"Tu pizza es no vegetariana y tiene mozzarella, tomate y jamón")
    elif opcion_ingrediente == 3:
        print(f"Tu pizza es no vegetariana y tiene mozzarella, tomate y salmón")
    else:
        print("Opción no válida")