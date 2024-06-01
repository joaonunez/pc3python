import acciones
while True:
    try:
        acciones.generar_numbers
        opcion=int(input("Digite 1 para elegir 20 numeros aleatorios:\n"))
        if (opcion == 1):
            acciones.selec_random
            opcion=int(input("Digite 2 para ordenar la lista:\n"))
            if (opcion == 2):
                acciones.ordenar
        break

               
    except:
        print("Error comando desconocido\nREINICIANDO PROGRAMA.........")