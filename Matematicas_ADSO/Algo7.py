###
import math

print("2.1 ↓")
a= int(3*(2*(4**3))/4)
    #                   PASO 1
    # primero se resuelve lo que esta dentro del parentesis:
    # --> (2*(4**3))
    # dentro del paréntesis se resuelve el exponente 4**3, que es igual a 64
    # --> 2*64=128
    #                   PASO 2
    # se resuelve la multiplicación ya que se encuentra primero (a la izquierda).
    # --> 3*128=384
    #                   PASO 3
    # --> 384/4=96 <-- Respuesta final
print("  ",a)

print("---------------------------------------------------------------------------------------------------------------------------------------")
print("2.2 ↓")
    #                   CUANDO LOS NUMEROS TIENEN EL MISMO SIGNO
    # se suman los valores y se deja el signo que tengan, si son positivos signo positivo y si son negativos signo negativo. 
    # si no se pone nada delante del número se entiende que es +.
    # --> (+5)+(+4)=+9
    # es lo mismo que:
    # --> 5 + 4 = 9
    # (-5) + (-4) = -9. Es lo mismo que:
    # --> -5-4 = -9
print("Ejemplos números enteros del mismo signo.")
b= int(5+4)
print("   ",b)
b1= int(-5-4)
print("  ",b1)
    #                   CUANDO LOS NUMEROS TIENEN DIFERENTE SIGNO
    # 
    # Se restan sus valores absolutos y se pone el signo del sumando de mayor valor absoluto. (Se restan y se deja el signo del más grande en valor absoluto).
    # --> (+20) + (-10) = 20-10 = +10
    # 20-10 = 10, el más grande es +20, se pone +10
print("Ejemplos números enteros de distinto signo.")
b2= int(20-10)
print("  ",b2)
    # --> (-8) + (+3) = -8+3 = -5
    # 8-3 = 5, el más grande es el -8, se pone -5
b3= int(-8+3)
print("  ",b3)
    # --> (+11) + (-2) = 11-2 = +9
    # 11 - 2 = 9, el más grande es el 11, se pone + 9
b4= int(11-2)
print("   ",b4)
    #                  PARA MULTIPLICAR DOS NUMEROS ENTEROS
    # Se multiplican sus valores absolutos y se aplica la regla de los signos. Cuando van dos signos seguidos hay que separarlos utilizando paréntesis.
    # --> (+8) * (+3) = +24
print("Ejemplos multiplicacion de numeros enteros")
b5= int(8*3)
print("  ",b5)
    # --> (-3) * (-2) = +6
b6= int((-3)*(-2))
print("   ", b6)
    #                   PARA DIVIDIR DOS NUMEROS ENTEROS
    # Se divide el dividendo entre el divisor y se aplica la regla de los signos. Una división es exacta cuando el resto es 0.
    # --> (-15) ÷ (15) = -1
print("Ejemplos division de numeros enteros.")
b7= int((-15)/15)
print("  ", b7)
    # --> 8 ÷ 4 = +2
b8= int(8/4)
print("   ",b8)
    #                   PASO 1
    # Lo primero que debemos realizar es pasar el problema a términos aritméticos para empezar a resolverlo y sacamos los datos cuantitativos.
    #                   PASO 2
    # 1200 litros es la cantidad inicial de leche.
    #                   PASO 3
    # Luego debemos calcular la cantidad de leche que ingresa al depósito 
    # en los 20 minutos de funcionamiento: 25 litros que ingresan en un minuto lo multiplicamos por la cantidad de minutos que son veinte:
    # (25 litros * 20 minutos)
    #                   PASO 4
    # Así mismo calculamos la cantidad de leche que sale del depósito en los mismo 20 minutos: 35 litros que salen por minuto lo 
    # multiplicamos por la cantidad de minutos que son veinte:
    # (35 litros * 20 minutos)
    #                   PASO 5    
    # Ahora calculamos la cantidad total de leche que queda en el depósito después de 20 minutos.
    # A la leche que hay en el depósito, le sumamos la leche que ingresa y le restamos la leche que sale y quedaría una expresión aritmética de esta forma:
    # 1200 litros + (25 litros * 20 minutos) – (35 litros * 20 minutos)
    # Resolvemos los paréntesis y nos queda.
    # 1200 litros + 500 litros – 700 litros = 1000 litros
    # Luego realizamos las sumas y restas y nos da como resultado:
    # 1000 litros quedan en el depósito.
b9= int(1200 + (25 * 20) - (35 * 20))
print(f"   {b9} litros quedan en el deposito.")

print("---------------------------------------------------------------------------------------------------------------------------------------")
print("2.3 ↓")
    # --> 3/4 + 5/7
    #                   PASO 1
    # Se multiplican los denominadores.
    # --> 4*7 = 28      
    #                   PASO 2
    # Se multiplican el numerador de la primera fracción por el denominador de la segunda.
    # --> 3*7 = 21         
    #                   PASO 3
    # Se coloca el signo más. ( + )
    #                   PASO 4
    # Se multiplica el numerador de la segunda fracción por el denominador de la primera.
    # --> 4*5 = 20        
    #                   PASO 5
    # Por último, sumamos los dos números que nos quedan en el en la parte de arriba.
    # --> 21+20 = 41      

eq1=(4*7)
eq2=(3*7)
eq3=(4*5)
c= int(eq1+eq2/eq3)   
print("   ", c)

print("---------------------------------------------------------------------------------------------------------------------------------------")
print("2.4 ↓")
    # El producto de dos números racionales es otro número racional y se realiza multiplicando los numeradores entre sí y denominadores entre sí.
    # Pero mejor veamos un ejemplo:
    # --> 7/2 * 15/4 
    # --> = (7*15)/(2*4) 
    # --> = 105/8
