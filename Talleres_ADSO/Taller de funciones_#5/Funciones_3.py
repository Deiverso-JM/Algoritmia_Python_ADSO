import math


def main():
    print("Escoja una opcion de como quiere cargar e imprimir:")
    print("1. Area de un circulo")
    print("2. Area de un cuadrado")
    print("3. Area de un triangulo")
    
    opcion=int(input(""))

    if opcion == 1:
        Areacirculo()
        
    elif opcion == 2:  
        Areacuadrado()
    else:
        Areatriangulo()
    
    
def Areatriangulo():
    A=float(input("Digite la Base del triangulos\n"))
    B=float(input("Digite la Altura del Triangulo\n"))
    Area=(A*B)/2
    print(f"El area del Circulo es: {Area}")
    
  
    
    
def Areacuadrado():
    A=float(input("Digite la diagonal del cuadrado\n"))
    Area=(A*A)/2
    print(f"El area del cuadrado es: {Area}")

    
    
def Areacirculo():
    A=float(input("Digite el radio del circulo\n"))
    Area=math.pow(A,2)*math.pi
    print(f"El area del Circulo es: {Area}")
    
    
    
    
    
    
if __name__ == "__main__":
    main()