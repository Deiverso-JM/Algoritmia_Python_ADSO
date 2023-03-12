V1=[]


Num=int(input("Digite la cantidad el tamaño del vector: \n"))


for i in range(0,Num):
    Entrada=int(input("Digite un numero para ingresar al vector\n"))
    V1.append(Entrada)


Conta=0

for Nume in V1:
    if Nume > 1:
        primo=True
        for i in range(2, Nume):
            if(Nume % i ==0):
                primo=False
                break
        if primo:
            Conta+= 1
                
    
print("la candtidad de numeros primos que hay en el arreglo son: ",Conta)

