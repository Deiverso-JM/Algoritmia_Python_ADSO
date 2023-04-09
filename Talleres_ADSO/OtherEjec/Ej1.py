# multiplicar dos números sin usar el símbolo de multiplicación
a=5
b=2
resul=0
for x in range(a):
    resul+=2

print("resultado:",resul) 

#Ingresa nombre y apellido e imprimelo alreves

nombre= "Pedro"
apellido="Perez"

resul=nombre+"  "+apellido
print(resul[::-1])

#Escribir una fucion que encuentre el numero menor de un lista

numeros=[1,2,0,2,4,-5,1]
def numero(numeros):
    numeros.sort()
    print(numeros)
    print(f"El numero menor de la lista es {numeros[0]} ")

#numero(numeros)

#Escribir una funcion que devuelve el volumen de una esfera por su radio    

from math import pi


def volumen():
    radio=float(input("De cuanto es el radio de la esfera:\n "))
    volumen=4/3*pi*radio**3
    print(f"el volumen tiene valor de: {volumen}")

#volumen()

#Escribir si una funcion para saber si es mayor de edad
def edad():
    edad1=int(input("Escribe tu edad: "))
    if edad1 >=18:
        print("Es mayor de edad")
    else:
        print("No es mayor de edad")

#edad()

#Escribir una funcion para saber si es par o impar

class numeropareimpar():
    def __init__(self,numero):
        self.numero=numero
    
    def idennumer(self):
        if self.numero % 2 == 0:
            print("El numero es par")
        else:
            print("El numero no es par, es impar")

#Numberloco= numeropareimpar(8)

#Numberloco.idennumer()

#Escribir una funcion que indique cuatas vocales tiene una palabra

palabra='HOLA'
palabra = palabra.lower()
vocales = ['a','e','i','o','u']
cont=0
for i in palabra:

    if i in vocales:
        cont+=1
    else:
        continue 
    
print(cont)

#Escribir una aplicacion que reciba una cantidad infinita de numeros hasta decir basta
#Decir basata, luego devuelva la suma de los numeros ingresados


# class app():
#     def __init__(self,numero, suma):
#         self.numero = numero
#         self.suma =  suma

# numeroelegido= app(0,0)

# while(True):
#     numeroelegido.numero=int(input("Digite un numero: "))
#     numeroelegido.suma+=numeroelegido.numero
#     try:
#         where=str(input("Desea continuar escriba si, si no Basta\n"))
#         if where.lower() == 'basta':
#             print("La suma de los numeros ingresados es: ", numeroelegido.suma)
#             break
#         elif(where.lower() == 'si'):
#             continue
#         else:
#             exit()
#     except:
#         print("Debes ingresar un respuesta valida")
#         exit()

#Escribir una funcion que reciba nombre y apellido y los vayaa agragando a un archivo
def agread(nombres, apellidos):
    Documento=open('Talleres_ADSO/Otherejec/Nombres.txt', 'a')
    Documento.write(f"\n Su nombres: {Nombres} y su apellido es:  {apellidos}")
    
    Documento.close()

Nombres=str(input("Escribe tu nombre\n"))
apellidos=str(input("Escribe tu apellido\n"))

agread(Nombres, apellidos)     
