#ARREGLOS DE ORDENAMIENTO
Numbers= []
Number=0 
i=0
for i in range (1,4):
    Number=int(input("Digite un numero \n"))
    Numbers.append(Number)

print("Numero de menor a mayor: ")
for i in range(0,3):
    Numbers.sort()
    print("--> ", Numbers[i])

print("Numero de mayor a menor: ")
for i in range(0, 3):
    Numbers.sort(reverse=True)
    print("--> ", Numbers[i])
    

