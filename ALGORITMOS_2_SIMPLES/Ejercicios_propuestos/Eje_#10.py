#LIST
cont=0
letra=str(input("Digite una letra \n"))
for i in ("a","e","i","o","u","A","E","I","O","U"):
    if (letra==i):
        print("Es una bocal")
        continue
    cont=cont+1
    if(cont==10):
        print("No es una bocal")