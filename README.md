# proyecto_taxi_grupo12

 # Taxímetro

Este programa simula el cálculo de tarifas de un taxi. Registra el tiempo de inicio y finalización de una carrera, así como las paradas intermedias. Calcula la tarifa correspondiente en función del tiempo de carrera y el tiempo de parada.

## Requisitos

- Python 3.x
- Librería pynput

## Instalación

1. Asegúrate de tener Python 3.x instalado en tu sistema.
2. Instala la librería pynput ejecutando el siguiente comando:

   pip install pynput
   

## Uso

1. Ejecuta el script `taximetro.py` desde la línea de comandos.
2. Sigue las instrucciones proporcionadas por el programa:
   - Presiona Enter para comenzar o terminar la carrera.
   - Presiona Espacio para frenar o continuar en una carrera.
   - Otras teclas no tienen función asignada.

El programa mostrará información detallada sobre el estado de la carrera, el tiempo transcurrido, y el total a pagar en euros. Utiliza el sistema de logs para mostrar los mensajes.


## Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de hacerlo. Puedes enviar pull requests con mejoras o correcciones de errores.

## Notas adicionales

Este programa utiliza el módulo pynput para gestionar las pulsaciones de teclas.

La tarifa se calcula en base al tiempo de carrera y el tiempo de parada.

La tarifa de carrera es de 0.05 euros por segundo.

La tarifa de parada es de 0.02 euros por segundo. 


##### Importante: Este programa es solo una simulación y no representa un taxímetro funcional real.
