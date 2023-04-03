V1=[]

Num=int(input("Digite la cantidad el tamaño del vector: \n"))


for i in range(0,Num):
    Entrada=int(input("Digite un numero para ingresar al vector\n"))
    V1.append(Entrada)



for i in range(0,Num):
    if V1.count(V1[i]) >= 2 and V1[i] != V1[i+1]:
        print(f"El numero {V1[i]} se repite en el vector:  {V1.count(V1[i])} veces")


print(V1)   
    
    
