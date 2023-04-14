import pyautogui
import tkinter as tk
import threading
import time

# Función para enviar mensajes
def enviar_mensajes(texto, intervalo, duracion):
    # Darle tiempo al usuario para cambiar a la ventana de chat
    time.sleep(5)

    # Enviar mensajes mientras el tiempo de duración no haya expirado
    tiempo_inicio = time.time()
    while (time.time() - tiempo_inicio) < duracion:
        pyautogui.typewrite(texto)
        pyautogui.press("enter")
        time.sleep(intervalo)
    
    # Mostrar mensaje de finalización
    mensaje_finalizacion = f"Finalizado después de {duracion} segundos."
    mensaje.config(text=mensaje_finalizacion)
    
    # Habilitar el botón "Iniciar" después de completar o cancelar el envío de mensajes
    boton_iniciar.config(state="normal")

# Función para manejar el botón "Iniciar"
def iniciar():
    # Obtener los valores de los campos de entrada
    texto = entrada_texto.get()
    intervalo = float(entrada_intervalo.get())
    duracion = int(entrada_duracion.get())

    # Desactivar el botón "Iniciar"
    boton_iniciar.config(state="disabled")

    # Iniciar el hilo de envío de mensajes
    t = threading.Thread(target=enviar_mensajes, args=(texto, intervalo, duracion))
    t.start()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mandador de mensajes")

# Crear los widgets de la interfaz
texto_etiqueta = tk.Label(ventana, text="Mensaje:")
entrada_texto = tk.Entry(ventana)
intervalo_etiqueta = tk.Label(ventana, text="Intervalo (segundos):")
entrada_intervalo = tk.Entry(ventana)
duracion_etiqueta = tk.Label(ventana, text="Duración (segundos):")
entrada_duracion = tk.Entry(ventana)
boton_iniciar = tk.Button(ventana, text="Iniciar", command=iniciar)
mensaje = tk.Label(ventana, text="Presione 'Iniciar' para comenzar.")

# Añadir los widgets a la ventana
texto_etiqueta.pack()
entrada_texto.pack()
intervalo_etiqueta.pack()
entrada_intervalo.pack()
duracion_etiqueta.pack()
entrada_duracion.pack()
boton_iniciar.pack()
mensaje.pack()

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
