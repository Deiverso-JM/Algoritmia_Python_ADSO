V1=[]
V2=[]

Num=int(input("Digite la cantidad el tamaño del vectores: \n"))

for i in range(0,Num):
    Entrada=int(input(f"Digite un numero {i} para ingresar al vector 1\n"))
    V1.append(Entrada)
    
    Entrada2=int(input(f"Digite un numero {i} para ingresar al vector 2\n"))
    V2.append(Entrada2)

print(V1)
print(V2)

    
for i in range(0,Num):
    if V1[i] in V2:
        print(f"El numero {V1[i]} del primer vector tambien existe en el vector 2")
    else:
        continue


