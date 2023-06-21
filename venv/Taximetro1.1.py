
import time
from pynput import keyboard
# tiempo inicial da carrera
tiempo_inicio = None
# tiempo total carrera
tiempo_total = 0
en_movimiento = False
tarifa = 0
tarifa_parada = 0
# tiempo inicial da parada
tiempo_inicio_parada = None
# tiempo total da parada
tiempo_total_parada = 0
tecla = None


def calcular_tarifa(tiempo):
    global tarifa
    
    tarifa = (tiempo * 0.05)  # 5 céntimos por segundo
    
    return tarifa

def calcular_tarifa_parada(tiempo):
    global tarifa_parada

    tarifa_parada = tarifa_parada + (tiempo * 0.02)  # 2 céntimos por segundo

    return tarifa_parada

def Pulsa(key):
    global tiempo_inicio, en_movimiento, tiempo_total, tiempo_inicio_parada, tiempo_total_parada, tarifa, tarifa_parada
    if key == keyboard.Key.enter:  # Presionar Enter para comenzar/terminar la carrera
        if tiempo_inicio is None:  # Comenzar la carrera
            print("La carrera ha comenzado.")
            tiempo_inicio = time.time()

        else:  # Terminar la carrera
            tiempo_actual = time.time()
            tiempo_carrera = tiempo_actual - tiempo_inicio
            tarifa = calcular_tarifa(tiempo_carrera)
            tarifa = tarifa + tarifa_parada
            #tiempo_total += tiempo_carrera
            print(f"La carrera ha terminado. Total a pagar: {tarifa:.2f} Euros.")
            tiempo_inicio = None
            en_movimiento = False
            print("Esperando instrucciones")
    elif key == keyboard.Key.space:  # Presionar Espacio para frenar/continuar en una carrera
        if tiempo_inicio is not None:  # Solo aplicable si la carrera está en curso
            if en_movimiento:
                # Terminar la Parada
                tiempo_actual = time.time()
                tiempo_parada = tiempo_actual - tiempo_inicio_parada
                tarifa_parada = calcular_tarifa_parada (tiempo_parada)
                print("El taxi ha continuado en movimiento.")
            else:
                 print("El taxi ha frenado.")
                 tiempo_inicio_parada = time.time() 
            en_movimiento = not en_movimiento
    else: # para tecla sin funcion
        print("Tecla sin funcion. Pulse Intro para Iniciar o Finalizar la carrera. Y Espacio para Frenar o Continuar en una Carrera.")
   
def main():
    print("Bienvenido al programa del taxímetro.")
    print("Este programa simula el cálculo de tarifas de un taxi.")
    print("Instrucciones:")
    print("  - Presiona Enter para comenzar/terminar la carrera.")
    print("  - Presiona Espacio para frenar/continuar en una carrera.")
    print("Esperando instrucciones...")

    with keyboard.Listener(on_press=Pulsa) as listener:
        listener.join()


main()



