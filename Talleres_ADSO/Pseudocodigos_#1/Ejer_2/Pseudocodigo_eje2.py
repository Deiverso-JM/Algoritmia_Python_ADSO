print("****************inicio******************")
n=""
i=1
print("-->Buscamos los ingredienrtes y herramientas para la pasta")
n=input("¿Hay ingredientes? Responda solamente con si o no \n ")
if(n=="si"):
    print("-->Encendemos el fogon")
    n=input("¿Encendio el fogon? Responda solamente con si o no \n ")    
    if(n=="si"):
        print("-->Colacamos la olla en la estufa")
        print("-->Verificamos si hay agua")
        n=input("¿Hay agua? Responda solamente con si o no \n") 
        if(n=="si"):  
            print("-->Echamos agua en la olla")
            print("-->echamos cucharadas de sal")
            print("-->echamos los ingridentes")
            print("-->Movemos la pasta con cuidado")
            print("-->Verificamos que la pasta esta lista")
            n=input("¿La pasta esta lista? Responda solamente con si o no \n")
            if(n=="si"):
                print("-->Apagamos el fogon y servimos la pasta")
                print("******************FIN*****************")
            else:
                while i<3:
                    print("-->Verificamos que la pasta esta lista")
                    n=input("¿La pasta esta lista? Responda solamente con si o no \n")
                    if(n=="si"):
                        print("-->Apagamos el fogon y servimos la pasta")
                        print("******************FIN*****************")
                        i=3
                    elif(i==2):
                        print("-->Se quemo la pasta")
                        print("-->llora :C")
                        print("******************FIN*****************")
                    i=i+1
        else:
            print("-->No hay agua, no hay pasta :C")
            print("******************FIN*****************")
    elif(n=="no"): #GUIA DEL NO
        print("-->Verifcamos si hay gas")
        n=input("¿Hay gas? Responda solamente con si o no \n")
        if(n=="si"):
            print("-->Encendemos el fogon de la estufa")
            n=input("¿Encendio el fogon? Responda solamente con si o no \n")
            if(n=="si"):
                print("-->Colocamos la olla en la estufa") #INICI DEL GAS --- GUIA
                print("-->Verificamos si hay agua")
                n=input("¿Hay agua? Responda solamente con si o no \n") 
                if(n=="si"):
                    print("-->Echamos agua en la olla")
                    print("-->echamos cucharadas de sal")
                    print("-->echamos los ingridentes")
                    print("-->Movemos la pasta con cuidado")
                    print("-->Verificamos que la pasta esta lista")
                    n=input("¿La pasta esta lista? Responda solamente con si o no \n")
                    if(n=="si"):
                        print("-->Apagamos el fogon y servimos la pasta ")
                        print("******************FIN*****************")
                    else:
                        while i<3:
                            print("-->Verificamos que la pasta esta lista")
                            n=input("¿La pasta esta lista? Responda solamente con si o no \n")
                            if(n=="si"):
                                print("-->Apagamos el fogon y servimos la pasta")
                                print("******************FIN*****************")
                                i=3
                                
                            elif(i==2):
                                print("-->Se quemo la pasta")
                                print("-->llora :C")
                                print("******************FIN*****************")
                            i=i+1
                else:
                    print("-->No hay agua, no hay pasta :C")
                    print("******************FIN*****************")
            else:
                print("-->Se daño la estufa")
                print("******************FIN*****************")
        else:
            print("No hay gas, no hay pasta :C")
            print("******************FIN*****************")      
else:
    print("-->Verficamos si hay dinero para ingredientes")
    n=input("¿Compramos ingredientes? Responda solamente con si o no \n")
    if(n=="si"):
        print("Encendemos el fogon")
        n=input("¿Encendio el fogon? Responda solamente con si o no \n") 
        if(n=="si"):
            print("-->Colacamos la olla en la estufa")
            print("-->Verificamos si hay agua")
            n=input("¿Hay agua? Responda solamente con si o no \n") 
            if(n=="si"):
                print("-->Echamos agua en la olla")
                print("-->echamos cucharadas de sal")
                print("-->echamos los ingridentes")
                print("-->Movemos la pasta con cuidado")
                print("-->Verificamos que la pasta esta lista")
                n=input("¿La pasta esta lista? Responda solamente con si o no \n")
                if(n=="si"):
                    print("-->Apagamos el fogon y servimos la pasta")
                    print("******************FIN*****************")
                else:
                    while i<3:
                        print("-->Verificamos que la pasta esta lista")
                        n=input("¿La pasta esta lista? Responda solamente con si o no \n")
                        if(n=="si"):
                            print("-->Apagamos el fogon y servimos la pasta")
                            print("******************FIN*****************")
                            i=3
                        elif(i==2):
                            print("-->Se quemo la pasta")
                            print("******************FIN*****************")
                            print("-->llora :C")
                            print("******************FIN*****************")
                        i=i+1
            else:
                print("-->No hay agua, no hay pasta :C")
                print("******************FIN*****************") 
        else:
            print("-->Verifcamos si hay gas")
            n=input("¿Hay gas? Responda solamente con si o no \n")
            if(n=="si"):
                print("-->Encendemos el fogon de la estufa")
                n=input("¿Encendio el fogon? Responda solamente con si o no \n")
                if(n=="si"):
                    print("-->Colocamos la olla en la estufa") #INICI DEL GAS --- GUIA
                    print("-->Verificamos si hay agua")
                    n=input("¿Hay agua? Responda solamente con si o no \n") 
                    if(n=="si"):
                        print("-->Echamos agua en la olla")
                        print("-->echamos cucharadas de sal")
                        print("-->echamos los ingridentes")
                        print("-->Movemos la pasta con cuidado")
                        print("-->Verificamos que la pasta esta lista")
                        n=input("¿La pasta esta lista? Responda solamente con si o no \n")
                        if(n=="si"):
                            print("-->Apagamos el fogon y servimos la pasta ")
                            print("******************FIN*****************")
                        else:
                            while i<3:
                                print("-->Verificamos que la pasta esta lista")
                                n=input("¿La pasta esta lista? Responda solamente con si o no \n")
                                if(n=="si"):
                                    print("-->Apagamos el fogon y servimos la pasta")
                                    print("******************FIN*****************")
                                    i=3
                                elif(i==2):
                                    print("-->Se quemo la pasta")
                                    print("-->llora :C")
                                    print("******************FIN*****************")
                                i=i+1
                    else:
                        print("-->No hay agua, no hay pasta :C")
                        print("******************FIN*****************") 
                else:
                    print("-->Se daño la estufa")
                    print("******************FIN*****************")
            else:
                print("-->No hay gas, no hay pasta :C")
                print("******************FIN*****************") 
    else:
        print("-->No hay ingredientes, no hay pasta :C")
        print("******************FIN*****************") 
        
