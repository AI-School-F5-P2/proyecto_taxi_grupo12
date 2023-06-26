import time
from datetime import datetime
from datetime import date
import logging
from pynput import keyboard
import unittest

# Configurar el sistema de logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

# tiempo inicial da carrera
tiempo_inicio = None
# tiempo total carrera
tiempo_carrera = 0
en_movimiento = False
tarifa = 0
tarifa_parada = 0
# tiempo inicial da parada
tiempo_inicio_parada = None
# tiempo total da parada
tiempo_total_parada = 0
tecla = None
precio_carrera = 0.05
precio_parada = 0.02
archivo = open("historico.txt", "a")


# calcula tafifa en movimiento
def calcular_tarifa(tiempo):
    global tarifa

    tarifa = (tiempo * precio_carrera)

    return tarifa


# Calcula tafifa de las paradas
def calcular_tarifa_parada(tiempo):
    global tarifa_parada

    tarifa_parada = tarifa_parada + (tiempo * precio_parada)

    return tarifa_parada


# archivar datos de la carrera
def almacena(tiempo_carrera, tarifa, tiempo_inicio):
    global archivo

    tarifa = "%.2f" % tarifa
    tiempo_carrera = datetime.utcfromtimestamp(tiempo_carrera).strftime('%H:%M:%S')
    tiempo_inicio = datetime.fromtimestamp(tiempo_inicio).strftime('%H:%M:%S')
    data = date.today()
    archivo = open("historico.txt", "a")
    archivo.write(str(data))
    archivo.write(" ")
    archivo.write("Hora Inicial: ")
    archivo.write(str(tiempo_inicio))
    archivo.write(" ")
    archivo.write("Tiempo da Carrera: ")
    archivo.write(str(tiempo_carrera))
    archivo.write(" ")
    archivo.write("Valor da Carrera: ")
    archivo.write(str(tarifa))
    archivo.write(" ")
    archivo.write("Euros")
    archivo.write("\n")
    archivo.close()


# Calcula o valor total da tafifa da carrera
def Pulsa(key):
    global tiempo_inicio, en_movimiento, tiempo_total, tiempo_inicio_parada, tiempo_total_parada, tarifa, tarifa_parada
    if key == keyboard.Key.enter:  # Presionar Enter para comenzar/terminar la carrera
        if tiempo_inicio is None:  # Comenzar la carrera
            logging.info("La carrera ha comenzado.")
            tiempo_inicio = time.time()

        else:  # Terminar la carrera
            tiempo_actual = time.time()
            tiempo_carrera = tiempo_actual - tiempo_inicio
            tarifa = calcular_tarifa(tiempo_carrera)
            tarifa = tarifa + tarifa_parada

            almacena(tiempo_carrera, tarifa, tiempo_inicio)
            logging.info(f"La carrera ha terminado. Total a pagar: {tarifa:.2f} Euros.")
            tiempo_inicio = None
            en_movimiento = False

            logging.info("Esperando instrucciones")
    elif key == keyboard.Key.space:  # Presionar Espacio para frenar/continuar en una carrera
        if tiempo_inicio is not None:  # Solo aplicable si la carrera está en curso
            if en_movimiento:
                # Terminar la Parada
                tiempo_actual = time.time()
                tiempo_parada = tiempo_actual - tiempo_inicio_parada
                tarifa_parada = calcular_tarifa_parada(tiempo_parada)
                logging.info("El taxi ha continuado en movimiento.")
            else:
                # Inicia la Parada
                logging.info("El taxi ha frenado.")
                tiempo_inicio_parada = time.time()
            en_movimiento = not en_movimiento
    else:  # tecla sin función
        logging.info("Tecla sin funcion. Pulse Intro para Iniciar o Finalizar la carrera. Y Espacio para Frenar o Continuar en una Carrera.")


def main():



    logging.info("Bienvenido al programa del taxímetro.")
    logging.info("Este programa simula el cálculo de tarifas de un taxi.")
    logging.info("Instrucciones:")
    logging.info("  - Presiona Enter para comenzar/terminar la carrera.")
    logging.info("  - Presiona Espacio para frenar/continuar en una carrera.")
    logging.info("Esperando instrucciones...")

    with keyboard.Listener(on_press=Pulsa) as listener:
        listener.join()


# Pruebas con unittest

class TestTaximetro(unittest.TestCase):

    def test_calcular_tarifa(self):
        tiempo = 10
        self.assertEqual(calcular_tarifa(tiempo), 0.5)

    def test_calcular_tarifa_parada(self):
        tiempo = 5
        self.assertEqual(calcular_tarifa_parada(tiempo), 0.1)

    def test_almacena(self):
        tiempo_carrera = 100
        tarifa = 5.5
        tiempo_inicio = time.time()
        almacena(tiempo_carrera, tarifa, tiempo_inicio)
        with open("historico.txt", "r") as archivo:
            contenido = archivo.readlines()
            self.assertTrue(contenido[-1].endswith("Euros\n"))


if __name__ == '__main__':
  main()

    