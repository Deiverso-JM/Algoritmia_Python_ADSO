import math
lad_1=float(input("Digite la longitud de un lado del triangulo equilatero: \n "))

def Area_Cuadrado(lado_1):
    area=math.pow(lado_1,2)*math.sqrt(3)/4
    print("El area del cuadrado es: ", area)
    

    
if __name__ == "__main__":
    Area_Cuadrado(lad_1)