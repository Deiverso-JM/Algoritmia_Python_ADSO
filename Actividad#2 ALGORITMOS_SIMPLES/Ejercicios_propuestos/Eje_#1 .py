#CUADRADO AREA ES MULTIPLICAION DE SUS DOS LADOS

lad_1=float(input("Digite la longitud del lado vertical del cuadrado: \n"))
lad_2=float(input("Digite la longitud del lado horizontal del cuadrado: \n"))

def Area_Cuadrado(lado_1, lado_2):
    area=lad_1*lad_2
    print("El area del cuadrado es: ", area)
    
    
    
if __name__ == "__main__":
    Area_Cuadrado(lad_1,lad_2)