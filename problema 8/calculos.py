import funciones
while True:
    opciones="1.SUMAR 2 NUMEROS\n 2.RESTAR 2 NUMEROS\n 3.MULTIPLICAR 2 NUMEROS\n 4.DIVIDIR 2 NUMEROS\n5.SALIR\n"
    x=input(f"ingrese una opcion:\n{opciones} ")
    if x=="1":
        funciones.sumar
    elif x=="2":
        funciones.resta
    elif x=="3":
        funciones.multi
    elif x=="4":
        funciones.divi
    elif x=="5":
        print("chao profe uwu")
    else:
        print("ERROR, comando desconocido")
