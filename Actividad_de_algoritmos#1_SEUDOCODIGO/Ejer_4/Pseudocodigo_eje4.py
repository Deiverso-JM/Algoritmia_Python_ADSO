print("******INICIO********* \n")
n=""
i=1
print("-->Suena la alarma y me despierto \n")
print("-->Verificamos si la hora es 5:30am o mas \n")
n=input("¿La hora es 5:30am o mas? responda solo con si o no \n")
if(n=="si"):
    print("-->Me siento en la cama a reflexionar \n")
    print("-->Me hago las preguntas sobre mi existencia \n")
    print("-->Me levanto de la cama, reviso la organizacion del dia que hice ayer \n")
    print("-->Entro al baño, me aseo y me alisto para salir \n")
    print("-->Verifico mi bolso, si no se me queda nada \n")
    n=input("¿Se me queda algo? responda solo con si o no \n")
    if(n=="si"):
        while i<3:
            print("-->Verifico mi bolso, si no se me queda nada \n")
            n=input("¿Se me queda algo? responda solo con si o no \n")
            if(n=="si"):
                i=i+1
                if(i==3):
                    print("Te dejo la ruta, demoraste mucho buscando")
                    print("***FIN***")     
            else:
                print("-->Salgo de la casa y voy a la parada de la ruta\n")
                print("-->Esquivo al ladron, llego a la parada de la ruta\n")
                i=1
                while i<3:
                    print("-->verifico que la ruta pase \n")
                    n=input("¿La ruta paso? responda solo con si o no \n")
                    if(n=="si"):
                        print("-->Me monto en la ruta \n")
                        print("-->Veo lastimosa la cara de santana y kevin \n")
                        print("-->Me siento y tomo un micro-sueño hasta que llegamos al hermoso CBC \n")
                        print("-->Verfico que llegamos al CBC \n")
                        n=input("¿LLegamos al CBC? responda solo con si o no \n")
                        if(n=="si"):
                            print("-->Me bajo de la ruta \n")
                            print("***FIN***")
                            i=3
                        else:
                            while i<3:
                                print("-->Verfico que llegamos al CBC \n")
                                n=input("¿LLegamos al CBC? responda solo con si o no \n")
                                if(n=="si"):
                                    print("-->Me bajo de la ruta \n")
                                    print("***FIN***")
                                    i=3 
                                else:
                                    i=i+1
                                    if(i==3):
                                        print("-->La ruta se varo, F \n")   
                                        print("***FIN***")
                    else:
                        i=i+1
                        if(i==3):
                            print("-->Grande CBC, la ruta no paso \n")
                            print("***FIN***")
                        
                        
                        
                        
                        
                                              
    else:
        print("-->Salgo de la casa y voy a la parada de la ruta\n")
        print("-->Esquivo al ladron, llego a la parada de la ruta\n")
        print("-->verifico que la ruta pase \n")
        n=input("¿La ruta paso? responda solo con si o no\n")
        if(n=="si"):
            print("-->Me monto en la ruta\n")
            print("-->Veo lastimosa la cara de santana y kevin\n")
            print("-->Me siento y tomo un micro-sueño hasta que llegamos al hermoso CBC\n")
            print("-->Verfico que llegamos al CBC")
            n=input("¿LLegamos al CBC? responda solo con si o no \n")
            if(n=="si"):
                print("-->Me bajo de la ruta \n")
                print("***FIN***")
            else:
                while i<3:
                    print("-->Verfico que llegamos al CBC \n")
                    n=input("¿LLegamos al CBC? responda solo con si o no \n")
                    if(n=="si"):
                        print("-->Me bajo de la ruta \n")
                        print("***FIN***")
                        i=3 
                    else:
                        i=i+1
                        if(i==3):
                            print("-->La ruta se varo, F \n")   
                            print("***FIN***")            
        else:
            while i<3:
                print("-->verifico que la ruta pase \n")
                n=input("¿La ruta paso? responda solo con si o no \n")
                if(n=="si"):
                    print("-->Me monto en la ruta \n")
                    print("-->Veo lastimosa la cara de santana y kevin \n")
                    print("-->Me siento y tomo un micro-sueño hasta que llegamos al hermoso CBC \n")
                    print("-->Verfico que llegamos al CBC \n")
                    n=input("¿LLegamos al CBC? responda solo con si o no \n")
                    if(n=="si"):
                        print("-->Me bajo de la ruta \n")
                        print("***FIN***")
                        i=3
                    else:
                        while i<3:
                            print("-->Verfico que llegamos al CBC \n")
                            n=input("¿LLegamos al CBC? responda solo con si o no \n")
                            if(n=="si"):
                                print("-->Me bajo de la ruta \n")
                                print("***FIN***")
                                i=3 
                            else:
                                i=i+1
                                if(i==3):
                                    print("-->La ruta se varo, F \n")   
                                    print("***FIN***")
                else:
                    i=i+1
                    if(i==3):
                        print("-->Grande CBC, la ruta no paso \n")
                        print("***FIN***")
else:
    print("-->Vuelvo a mimir \n")
    print("***FIN***")