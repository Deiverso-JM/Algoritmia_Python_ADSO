Matriz=[]
Vocales=[]
VocalesM=['a','e','i','o','u']
Tamañofila=int(input("Digite el numero de filas: "))
Tamañocolum=int(input("Digite el numero de columnas: "))

for i in range(0,Tamañofila):
    Matriz.append([])
    for l in range(0,Tamañocolum):
        numero=str(input(f"Escriba una Letra para la fila {i} con columna {l} de la matriz\n"))
        Matriz[i].append(numero)
        if Matriz[i][l].lower() in VocalesM:
            Vocales.append(Matriz[i][l])



print(Vocales)






