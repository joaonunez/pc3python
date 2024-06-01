from random import choice
def generar_numbers():
    numeros1_100=[]
    for i in range(100):
        numeros1_100.append(int(i+1))
    print(f"Los 100 numeros:\n {numeros1_100}")
    
    lista_random=[]
    for i in range(20):
        random=choice(numeros1_100)
        lista_random.append(int(random))
    print(lista_random)
    

    
    for recorrido in range(1,len(lista_random)):
        for posicion in range (len(lista_random)-recorrido):
            if lista_random[posicion]>lista_random[posicion+1]:
                temp = lista_random[posicion]
                lista_random[posicion]=lista_random[posicion+1]
                lista_random[posicion+1]=temp
    print(lista_random)
    pass

    