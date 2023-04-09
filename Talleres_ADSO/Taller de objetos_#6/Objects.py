#Navagadores super-class 
#Superclass - herencia con parametros
class Navegadores:
    
    #Constructor
    def __init__(self,autor,font_family,motorBusqueda,marketPlace):   
        self.autor=autor
        self.font_family=font_family
        self.motorBusqueda=motorBusqueda
        self.marketplace=marketPlace
    
    #METODOS DE UTILIDADES
    def busqueda(self):
        print("Buscando....")
        
    def verificacionConexion(self):
        print("......verifica")
        print(".....Utilidad")
        
    def errorNavegador(self):
        print("File not found")


class standNavigation(Navegadores):
    def subclas(self):
        print("Otra clase mas")

#Instancioas de objetos con init
safari=standNavigation("Pedro pineda","Cursiva","Bin","playStore")
chorme=standNavigation("Andes perez","Roboto","Bin","operaStore")
opera=standNavigation("Manzana quintero","Arial","Bin","operaStore")
eagle=standNavigation("Samuel luque","Roboto","Bin","microsoftStore")



#SALIDAS METODOS

safari.verificacionConexion()
eagle.busqueda()
opera.errorNavegador()



#Salidas
print("Navegadores atributos: ")
print("safari: ", safari.autor,safari.font_family,safari.motorBusqueda,safari.marketplace)
print("chorme: ", chorme.autor,chorme.font_family,chorme.motorBusqueda,chorme.marketplace)
print("opera: ", opera.autor,opera.font_family,opera.motorBusqueda,opera.marketplace)
print("eagle: ", eagle.autor,eagle.font_family,eagle.motorBusqueda,eagle.marketplace)
print("_-------------------------------------------_")


#Clases de herencia sin init
class tor():
    Nombre="onion"
    utilidad="Cebolla"
    autor="Anonimos"
    
    def ultrator(self):
        print("ULTRA TOR SU METODO")
        
    
        
class hijotor(tor):
    Uso="Sub-terraneoweb"
    
    def ultrator(self):
        print("ESOT ES ESPARTA PERO DELO HIJO TOR")


#instancia sin init
objetos2=hijotor()

objetos2.ultrator()

#Herencia sin init
print("Utilidad ", objetos2.Nombre, objetos2.Uso,objetos2.utilidad)




