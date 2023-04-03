#CONSTANTE
Salariomin=828.116

#VARIBALE DE ENTRADA
Name=input("Digite su nombre\n")
Cedula=input("Digite su cedula\n")
Diat=int(input("Digite los dias trabajados\n"))
Comis=float(input("Digite el total de venta del mes que hizo\n"))
salbasi=float(input("Digite su salario basico\n"))

#EN EL PROBLEMA NO MENCIONA LA PARTE DE DEDUCIONES PERO SE PRESENTAN VARIABLES ASI QUE ASUMIRE QUE UN VALOR DE ENTRADA
DEDUCIONES=float(input("Digite el valor de sus deduciones, si no tiene digite 0\n"))



#OPERACIONES DE VARIABLES
comision=Comis*0.02
sueldoDevenegado=(salbasi*Diat)/30
Totalsueldodevengado=sueldoDevenegado+comision


#LOGICA
if Diat >=1 and Diat <=30:

    if sueldoDevenegado <= (Salariomin*2):
        Auxt=(Diat*97.032)/30 #AUXILIO DE TRANSPORTE
        Sn=(Totalsueldodevengado-DEDUCIONES)
        print("Cedula del empleado: ", Cedula)
        print("Nombre del empleado: ", Name)
        print("Salario basico: ", salbasi)
        print("Auxilio de transporte: ", Auxt)
        print("Comision de ventas: ", comision)
        print("Prestamos: ", DEDUCIONES)
        print("El Salario netro a recibir es: ", Sn)
        

        print("El Salario netro a recibir es: ", Sn)
    else:
        Auxt=0
        Sn=(Totalsueldodevengado-DEDUCIONES)
        print("Cedula del empleado: ", Cedula)
        print("Nombre del empleado: ", Name)
        print("Salario basico: ", salbasi)
        print("Auxilio de transporte: ", Auxt)
        print("Comision de ventas: ", comision)
        print("Prestamos: ", DEDUCIONES)
        print("El Salario netro a recibir es: ", Sn)


else:
    print("USTED NO CUMPLE CON LO MINIMO DE DIAS TRABAJADOS - NO SALARIO")


