import math

def main():
    peso=float(input("Digite el peso(KG): " ))
    altura=float(input("Digite la altura (mts): "))
    IMC=peso/(altura**2)
    print("Su indice de masa corporal es: ", IMC)
    
    
    
    
if __name__ == '__main__':
    main()