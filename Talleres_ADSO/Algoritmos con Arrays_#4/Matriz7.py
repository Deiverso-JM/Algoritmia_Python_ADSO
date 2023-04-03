Matriz=[]
Numpares=[]
Numimpar=[]
Positivos=[]
Negativos1=[]
Tamañofila=int(input("Digite el numero de filas: "))
Tamañocolum=int(input("Digite el numero de columnas: "))

for i in range(0,Tamañofila):
    Matriz.append([])
    for l in range(0,Tamañocolum):
        numero=int(input(f"Escriba un numero para la fila {i} con columna {l} \n"))
        Matriz[i].append(numero)
        if numero >0:
            Positivos.append(numero)
        elif numero <0:
            Negativos1.append(numero)
        
        if numero % 2 ==0:
            Numpares.append(numero)
        else:
            Numimpar.append(numero)



print("Los numeros impares que existen en la matriz son: " , Numimpar)
print("Los numeros Pares que existen en la matriz son: " , Numpares)
print("Los numeros positivos que existen en la matriz son: " ,Positivos)
print("Los numeros negativos que existen en la matriz son: " ,Negativos1)

            
        
