import sqlite3
import os

class ConexionDb:
    def __init__(self):
        try:
            self.base_datos = os.path.abspath("C:/Users/Usuario/Desktop/Apps_py/Catalogo_movies_app/Catalogo.py/database/peliculas.db")
            self.conexion = sqlite3.connect(self.base_datos)
            self.cursor = self.conexion.cursor()
        except sqlite3.OperationalError as e:
            print(f"Error al conectar a la base de datos: {e}")
    
    def cerrar(self):
        try:
            self.conexion.commit()
            self.conexion.close()
        except sqlite3.OperationalError as e:
            print(f"Error al cerrar la conexión a la base de datos: {e}")
