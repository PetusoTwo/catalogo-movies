from conexion_db import ConexionDb
from tkinter.messagebox import *
def crear_tabla():
    conexion = ConexionDb()
    
    sql = ''' 
    CREATE TABLE pelicula(
        id_pelicula INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(100),
        duracion VARCHAR(100), 
        genero VARCHAR(100)
    )
    '''
    # Ejecutar
    conexion.cursor.execute(sql)
    conexion.cerrar()
    
def borrar_tabla():
    conexion = ConexionDb()
    
    sql = 'DROP TABLE pelicula'
    # Ejecutar
    conexion.cursor.execute(sql)
    conexion.cerrar()


class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
    
    def __str__(self):
        return f"Peliculas[{self.nombre}, {self.duracion}, {self.genero}]"

def guardar(pelicula):
    conexion = ConexionDb()
    sql = f'''INSERT INTO pelicula (nombre, duracion, genero)
    VALUES('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero }' )'''
        
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except: 
        pass
def lista():
    conexion = ConexionDb()
    listar_peliculas = []
    sql = 'SELECT * FROM pelicula'
    
    try:
        conexion.cursor.execute(sql)
        listar_peliculas = conexion.cursor.fetchall()  # Corregí la llamada al método
        conexion.cerrar()
    except Exception as e:
        print(f"Error al obtener datos: {e}")
    return listar_peliculas

def editar(pelicula, id_pelicula):
    conexion = ConexionDb()
    
    sql = f'''
    UPDATE pelicula 
    SET nombre= '{pelicula.nombre}', duracion = '{pelicula.duracion}', 
    genero = '{pelicula.genero}'
    WHERE id_pelicula = {id_pelicula}'''
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except Exception as i: 
        showerror(title="Edicion de campo", message=f"No se pudo editar el campo, Detalles: {i}")
        
def eliminar(id_pelicula):
    conexion = ConexionDb()
    sql = f'''
    DELETE FROM pelicula WHERE id_pelicula = {id_pelicula}
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except Exception as k:
        showerror(title="Eliminacion de campo", message=f"No se pudo eliminar el campo, Detalles: {k}")