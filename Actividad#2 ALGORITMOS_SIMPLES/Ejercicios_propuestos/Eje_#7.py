i=1
cont=0
nota=0
while i <= 5:
    print("Digite la nota # ", i, ":")
    nota=float(input())
    cont=cont+nota
    i=i+1

Prom=cont/5
print("El promedio de notas es de: ", Prom )