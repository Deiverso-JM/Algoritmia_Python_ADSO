import math

def main():
    nombres=input("Digite el nombre del estudiante: ")
    apellidos=input("Digitel el apellido del estudiante: ")
    nota1=float(input("Nota 1: "))
    nota2=float(input("Nota 2: "))   
    nota3=float(input("Nota 3: ")) 
    
    pond_nota_1=(nota1*30)/100
    pond_nota_2=(nota2*30)/100  
    pond_nota_3=(nota3*40)/100
    
    nota_final=pond_nota_1+pond_nota_2+pond_nota_3
    print("La nota final de :", nombres," ", apellidos," :",nota_final)
    
    
if __name__ == '__main__':
    main()