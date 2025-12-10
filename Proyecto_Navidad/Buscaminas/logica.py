# Clase para la Lógica del juego, Buscaminas.
"""
"self" es a forma en que el código se refiere a "sí mismo", a SU propia información.

La Clase (class BuscaminasLogica) es el plano de una casa. Es solo papel, no se puede vivir ahí.
El Objeto es la casa construida a partir de ese plano.
self es cuando estás dentro de la casa y dices: "Voy a pintar MI pared" (self.pared) o "Voy a abrir MI puerta" (self.abrir_puerta()).
"""

# Importamos la librería para generar números aleatorios (para las minas)
import random

class buscaminasLogica:
    def __init__(self, filas=8, columnas=8, num_minas=10):
        # Guardamos en 'self' las configuraciones para usarlas en cualquier método de la clase
        self.filas = filas
        self.cols = columnas
        self.num_minas = num_minas

        # self.tablero será nuestra lista de listas (la matriz)
        self.tablero = [] # Aquí guardaremos los valores (0=vacío, 1=mina)

        # Llamamos automáticamente a la función que prepara el juego al iniciar
        self.generar_tablero()

    def generar_tablero(self):
        # Crear matriz vacía llena de ceros
        # Usamos dos bucles 'for' comprimidos: crea filas llenas de 0 y repite eso 'filas' veces.
        self.tablero = [[0 for _ in range(self.cols)] for _ in range(self.filas)]
        
        # Colocar minas aleatoriamente
        minas_colocadas = 0
        while minas_colocadas < self.num_minas:
            f = random.randint(0, self.filas - 1)
            c = random.randint(0, self.cols - 1)
            
            # Verificamos: Si NO hay una mina ("M") ahí todavía...
            if self.tablero[f][c] != "M":
                self.tablero[f][c] = "M"
                minas_colocadas += 1

    def obtener_valor(self, f, c):
        """Método puente: La interfaz gráfica usará esto para preguntar:
        '¿Qué hay en la fila F y columna C?'
        """
        return self.tablero[f][c]
    
    # Más adelante aquí harás una función para contar minas vecinas