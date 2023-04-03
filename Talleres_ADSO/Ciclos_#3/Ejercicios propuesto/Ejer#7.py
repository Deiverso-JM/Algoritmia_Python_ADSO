#MESES
Meses=("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre","Diciembre" )
num=0 
num=int(input("Digite un numero\n"))

if(num >=13):
    print("El numero no corresponde a ningun mes del año")
else:
    print("El numero corresponde al mes del año:", Meses[num])