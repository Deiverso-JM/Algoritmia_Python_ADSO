#RAIZ CON INDICE MAYOR A 2

A=int(input("Digite un numero para su Radicado \n"))
indice=int(input("Digite su Exponente de la raiz, si no tiene coloque 1"))
potencia=int(input("Digite la potencia de su radicado, si no tiene coloque 1"))


if A>0:
    Resultado=A**(potencia/indice)
    print("El resultado es: ", Resultado)
else:
    print("Raiz negativa no existe.") 
