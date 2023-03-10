V1=[]
V2=[]

Num=int(input("Digite la cantidad el tamaño del vectores: \n"))

for i in range(0,Num):
    Entrada=int(input(f"Digite un numero {i} para ingresar al vector 1\n"))
    V1.append(Entrada)
    
for i in range(0,Num):
    Entrada2=int(input(f"Digite un numero {i} para ingresar al vector 2\n"))
    V2.append(Entrada2)
    
    
Suma=[]
Resta=[]
Multiplicacion=[]
Division=[]

for i in range(0,Num):
    Suma.append((V1[i]+V2[i]))
    Resta.append((V1[i]-V2[i]))
    Multiplicacion.append((V1[i]*V2[i]))
    Division.append((V1[i]/V2[i]))
    
    
    
print("Vector Suma:")
print(Suma)
print("Vector Resta:")
print(Resta)
print("Vector Multiplicacion:")
print(Multiplicacion)
print("Vector Divsion:")
print(Division)
