Matriz=[]
Matriz2=[]
Matrizpro=[]

Sumador=0
con=0
Tamañofila=int(input("Digite el numero de filas: "))
Tamañocolum=int(input("Digite el numero de columnas: "))



for i in range(0,Tamañofila):
    Matriz.append([])
    for l in range(0,Tamañocolum):
        numero=int(input(f"Escriba una Letra para la fila {i} con columna {l} de la matriz 1\n"))
        Matriz[i].append(numero)
        
for i in range(0,Tamañofila):
    Matriz2.append([])
    for l in range(0,Tamañocolum):
        numero=int(input(f"Escriba una Letra para la fila {i} con columna {l} de la matriz 2\n"))
        Matriz2[i].append(numero)
        
print("MATRIZ PRINCIPAL 1")
for i in Matriz:
    print(i, end="")
    print("")  



print("MATRIZ PRINCIPAL 2")
for i in Matriz2:
    print(i, end="")
    print("")  
      
#PROCESO DE PRODUCTO

for i in range(len(Matriz)):
    Matrizpro.append([0]*Tamañocolum)



for i in range(Tamañofila):
    for l in range(Tamañocolum):
        for k in range(Tamañocolum):
            Matrizpro[i][l] += Matriz[i][k]* Matriz2[k][l]       
                
     
        



print("MATRIZ Producto")
for i in Matrizpro:
    print(i, end="")
    print("")  



            
        
