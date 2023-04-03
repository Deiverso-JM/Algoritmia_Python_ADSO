print("--------------------------------------------------------------")

#3.1 Operaciones con numeros

a=int(123-45)
b=int(123*45)
c=int(123**45)
d=int(123/45)
e=int(123//45)
f=int(123%45) 

print(f"Resultados: a) {a} || b) {b} || c) {c} || d) {d} || e) {e}  || f) {f}")



#Respuesta
#Los resultados son enteros


print("--------------------------------------------------------------")

#3.2

a=12.3 - 4.5
b=12.3* 4.5
c=12.3**4.5
d=12.3/4.5
e=12.3//4.5
f=12.3%4.5

print(f"Resultados: a) {a} || b) {b} || c) {c} || d) {d} || e) {e}  || f) {f}")

#Respuesta
#Los resultados si tienes resultados decimales

print("--------------------------------------------------------------")

#3.3

#a=12/0 
#b=34.5 / 0
#c=67 // 0

#print(f"Resultados: a) {a} || b) {b} || c) {c}")

#Respuesta
#No existe ya que la division por cero no se pued eo no existe.

print("--------------------------------------------------------------")

#3.4

#Segun las matemiticas todo numero elevado a la ptencia cero es 1, ahora con python:

a=0**0
print(f"Respuesta {a}")

#En python tambien se cumple esta propiedad

print("--------------------------------------------------------------")

#3.5

a=4-(3+2)   
b=(4-3)+2

print(f"Resultado: a) {a}, b) {b}")

#Se observa que las operaciones en parentesis se hacen primero por la jerarquia de operadores

print("--------------------------------------------------------------")

#3.6

a= 2-3+4-5  #Conjetura = -2
b=3/4*5/6   #Conjetura = 0.0024

print(f"Resultado: a) {a}, b) {b}")

#Resutlado
#Se realizan las operaciones de izquierda a derecha de forma secuencial

print("--------------------------------------------------------------")

#3.7



a=(-3)**-4

print(f"Resultado: a) {a}")

#La expresion es equivalente a (-3)^-4

print("--------------------------------------------------------------")

#3.8

a=3**(1/2)
b=4**(1/2)

print(f"Resultado: a) {a}, b) {b}")

#Los resultados son: a) es de tipo decimal o flotante y b) tipo entero 

print("--------------------------------------------------------------")

#3.9 

#para realizar empleamos el teorema de pitagoras

catetooPuesto=12
catetoadyacente=5

hipotenusa = (((catetooPuesto**2)+(catetoadyacente**2)))**(1/2)

print(f"EL valor de la hipotenusa del triangulo es: {hipotenusa}")

print("--------------------------------------------------------------")


#3.10
botellas1=4*100
botellas2=7*60

print(f"La cantidad de botellas compradas fue: {7+4}")
print(f"La cantidad total gastada fue: {botellas1+botellas2}")
promedio=(botellas1+botellas2)/11
print(f"EL valor de la promedio del de cada botella es: {promedio}")

print("--------------------------------------------------------------")

#3.11

#Inciiso A

Articulo = 100
yearOne = (Articulo*0.22)+Articulo
yearTwo = (yearOne*0.25)+yearOne

print(f"El total del articulo con la inflacion es de: {yearTwo}")


#Inciso B
Tasa1=22
tasa2=25

print(f"La inflacion promedio anula de los dos años sera de: {(Tasa1+tasa2)/2}% ")

#inciso C

anualInflae = ((60/30)**(0.5))-1
print(f"La inflacion anual seria de: {anualInflae*100}% mensual")

#inciso D
anualInflae=36/12
print(f"La inflacion anual seria de: {anualInflae}% mensual")


#inciso E

inflae = 3 
anualInflae=((1+0.03)**12)-1
print(f"La inflacion anual seria de: {anualInflae*100}% anual")

print("--------------------------------------------------------------")

#3.12

#Funciones abs(x), round(x)

#Inciso a
help(abs) #Da el valor absoluto de un numero

help(round) #Redondea el numero hasta valor entero o dependiendo de cuantos decimales quieres aproximar

#Inciso b

i= abs(12) #Da el valor absoluto del numero 
i2=round(12.3) #Redonde el numero
i3=round(-5.67) #Redonde el numero
i4=abs(-3.21) #Valor absoluto de un numero negativo es el numero positivo
print(f"Resultados : a) {i} b) {i2} c) {i3} d) {i4}")
#Inciso c

print(abs)
print(round)

#Mensaje de funciones propies sin argumento

#Inciso d

#Abs(2) 
#ABS(2)

#PYTHON NO identifica la funcion ya que si es extricto con las mayusculas y minisculas con las palabras reservadas

print("--------------------------------------------------------------")

#3.13

#INCISO a

i=round(123.4567,3) #DEJA TRES DECIMALES
i2=round(765.4321,2) #DEJA DOS DECIMALES 
print(f"Resultados: a) {i} b) {i2}")

#Inciso b

print(f"El promedio redondeado del ejercicio 3.10 seria de formato centavo: {round(promedio,2)}")

#Inciso c

carro=239400
print(f"El precio en mil sera: {round(carro,-3)} y en diez mil seria {round(carro,-4)}")

print("--------------------------------------------------------------")

#3.14 
 
print(f" a) {type(12)} and b) {type(12.3)}")  #Float
print(f" c) {round(12.3)} and d) {type(round(12.3))}")  #Entero
print(f" e) {98 // 76} and f) {type(98 // 76)}") #Entero
print(f" g) {98.0 // 76.0} and h) {type(98.0 // 76.0)}") #Float

print("--------------------------------------------------------------")

#3.15
print(f" a) {int(12.3)} and b) {type(int(12.3))}")  #Tipo entero
print(f" c) {float(-45)} and d) {type(float(-45))}")  #Tipo flotante

#3.16

#help(int)#Vuelve entero al valor
help(round) #Redodnde el valor

print(f" a) {int(1.2)} and b) {round(1.2)}")  
print(f" a) {int(1.7)} and b) {round(1.7)}")  
print(f" a) {int(-1.2)} and b) {round(-1.2)}")  
print(f" a) {int(1.7)} and b) {round(-1.7)}")  
print(f" a) {int(1.5)} and b) {round(1.5)}")  
print(f" a) {int(2.5)} and b) {round(2.5)}")  

#Pues al utilizar las dos funciones de esa manera seran valores enteros, entonces no hay diferencia, pero en la funcionalidad
#int toma el primero numero entero despuesd del 0 y round redondea los decimales hasta un punto

#3.17

print(f"A) valor: {12**34} and valor 2: {12.0**34}")
print(f"B) Valor: {1/12**34}")
print(f"C) Valor {12.3e45} and valor 2: {12.3e-45}")
print(f"D) {123**456}") #NUMERO ES DEMASIADO LARGO
print(f"E) {123.0**456.0}") #NUMERO ES DEMASIADO LARGO
