from pynput import keyboard

def pulsa(tecla):
 Verificar si la tecla presionada es una tecla específica
    if tecla == keyboard.Key.space:
        print("Espacio presionado")
    elif tecla == keyboard.Key.enter:
       # print("Intro presionado")
    else:
        print("Esta tecla presionada no tiene fuction!!")

 Crear un Listener para escuchar las pulsaciones de teclas
with keyboard.Listener(on_press=pulsa) as escuchador:
    escuchador.join()


import time
from pynput import keyboard

tiempo_inicio = None
en_movimiento = False
tiempo_total = 0

def calcular_tarifa(tiempo, en_movimiento):
    if en_movimiento:
        tarifa = tiempo * 0.05  # 5 céntimos por segundo
    else:
        tarifa = tiempo * 0.02  # 2 céntimos por segundo
    return tarifa
















