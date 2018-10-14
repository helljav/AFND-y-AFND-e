#python 2.7.6
from Automata_FND import Automata
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui

# Clase Ventana que hereda de QtGui.QMainWindow
class Ventana (QtGui.QMainWindow):
	# Constructor de la Ventana
    def __init__(self):
        # Se ejecuta el Constructor de la clase Padre
        super(Ventana, self).__init__()
        self.setGeometry(400,50,600,650)
        # Se agrega un titulo al Grafico
        self.setWindowTitle("Implementacion de un AFND y AFND-e")
        # Se Agrega un Icono al Grafico
        self.setWindowIcon(QtGui.QIcon('logoturing.jpg'))
        

        # Se agrega un evento Se agrega un atajo, debe ir junto la cadena
        EventoSalir = QtGui.QAction(QtGui.QIcon("salir.png"),"salir",self)         
        EventoSalir.setShortcut("Ctrl+Q")
        EventoSalir.setStatusTip('Sali de la aplicacion')
        EventoSalir.triggered.connect(self.cierra_aplicacion)

        # Menu
        MenuPrincipal = self.menuBar()
        MenuArchivo = MenuPrincipal.addMenu('&Inicio')

         # Se agrega un listener o escuchador de evento, recibe el evento "EventoSalir"
        MenuArchivo.addAction(EventoSalir)

        # Se crea el contenifo del Grafico
        self.elem()


    def elem(self):
        # Configuracion de el Contenido
        # Declaracion de componentes
        self.combobox = QtGui.QComboBox(self)#Combobox
        self.titulo_lbl = QtGui.QLabel('Automata Finito No Determinista-AFND',self)
        self.Sigma_lbl = QtGui.QLabel('Lenguaje Sigma = {1,0}',self)
        self.prop_lbl = QtGui.QLabel('Proporcione la cadena a evaluar',self)
        self.ev_lbl = QtGui.QLabel('Seleccione el tipo de automata',self)
        self.pantalla = QtGui.QLabel(self)
        self.button = QtGui.QPushButton('Comenzar',self)
        self.entrada_texto = QtGui.QLineEdit(self)      
        self.salida_texto  = QtGui.QLineEdit(self)
        
        
        self.titulo_lbl.resize(400,30)
        self.titulo_lbl.move(120,40)
        self.titulo_lbl.setFont(QtGui.QFont('Arial',16))

        self.Sigma_lbl.resize(300,30)
        self.Sigma_lbl.move(30,315)

        self.prop_lbl.resize(300,30)
        self.prop_lbl.move(30,340)

        

        self.entrada_texto.resize(300,20)
        self.entrada_texto.move(230,345)

        self.button.resize(150,40)
        self.button.move(30,430)
        self.button.clicked.connect(self.evalua)

        self.ev_lbl.resize(300,30)
        self.ev_lbl.move(40,390)

        self.pantalla.setPixmap(QtGui.QPixmap("logoturing.jpg"))
        self.pantalla.resize(600,255)
        self.pantalla.move(10,70)

        self.salida_texto.setGeometry(230,410,350,300)

        self.combobox.resize(360, 30)
        self.combobox.move(230,378)
        #Agregamos los items (son como las opciones a desplegar)
        self.combobox.addItem('--------------------------------')
        self.combobox.addItem('Automata Finito no Determinista')
        self.combobox.addItem('Automata Finito no Determinista-e')
        #evento del combobox para poder cambiar las imagenes en el label, llama al metodo imagen
        self.combobox.currentIndexChanged.connect(self.imagen)
        # Hace Visible el Grafico
        self.show()

    def cierra_aplicacion(self):
        sys.exit()


    #Metodo que ejecuta el boton
    def evalua(self):
        contador = 0
        mensaje = self.entrada_texto.text()
        #Recorre la cadena del mensaje y verifica si hay puros ceros y unos, de caso contarario aumenta un contador a uno
        for m in mensaje:
            if m!="0" and m!="1":
                contador = contador+1
        #Si no son cadenas de 1 y 0 manda un error y ya no hace nada
        if(contador>0 or mensaje==""):
            QtGui.QMessageBox.critical( self , "Error", "Cadena Invalida o vacia")
            self.entrada_texto.setText("")
            contador =0
        elif(self.combobox.currentIndex()==0):
            QtGui.QMessageBox.critical( self , "Error", "Seleccione un Automata")
            self.entrada_texto.setText("")
            contador =0
        else:
            estados = []
            auto = Automata()
            evaluacion = auto.q0(mensaje,contador,estados)
            if(evaluacion==0):
                self.salida_texto.setText("La cadena es aceptada")
            elif(evaluacion==1):
                self.salida_texto.setText("La cadena no es aceptada")

    #Metodo para el combobox
    def imagen(self):
        #agarra el indice de la opcion como un arreglo (primera opcion = 0, segunda =1, tercera =2, .....)
        tipoimg = self.combobox.currentIndex()
        #hacemos el cambio de imagen
        if(tipoimg==0):
            self.pantalla.setPixmap(QtGui.QPixmap("logoturing.jpg"))
        if(tipoimg==1):
            self.pantalla.setPixmap(QtGui.QPixmap("AFND.jpg"))
            self.titulo_lbl.setText("Automata Finito No Determinista-AFND")
        if(tipoimg==2):
            self.pantalla.setPixmap(QtGui.QPixmap("AFND-e.jpg"))
            self.titulo_lbl.setText("Automata Finito No Determinista-E-AFND-E")
            
            
#Metodo main que correr la aplicacion es como si fuera otra clase 
def main():    
    app = QtGui.QApplication(sys.argv)
    GUI = Ventana()
    sys.exit(app.exec_())

# Se corre el main
main()


