Dura=int(input("Digite la duracion de la llamada\n"))

if Dura <= 3:
    print("El costo total de la llamada es: $200" )
elif Dura > 3:
    Dura2=Dura-3
    Totalp=200+(Dura2*30)
    print("El costo total de la llamada es: $", Totalp )
    