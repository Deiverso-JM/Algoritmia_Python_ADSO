num=0 
num=int(input("Digite un numero para saber los divisiores de un numero\n"))
print("Los numero divisores son: ")
for i in range(1,(num+1)):
    if (num % i == 0):
        print("--->  ", i)
    
        


