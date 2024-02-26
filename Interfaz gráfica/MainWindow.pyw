import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
import ctypes # Nos permite acceder a la función "GetSystemMetrics"
from PyQt5.QtGui import QFont # Nos permite trabajar con fuentes (tipos de letras)
from PyQt5.QtCore import Qt # Para modificar el cursor

# Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
    # Método constructor de la clase
    def __init__(self):
        # Inicial el objeto QMainWindow
        QMainWindow.__init__(self)
        # Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("MainWindow.ui",self) # El self es para asignárselo al objeto
        self.setWindowTitle("Cambiando el título de la ventana")
        # Mostrar la ventana maximizada
        self.showMaximized()
        # Fijar el tamaño de la ventana (anula lo de la ventana maximizada)
        # Fijar el tamaño mínimo
        self.setMinimumSize(500,500)
        self.setMaximumSize(500,500)
        # Mover la ventana y centrarla en el escritorio
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)
        left = (resolucion_ancho/2)-(self.frameSize().width()/2)
        top = (resolucion_alto/2)-(self.frameSize().height()/2)
        self.move(left,top)
        # Desactivar la ventana
        #self.setEnabled(False)
        # Asignar un tipo de fuente
        qfont = QFont("Arial",12,QFont.Bold)
        self.setFont(qfont)
        # Asignar un tipo de cursor
        self.setCursor(Qt.SizeAllCursor)
        # Asignar estilos CSS
        #self.setStyleSheet("background-color: #000; color:#fff;")
        self.boton.setStyleSheet("Background-color: #000;color: #fff; font-size: 14px;")

    def showEvent(self,event):
        self.bienvenido.setText("¡¡¡Bienvenido!!!")

    def closeEvent(self,event): # Fue necesario importar QMessageBox
        resultado = QMessageBox.question(self,"Salir ...","¿Seguro que quieres salir de la aplicación?",\
                                         QMessageBox.Yes|QMessageBox.No)
        if resultado == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def moveEvent(self,event):  # Para cuando movamos la ventana
        x = str(event.pos().x())
        y = str(event.pos().y())
        self.posicion.setText("x: "+x+"y: "+y)
        
        
             
# Instancia para iniciar una aplicación
app = QApplication(sys.argv) # A cada aplicación que vayamos a crear hay que pasarle sys.argv
# Crear un objeto de la clase
_ventana = Ventana()
# Mostrar la ventana
_ventana.show()
# Ejecutar la aplicación
app.exec()
