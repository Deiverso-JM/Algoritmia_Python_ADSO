#Metodo append

Number=[1,2,3,4]
Number.append(5)
print(Number)

#METODO COPY
Number=[1,2,3,4]
Number2=Number.copy()
print(Number)
print(Number2)

#Metodo extend

Letras=[]
Letras.extend("MANZANA")
print(Letras)

#Metodo insert

paises=["Fracia", "Paris", "España"]
print(paises)
paises.insert(2,"Alemania")
print(paises)

#Metodo remove

paises=["Fracia", "Paris", "España"]

print(paises)

paises.remove("España")

print(paises)

#Metodo sort

lista=[2,9,4,10]
print(lista)
lista.sort()
print(lista)

#Metodo CLEAR

lista=[2,9,4,10]
print(lista)
lista.clear()
print(lista)

#METODO COUNT

lista=[2,9,4,10,9]
print(lista)
print(lista.count(9))

#METODO INDEX

lista=[2,9,4,10,9,10]
print(lista)
print(lista.index(10))



#METODO POP

lista=["A","B","E","X"]
print(lista)
lista.pop()
print(lista)

#METODO REVERSE

lista=[2,9,4,10]
print(lista)
lista.reverse()
print(lista)