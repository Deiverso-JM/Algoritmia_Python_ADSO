
a=int(input("digita numero a: "))
b=int(input("digita numero b: "))

mul=a*b

if a>0 and b>0:
    print("Multiplicacion + por +: ", mul)
elif a>0 and b<0:
    print("Multiplicacion + por -: ", mul)
elif a<0 and b>0:
    print("Multiplicacion - por +: ", mul)
elif a<0 and b<0:
    print("Multiplicacion  por -: ", mul)
else: 
    print("no puedes multiplicar por 0.")