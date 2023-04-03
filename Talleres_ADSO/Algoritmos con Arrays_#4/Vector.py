V1=[]

Num=int(input("Digite la cantidad el tamaño del vector: \n"))


for i in range(0,Num):
    Entrada=int(input("Digite un numero para ingresar al vector\n"))
    V1.append(Entrada)
    
V1.sort()
print("El numero mayor es: ", V1[Num-1])
print("El numero menor es: ", V1[0])