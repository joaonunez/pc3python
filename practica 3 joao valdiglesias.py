print("___________________________________________________________EJERCICIO 1:\n")
def contabilizador_combustible():
    import re
    while True:
            try:
                fraccion=input("Hola,Ingrese la fraccion actual del combustible indicado en el marcador")
                fraccion.strip()
                fraccionuwu=re.split(f'[/]',fraccion)
                numerador,denominador=[int(a) for a in fraccionuwu]
                try:
                    if denominador>=numerador:
                        porcentaje=numerador*100 / denominador
                        if porcentaje<1:
                            print("F")
                        elif porcentaje>99:
                            print("E")
                        print(f"el porcentaje de combustible es:\n{porcentaje}%")
                        break
                    elif denominador<numerador:
                        print("ERROR el combustible actual no puede ser mayor a su capacidad del tanque")

                except:
                    if  denominador+numerador==0:
                        print("ERROR, ZeroDivisionError\n AMBOS NUMEROS  NO PUEDEN SER 0")
                    elif porcentaje<0:
                        print("error el porcentaje no puede ser negativo\n")



            except:
                print("ERROR no se pudo calcular el porcentaje de combustible, ingrese correctamente la fraccion con numeros ENTEROS\nREINICIANDO PROGRAMA......\n")
contabilizador_combustible()
print("_____________EJERCICIO 2:\n")
def calificaciones():
    import re
    while True:
        try:
            x=input("Hola,Ingrese las calificaciones separadas por comas:\n")
            x.strip()
            sepx=re.split(f'[,]',x)
            notasint=[int(a) for a in sepx]
            print(f"Las calificaciones son:\n{notasint}")
            break
        except:
            print("ERROR no se pudo separar alguna de las notas, ingreselas correctamente separadas por comas\nREINICIANDO PROGRAMA......\n")
calificaciones()
print("_____________________________________________________________________EJERCICIO 3:\n")
