# Clase para la interfaz del juego, Buscaminas

import tkinter as tk
from tkinter import messagebox

# Aquí podrías importar tu clase:
from logica import buscaminasLogica

class BuscaminasUI:
    def __init__(self, root):
        # 'root' es la ventana principal que nos pasa Tkinter
        self.root = root
        self.root.title("Buscaminas Python")
        
        # Iniciamos la lógica
        # Creamos el objeto 'cerebro' que manejará los datos internos
        self.logica = buscaminasLogica(filas=8, columnas=8, num_minas=10)
        
        # Lista para guardar los botones visuales y poder modificarlos luego (cambiar color, texto)
        self.botones = []
        
        # Dibujamos el tablero visual
        # Recorremos cada fila (f) y cada columna (c)
        for f in range(self.logica.filas):
            fila_btns = []
            for c in range(self.logica.cols):

                # CREACIÓN DEL BOTÓN
                # command=lambda... : Esto es un truco. Si no usamos 'lambda', todos los botones creerían que son el último botón. 
                # Esto "congela" los valores de f y c para cada botón específico.
                btn = tk.Button(self.root, text=" ", width=4, height=2, command=lambda x=f, y=c: self.clic(x, y))

                # Lo colocamos en la rejilla visual de la ventana
                btn.grid(row=f, column=c)

                # Lo guardamos en nuestra lista temporal
                fila_btns.append(btn)

                # Añadimos la fila completa a nuestra matriz de botones visuales
            self.botones.append(fila_btns)

    def clic(self, f, c):

        # Preguntamos a la lógica qué hay en esa coordenada
        valor = self.logica.obtener_valor(f, c)
        
        # Actuamos según el valor
        if valor == "M":
            # CASO MINA: Cambiamos texto a bomba y fondo rojo
            self.botones[f][c].config(text="💣", bg="red")
            # Mostramos alerta
            messagebox.showerror("Fin del juego", "¡Has pisado una mina!")
            # (Aquí en el futuro podrías añadir código para reiniciar el juego)

        else:
            # CASO SEGURO: Por ahora mostramos un punto y fondo gris
            # state="disabled" hace que el botón ya no se pueda volver a pulsar
            self.botones[f][c].config(text=".", bg="lightgrey", state="disabled")
            # Aquí falta la lógica de mostrar números vecinos

if __name__ == "__main__":
    root = tk.Tk()
    app = BuscaminasUI(root)
    root.mainloop()