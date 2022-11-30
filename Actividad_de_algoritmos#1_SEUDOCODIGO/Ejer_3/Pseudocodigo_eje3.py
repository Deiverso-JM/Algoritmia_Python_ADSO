print("*******INICIO********")
n=""
i=1
print("-->Iniciamos el telefono")
print("-->Verificamos si tiene bateria el telefono")
n=input("¿El telefono tiene bateria? responda con si o no \n")
if(n=="si"):
    print("-->Seleccionamos la opcion de icono de llamadas")
    print("-->Seleccionamos la opcion de menu para el numero")       
    print("-->Digitamos el numero en teclado de la pantalla del telefono")    
    print("-->Seleccionamos la funciona llamar")    
    print("-->Verificamos que el telefono tiembre(llamada entre)")
    n=input("¿El telefono timbra o suena? responda con si o no \n")
    if(n=="si"):
        print("-->Esperamos a que conteste")
        print("-->Verficamos si contesto")
        n=input("¿Contesto? responda con si o no \n")        
        if(n=="si"):
            print("-->Iniciamos comversacion")
            print("*********FIN**********")
        else:
            while i<3:
                print("-->Digitamos el numero en teclado de la pantalla del telefono")    
                print("-->Seleccionamos la funciona llamar")
                print("-->Verificamos que el telefono tiembre(llamada entre)")
                n=input("¿El telefono timbra o suena? responda con si o no \n")
                if(n=="si"):
                    print("-->Espeamos a que conteste")
                    print("-->Verficamos si contesto")
                    n=input("¿Contesto? responda con si o no \n")
                    if(n=="si"):
                        print("-->Iniciamos comversacion")
                        print("*********FIN**********")
                        i=3
                    elif(i==2):
                        print("-->No contesto la llamada, valorate")
                        print("*********FIN**********")
                elif(i==2):
                    print("-->El telefono esta apagado, intenta mas tarde")
                    print("*********FIN**********")
                i=1+i            
    else:
        print("-->NO ENTRA LA LLAMADA")
        print("*********FIN**********")
        
        
        
else:
    print("-->Buscamos un cargador")
    n=input("¿Encontraste cargador? responde con si o no \n")
    if(n=="si"):
        print("-->Poner a cargar el celular")
        print("-->Verificamos si tiene bateria el telefono")
        n=input("¿El telefono tiene bateria? responda con si o no \n")
        if(n=="si"):
            print("-->Seleccionamos la opcion de icono de llamadas")
            print("-->Seleccionamos la opcion de menu para el numero")       
            print("-->Digitamos el numero en teclado de la pantalla del telefono")    
            print("-->Seleccionamos la funciona llamar")    
            print("-->Verificamos que el telefono tiembre(llamada entre)")
            n=input("¿El telefono timbra o suena? responda con si o no \n")
            if(n=="si"):
                print("-->Esperamos a que conteste")
                print("-->Verficamos si contesto")
                n=input("¿Contesto? responda con si o no \n")        
                if(n=="si"):
                    print("-->Iniciamos comversacion")
                    print("*********FIN**********")
                else:
                    while i<3:
                        print("-->Digitamos el numero en teclado de la pantalla del telefono")    
                        print("-->Seleccionamos la funciona llamar")
                        print("-->Verificamos que el telefono tiembre(llamada entre)")
                        n=input("¿El telefono timbra o suena? responda con si o no \n")
                        if(n=="si"):
                            print("-->Espeamos a que conteste")
                            print("-->Verficamos si contesto")
                            n=input("¿Contesto? responda con si o no \n")
                            if(n=="si"):
                                print("-->Iniciamos comversacion")
                                print("*********FIN**********")
                                i=3
                            elif(i==2):
                                print("-->No contesto la llamada, valorate")
                                print("*********FIN**********")
                        elif(i==2):
                            print("-->El telefono esta apagado, intenta mas tarde")
                            print("*********FIN**********")
                        i=1+i  
            else:
                print("-->El telefono esta apagado, intenta mas tarde")
                print("*********FIN**********")
        else:
            print("-->se le murio la bateria a tu telefono")
            print("*********FIN**********")    
    else:
        print("-->Sin cargardor, no hay llamada XD")
        print("*********FIN**********")