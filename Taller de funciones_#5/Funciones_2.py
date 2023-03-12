
def main():
    print("Escoja una opcion de como quiere cargar e imprimir:")
    print("1. Vector")
    print("2. Matriz")
    opcion=int(input(""))

    if opcion == 1:
        Vector()
    else:  
        Matriz()




def Vector():
    Tamaño=int(input("Digite el tamaño del vector\n"))
    Vector=[]
    for i in range(0,Tamaño):
        numero=float(input(f"Escriba un numero {i} \n"))
        Vector.append(numero)
    print("El vector es:")
    print(Vector)
    
    

def Matriz():
    Matriz=[]
    Tamañocolum=int(input("Digite el numero de columbas\n"))
    Tamañofila=int(input("Digite el numero de filas\n"))


    for i in range(0,Tamañofila):
        Matriz.append([])
        for l in range(0,Tamañocolum):
            numero=int(input(f"Escriba un numero para la fila :{i} con columna {l} \n"))
            Matriz[i].append(numero)
        
    
    for i in range(0,Tamañofila):
        print("[",end="")    
        for l in range(0,Tamañocolum):
            print(" ",Matriz[i][l],"  ", end="")
        print("]")
    
        






if __name__ == "__main__":
    main()