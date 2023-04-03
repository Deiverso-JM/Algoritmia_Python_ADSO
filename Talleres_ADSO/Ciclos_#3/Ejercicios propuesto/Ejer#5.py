#5

Edad=int(input("Digite su edad por favor \n"))


match Edad:
    case Edad if Edad >= 18 and Edad < 60 : print("La persona es adulta y esta apta para votar")
    case Edad if Edad < 18: print("Es menor de edad") 
    case Edad if Edad >= 60 : print("La persona es adulto mayor y esta apta para votar")
    