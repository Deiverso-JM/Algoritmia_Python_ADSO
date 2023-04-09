#Abrir ARCHIVO FUNCION
holaArchivo = open('Talleres_ADSO/Archivos/ER.txt', 'a')
#AGREGAR
holaArchivo.write("\nAGREGAMOS COSAS")
#CERRAS
holaArchivo.close()

#Abrir ARCHIVO FUNCION
holaArchivo = open('Talleres_ADSO/Archivos/ER.txt')
#LEER ARCHIVO FUNCION
print(holaArchivo.readlines())
#CERRAR
holaArchivo.close()


#ELIMINACION DIRECTA
import os
#os.remove('Talleres_ADSO/Archivos/ER.txt')

#CON VALIDACION

if os.path.exists('Talleres_ADSO/Archivos/ER.txt'):
    #os.remove('Talleres_ADSO/Archivos/ER.txt')
    print
else:
    print("NO EXISTE")
    
    
#PARA ELIMINAR CARPETAS

os.rmdir(#direcion de la carpeta con sus NOMBRE
        )