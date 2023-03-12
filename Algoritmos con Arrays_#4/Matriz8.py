Matriz=[]
Matriz2=[]
Suma=[]

Tamañofila=int(input("Digite el numero de filas de las matrizes: "))
Tamañocolum=int(input("Digite el numero de columnas de las matrizes: "))


for i in range(0,Tamañofila):
    Matriz.append([])
    for l in range(0,Tamañocolum):
        numero=int(input(f"Escriba un numero para la fila {i} con columna {l} de la matriz 1\n"))
        Matriz[i].append(numero)
        
        
        
        
for i in range(0,Tamañofila):
    Matriz2.append([])
    for l in range(0,Tamañocolum):
        numero=int(input(f"Escriba un numero para la fila {i} con columna {l} de la matriz 2 \n"))
        Matriz2[i].append(numero)
        
        
        
for i in range(0,Tamañofila):
    Suma.append([])
 
    for l in range(0,Tamañocolum):
        n=Matriz[i][l] + Matriz2[i][l]
        Suma[i].append(n)
        
        


for i in Suma:
    print(i, end=" ")
    print("")

        