d= int((7/2)*(15/4))
print("   ", d)
    # Para evidenciar en que se aplica la multiplicación de fracciones continuemos con 
    # la situación presentada anteriormente del campesino y sus cultivos.
    # Teniendo en cuenta que la finca del campesino cuenta con 1000 m2 y la fracción de ese terreno sembrada es de 17 / 35.
    # A. ¿Cuánto mide en metros cuadrados la parte del terreno que se encuentra sembrada?
    # B. Teniendo en cuenta que 2 / 7 se encuentra sembrada con papa, ¿Cuál es el área que se encuentra con papa?
    #Para encontrar la medida o el área del terreno sembrado multiplicamos el total de metros cuadrados (1000) 
    # por la fracción que se encuentre sembrada así:
    # Le ponemos el 1 de denominador al 1000 para que quede expresado como fracción.
    # --> (1000/1)*(17/35) = 17000/35
    # Simplificamos:
    # Recordemos que simplificar es dividir tanto el numerador como el denominador por el mismo número primo. 
    # En este caso el 17000 es divisible por 2 y por 5, mientras que el 35 es divisible por 5 y por 7. 
    # Así que dividimos ambos números por 5 y nos queda:
    # --> 17000/5 = 3400 and 35/5 = 7
    # Por último, dividimos la fracción y nos da como resultados que la cantidad de terreno que se encuentra sembrado es de 485.71 m2
    # La fracción quedaría.
    # 3400/7 = 485.71 m2
eqq1=(17000/5)
eqq2=(35/5)
d1= int(eqq1/eqq2)
print("   ", d1)

print("---------------------------------------------------------------------------------------------------------------------------------------")
print("2.5 ↓")
    # Para dividir dos números racionales se multiplica el numerador del primer número racional con el denominador del segundo número racional, 
    # y el numerador del segundo número con el denominador del primero. (Se multiplica en cruz) así:
    # --> (7/2)/(4/5) = 35/8 teniendo en cuenta que 7*5 = 35 y 2*4 = 8
e= int((7*2)/(4*5))
print("   ", e)
    # Ahora miremos una aplicación cotidiana.
    # Andrea compró un queso que pesa 3 / 4 de kilo, si lo partió 
    # en porciones de 1 / 8 de kilo, ¿Cuántas porciones salieron de la totalidad del queso?.
    # Lo que debemos hacer es dividir la cantidad de queso que hay entre 1/8 que es la porción que va a quedar.
    # --> (3/8)/(4/1) = 24/4 = 6
    # La cantidad de porciones de 1 / 8 que salen es de 6.
e1= int((3*8)/(4*1))
print("   ", e1)

print("---------------------------------------------------------------------------------------------------------------------------------------")
print("2.6 ↓")
    # La potenciación es la multiplicación de un número (n) veces, el mismo número entero o racional, en el la base es el 
    # número racional que multiplicaremos y n (Denominado exponente) es el número de veces que multiplicamos la base.
    # a**n = a . a . a . a . n veces
    # Potencia de base cero: cualquier potencia de base 0 es igual a 0, 0**4 = 0
f= int(0**4)
print("   ", f)
    # Potencia de exponente cero: cualquier potencia de exponente 0 es igual a 1, 5**0 = 1
f1= int(5**0)
print("   ", f1)
    # Potencia de exponente 1.	Cualquier potencia de exponente 1 es el mismo número. 7**1 = 7
f2= int(7**1)
print("   ", f2)
    # Producto de potencias de la misma base. El producto de potencias de la misma base es la misma base y 
    # el exponente la suma de los exponentes. 2**4 * 2**6 = 2**4 + **6 = 2**10
f3= int(2**10)
print("   ", f3)
    # Cociente de potencias de la misma base. El producto de potencias de la misma base es la misma base y el 
    # exponente de la suma de los exponentes. 3**5 / 3**2 = 3**5 - **2 = 3**3
f4= int(6**8)
print("   ", f4)
    # Potencia de una potencia.	La potencia de una potencia es la misma base y el exponente el producto de los exponentes.
    # --> (6**2)**4 = 6**2 * (**4) = 6**8
f5= int((2*4)**3)
print("   ", f5)
    # Producto de potencias con el mismo exponente.	El producto de potencias con el mismo exponente es una potencia con el mismo exponente y como base el producto de las bases. 
    # --> 2**3 * 4**3 = (2 * 4)**3
f6= int((2*4)**3)
print("   ", f6)
    # Cociente de potencias con el mismo exponente.	El cociente de potencias es una potencia con el 
    # mismo exponente y con base el cociente de las bases. 6**3 / 2**3 = ( 6 / 2 )**3 = 3**3
    # Potencia de exponente negativo. La potencia de exponente negativo es igual al inverso de la potencia, con exponente positivo. 
    # --> 4**-2 / 2 = 1/4**2
f7= int(1/(4**2))
print("   ", f7)
    # Potencia de exponente racional. La potencia de exponente racional es igual a una raíz, donde el denominador es el índice de la raíz y el numerador el exponente del radicando. 
    #  --> 7**4 / **3 = 3√7**4
f8= int((7**(4/3)))
print("   ", f8)
    # Radicacion 
    # La radicación es conocida como la operación contraria a la potenciación en donde se conoce el índice de la raíz y el radicando de este modo se puede encontrar un número que
    #  multiplicado el número de veces que enuncie el índice nos de como resultado el radicando.
    #





