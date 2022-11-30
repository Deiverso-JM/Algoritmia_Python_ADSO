import math

def main():
    Salario_Basico=float(input("Digite el salario basico: "))
    Prima=float(input("Digite el valor de la prima de alimentacion: "))
    Descuento_Salud=(Salario_Basico*8)/100
    Descuento_Pension=(Salario_Basico*12)/100
    Descuento_Sindicato=(Salario_Basico*3)/100
    Descuento_fondo=(Salario_Basico*3)/100
    Salario_Neto=Salario_Basico+Prima+Descuento_fondo-Descuento_Pension-Descuento_Salud+Descuento_Sindicato
    print("El salario neto del empleado es: ", Salario_Neto)
    
    
    
    
if __name__ == '__main__':
    main()