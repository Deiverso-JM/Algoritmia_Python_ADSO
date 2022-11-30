import math

def main():
    #DOCUMENTOS
    ident=str(input("Digite su numero de identificacion: "))
    Names=str(input("Digite sus nombres: "))
    Apeliido=str(input("Digite sus apellidos: "))
    
    
    #DATOS
    Salario_Basico=float(input("Digite el salario basico: \n"))
    Comisiones_de_ventas=float(input("Digite Su comision de ventas: \n"))
    Subcidio_T=float(input("Digite su el valor del subcidio de transporte: \n"))
    Descuento_Salud=(Salario_Basico*4)/100
    Descuento_Pension=(Salario_Basico*8)/100
    Descuento_libranza=200000
    Salario_Neto=(Salario_Basico+Comisiones_de_ventas+Subcidio_T)-(Descuento_Salud+Descuento_Pension+Descuento_libranza)
    
    #PANTALLA
    print("El identificador del empleado es: ", ident)
    print("El nombre del empleado es: ", Names)
    print("El apellido del empleado es: ", Apeliido)
    print("El salario neto del empleado es: ", Salario_Neto)
    
    
if __name__ == '__main__':
    main()