    from pynput import keyboard

def pulsa(tecla):
# Verificar si la tecla presionada es una tecla específica
    if tecla == keyboard.Key.space:
        print("Espacio presionado")
    elif tecla == keyboard.Key.enter:
        print("Intro presionado")
    else:
        print("Esta tecla presionada no tiene fuction!!")

# Crear un Listener para escuchar las pulsaciones de teclas
with keyboard.Listener(on_press=pulsa) as escuchador:
    escuchador.join()




