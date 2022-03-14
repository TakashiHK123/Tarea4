import sys
import serial
from GUIControlador import *            #Importamos el archivo enviar, es el nombre de la GUI diseñado
from PyQt5.QtWidgets import *
import time

serialArduino = serial.Serial("COM3",9600)
time.sleep(2)
cadenaPosicion="0";
velocidadMostrar="0";
posicionMostrar="0";
voltajeMostrar="0";
corrienteMostrar="0";
I2CbusEco="0";
class VentanaInicio(QWidget):

    def manual(self):
        self.ui.boton_manual.setEnabled(False)
        self.ui.boton_automatico.setEnabled(True)
        self.ui.boton_on.setEnabled(True)
        self.ui.boton_off.setEnabled(True)
        self.ui.label_estado.setText("Manual")


    def botonON(self):
        #Guardamos los datos respectivamente
        self.ui.boton_on.setEnabled(False)
        self.ui.boton_off.setEnabled(True)
        posicion=self.ui.text_posicion.toPlainText()
        kp=self.ui.text_kp.toPlainText()
        ki=self.ui.text_ki.toPlainText()
        kd=self.ui.text_kd.toPlainText()
        #Cargamos los datos en cadena
        cadena  = str(posicion) + ","+ str(kp)+","+ str(ki) +","+ str(kd)
        #Enviamos los datos por Serial con codigo ascii
        serialArduino.write(cadena.encode('ascii'))     #Envia los datos al arduino
        cadena_recibido = serialArduino.readline().decode('ascii')  #El arduino vuelve a reenviar la cadena al python
        cadena_mostrar = cadena_recibido.split(',')
        velocidadMostrar = cadena_mostrar[0]                  # se guarda lo que esta antes de la coma
        posicionMostrar = cadena_mostrar[1]    #se guarda lo que esta luego de la coma
        voltajeMostrar = cadena_mostrar[2]
        corrienteMostrar = cadena_mostrar[3]
        I2CbusEco = cadena_mostrar[4]
        self.ui.label_text.setText(I2CbusEco)
        self.ui.label_velocidad.setText(velocidadMostrar)
        self.ui.label_posicion.setText(posicionMostrar)
        self.ui.label_voltaje.setText(voltajeMostrar)
        self.ui.label_corriente.setText(corrienteMostrar)
        cadenaPosicion="0";
        velocidadMostrar="0";
        posicionMostrar="0";
        voltajeMostrar="0";
        corrienteMostrar="0";
        I2CbusEco="0";
    def botonOFF(self):
        self.ui.boton_off.setEnabled(False)
        self.ui.boton_on.setEnabled(True)
        cadena  = str(0) + ","+ str(0)+","+ str(0) +","+ str(0)
        serialArduino.write(cadena.encode('ascii'))
        cadena_recibido3 = serialArduino.readline().decode('ascii')  #El arduino vuelve a reenviar la cadena al python
        cadena_mostrar2 = cadena_recibido3.split(',')
        velocidadMostrar = cadena_mostrar2[0]                  # se guarda lo que esta antes de la coma
        posicionMostrar = cadena_mostrar2[1]    #se guarda lo que esta luego de la coma
        voltajeMostrar = cadena_mostrar2[2]
        corrienteMostrar = cadena_mostrar2[3]
        I2CbusEco = "0"
        self.ui.label_text.setText(I2CbusEco)
        self.ui.label_velocidad.setText(velocidadMostrar)
        self.ui.label_posicion.setText(posicionMostrar)
        self.ui.label_voltaje.setText(voltajeMostrar)
        self.ui.label_corriente.setText(corrienteMostrar)
        cadenaPosicion="0";
        velocidadMostrar="0";
        posicionMostrar="0";
        voltajeMostrar="0";
        corrienteMostrar="0";
        I2CbusEco="0";

    def automatico(self):
        self.ui.boton_manual.setEnabled(True)
        self.ui.boton_automatico.setEnabled(False)
        self.ui.boton_on.setEnabled(False)
        self.ui.boton_off.setEnabled(False)
        self.ui.label_estado.setText("Automatico")
        cadena_recibido2 = serialArduino.readline().decode('ascii')  #El arduino envia para verificar velocidad, la posicion actual, voltaje, corriente y el ecobudI2C
        cadenaPosicion = cadena_recibido2.split(',')           #separamos la cadena lo que viene entre coma ,
        velocidadMostrar = cadenaPosicion[0]                  # se guarda lo que esta antes de la coma
        posicionMostrar = cadenaPosicion[1]    #se guarda lo que esta luego de la coma
        voltajeMostrar = cadenaPosicion[2]
        corrienteMostrar = cadenaPosicion[3]
        I2CbusEco = cadenaPosicion[4]
        #self.ui.label_14.setText("Eco del I2C")
        #Mostramos los datos recibidos respectivamente
        self.ui.label_text.setText(I2CbusEco)
        self.ui.label_velocidad.setText(velocidadMostrar)
        self.ui.label_posicion.setText(posicionMostrar)
        self.ui.label_voltaje.setText(voltajeMostrar)
        self.ui.label_corriente.setText(corrienteMostrar)
    #Inicializamos el GUI
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui=Ui_VentanaInicio()
        self.ui.setupUi(self)
        self.ui.boton_manual.setEnabled(False)
        self.ui.label_estado.setText("Manual")
        self.ui.boton_off.setEnabled(False)
        #Para poner el estado entre automatico o manual
        self.ui.boton_manual.clicked.connect(self.manual)
        self.ui.boton_automatico.clicked.connect(self.automatico)
        #Para enviar los datos en el caso del estado manual
        self.ui.boton_on.clicked.connect(self.botonON)
        self.ui.boton_off.clicked.connect(self.botonOFF)


if __name__=="__main__":
    mi_aplicacion= QApplication(sys.argv)
    mi_app = VentanaInicio()
    mi_app.show()
    sys.exit(mi_aplicacion.exec_())