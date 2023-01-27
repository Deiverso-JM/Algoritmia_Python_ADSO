Num1=float(input("Digite el primer numero \n"))
Num2=float(input("Digite el segundo numero \n"))
print("Seleccionones una opcion a continuacion: \n 1. Suma \n 2. Resta \n 3. Multiplicacion \n 4. Division   ")
Op=int(input())

match Op:
    case 1:
        Res=Num1+Num2
        print("El resultado es: ", Res)     
    case 2:
        Res=Num1-Num2
        print("El resultado es: ", Res)        
    case 3:
        Res=Num1*Num2
        print("El resultado es: ", Res)     
    case 4:
        Res=Num1/Num2
        print("El resultado es: ", Res)     