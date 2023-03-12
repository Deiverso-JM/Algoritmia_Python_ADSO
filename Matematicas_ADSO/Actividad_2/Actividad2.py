totalU=1350 #VALORES CONSTANTES
totalVU=132000000 #VALOR CONSTANTE

TrabU=[250,480,120]  #ARREGLOS DE TRABAJADOR POR SUS UNIDADES
ValorTrab=[120000,280000,80000] #ARREGLO DE TRABAJADOR POR EL PRECIO DE SUS PRODUCTOS

PorceU=[]       #ARREGLO DE PORCENTAJE DE UNIDADES
PorceVU=[]      #ARREGLO DE PORCENTAJE DE VALOR UNITARIO
acumuladorPorceU=0  #ACUMULADOR DE PORICENTAJE UNIDAD
acumuladorPorceVU=0 #ACUMULADOR DE PORICENTAJE VALOR UNITARIO

for i in range(0,3):
    N=(TrabU[i]*100)/totalU       #OPERACION DE PROCNETAJE DE UNIDADES
    N2=((ValorTrab[i]*TrabU[i])*100)/totalVU #OPERACION DE PROCNETAJE DE VALOR UNITARIO
    acumuladorPorceVU=acumuladorPorceVU+N2  #ACUMULADOR DE PORCENTAJE DE UNIDADES
    acumuladorPorceU=acumuladorPorceU+N  #ACUMULADOR DE PORCENTAJE DE VALOR UNITARIO
    PorceU.append(N)  #AÑADIR A VECTOR 
    PorceVU.append(N2) #AÑADIR A VECTOR 


#SALIDAS
print(f"El porcentaja de unidades asigandos a los trabajadores de las unidades totales fue de: {acumuladorPorceU}% y el restante de unidades es de: {100-acumuladorPorceU}%")

print(f"El porcentaja de valorunitario asigandos a los trabajadores de las unidades totales fue de: {acumuladorPorceVU}% y el restante se excedio: {acumuladorPorceVU-100}%")