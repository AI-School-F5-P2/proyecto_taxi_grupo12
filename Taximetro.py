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
















