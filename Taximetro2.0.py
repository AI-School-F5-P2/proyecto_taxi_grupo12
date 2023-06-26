

    import time
from datetime import datetime, date
import logging
from pynput import keyboard
import unittest

# Configurar el sistema de logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

class Taximetro:
    def __init__(self):
        self.tiempo_inicio = None
        self.tiempo_carrera = 0
        self.en_movimiento = False
        self.tarifa = 0
        self.tarifa_parada = 0
        self.tiempo_inicio_parada = None
        self.tiempo_total_parada = 0
        self.precio_carrera = 0.05
        self.precio_parada = 0.02
        self.archivo = open("historico.txt", "a")

    def calcular_tarifa(self, tiempo):
        self.tarifa = tiempo * self.precio_carrera
        return self.tarifa

    def calcular_tarifa_parada(self, tiempo):
        self.tarifa_parada += tiempo * self.precio_parada
        return self.tarifa_parada

    def almacena(self):
        tarifa = "%.2f" % self.tarifa
        tiempo_carrera = datetime.utcfromtimestamp(self.tiempo_carrera).strftime('%H:%M:%S')
        tiempo_inicio = datetime.fromtimestamp(self.tiempo_inicio).strftime('%H:%M:%S')
        data = date.today()
        self.archivo.write(str(data) + " Hora Inicial: " + str(tiempo_inicio) + " Tiempo da Carrera: " + str(tiempo_carrera) + " Valor da Carrera: " + str(tarifa) + " Euros\n")
        self.archivo.close()

    def pulsa(self, key):
        if key == keyboard.Key.enter:
            if self.tiempo_inicio is None:
                logging.info("La carrera ha comenzado.")
                self.tiempo_inicio = time.time()
            else:
                tiempo_actual = time.time()
                self.tiempo_carrera = tiempo_actual - self.tiempo_inicio
                self.tarifa = self.calcular_tarifa(self.tiempo_carrera)
                self.tarifa += self.tarifa_parada

                self.almacena()
                logging.info(f"La carrera ha terminado. Total a pagar: {self.tarifa:.2f} Euros.")
                self.tiempo_inicio = None
                self.en_movimiento = False

                logging.info("Esperando instrucciones")
        elif key == keyboard.Key.space:
            if self.tiempo_inicio is not None:
                if self.en_movimiento:
                    tiempo_actual = time.time()
                    tiempo_parada = tiempo_actual - self.tiempo_inicio_parada
                    self.tarifa_parada = self.calcular_tarifa_parada(tiempo_parada)
                    logging.info("El taxi ha continuado en movimiento.")
                else:
                    logging.info("El taxi ha frenado.")
                    self.tiempo_inicio_parada = time.time()
                self.en_movimiento = not self.en_movimiento
        else:
            logging.info("Tecla sin función. Pulsa Intro para Iniciar o Finalizar la carrera. Y Espacio para Frenar o Continuar en una Carrera.")

    def iniciar_taximetro(self):
        logging.info("Bienvenido al programa del taxímetro.")
        logging.info("Este programa simula el cálculo de tarifas de un taxi.")
        logging.info("Instrucciones:")
        logging.info("  - Presiona Enter para comenzar/terminar la carrera.")
        logging.info("  - Presiona Espacio para frenar/continuar en una carrera.")
        logging.info("Esperando instrucciones...")

        with keyboard.Listener(on_press=self.pulsa) as listener:
            listener.join()


# Pruebas con unittest

class TestTaximetro(unittest.TestCase):
    def setUp(self):
        self.taximetro = Taximetro()

    def test_calcular_tarifa(self):
        tiempo = 10
        self.assertEqual(self.taximetro.calcular_tarifa(tiempo), 0.5)

    def test_calcular_tarifa_parada(self):
        tiempo = 5
        self.assertEqual(self.taximetro.calcular_tarifa_parada(tiempo), 0.1)

    def test_almacena(self):
        tiempo_carrera = 100
        tarifa = 5.5
        tiempo_inicio = time.time()
        self.taximetro.tiempo_carrera = tiempo_carrera
        self.taximetro.tarifa = tarifa
        self.taximetro.tiempo_inicio = tiempo_inicio
        self.taximetro.almacena()
        with open("historico.txt", "r") as archivo:
            contenido = archivo.readlines()
            self.assertTrue(contenido[-1].endswith("Euros\n"))


if __name__ == '__main__':
    taximetro = Taximetro()
    taximetro.iniciar_taximetro()
