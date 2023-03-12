Matriz=[]
Matriztra=[]
cont=0
Tamañofila=int(input("Digite el numero de filas: "))
Tamañocolum=int(input("Digite el numero de columnas: "))

for i in range(0,Tamañofila):
    Matriz.append([])
    for l in range(0,Tamañocolum):
        numero=int(input(f"Escriba una Letra para la fila {i} con columna {l} de la matriz\n"))
        Matriz[i].append(numero)

print("Seleciones una opcion: \n 1.Diagonal \n 2.Transpuesta")
Opcion=int(input())

if Opcion == 1:
    if(Tamañocolum==Tamañofila):
        for i in range(0,Tamañofila):
            Matriz[i][cont]=0
            cont+=1

        print("MATRIZ PRINCIPAL")
        for i in Matriz:
            print(i, end="")
            print("")          
    else:
        print("No es una matriz cuadrada no se puede su diagonal")
    
elif Opcion ==2:
    for i in range(0,Tamañocolum):
        Matriztra.append([])
        for l in range(0,Tamañofila):
            numero=Matriz[l][i]
            Matriztra[i].append(numero)
    
    
    print("MATRIZ PRINCIPAL")
    for i in Matriz:
        print(i, end="")
        print("")
    
    print("MATRIZ TRANSPUESTA")
    for i in Matriztra:
        print(i, end="")
        print("")         
          
    


        




    
    
