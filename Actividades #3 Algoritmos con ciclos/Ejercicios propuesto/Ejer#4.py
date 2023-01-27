cont=0
num=0 
num=int(input("Digite un numero para saber si es perfecto\n"))
for i in range(1,num):
    if (num % i == 0):
        cont=cont+i



if(cont==num):
    print("Es un numero perfecto")
else: 
    print("No es un numero perfecto")
    
    
        
