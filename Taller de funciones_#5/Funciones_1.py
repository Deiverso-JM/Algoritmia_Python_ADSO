def Operaciones_matematicas():
    
    a=float(input("Digite el primer numero \n "))
    b=float(input("Digite el segundo numero\n"))


    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    opcion=int(input("Escoja una operacion \n"))


    match opcion:
        case 1:
            suma(a,b)
        case 2:
            resta(a,b)
        case 3:
            multiplicacion(a,b)
        case 4:
            division(a,b)
        case 5:
            potencia(a,b)
    


def suma(a,b):
    print(f"Suma = {a+b}")

def resta(a,b):
    print(f"Resta = {a-b}")


def multiplicacion(a,b):
    print(f"Multiplicacion = {a*b}")


def division(a,b): 
    print(f"Division = {a/b}")

def potencia(a,b):
    p=float(input("Digite el grado de la potencia\n"))
    print(f"Potencia de a es: {a**p}")
    print(f"Potencia de b es: {b**p}")







if __name__=="__main__":
    Operaciones_matematicas()