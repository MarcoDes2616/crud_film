from .conection_db import conection_db
from tkinter import messagebox


def crear_tabla():
    conexion = conection_db()

    sql = """
        CREATE TABLE peliculas(
            id INTEGER,
            nombre VARCHAR(30),
            duracion VARCHAR(10),
            genero VARCHAR(20),
            PRIMARY KEY(id AUTOINCREMENT)
        )
    """ 
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Crear Registro"
        mensaje = "Se creó la base de datos"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = "Crear Registro"
        mensaje = "La tabla ya está creada"
        messagebox.showwarning(titulo, mensaje)


def borrar_tabla():
    conexion = conection_db()

    sql = "DROP TABLE peliculas"
    

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Eliminar tabla"
        mensaje = "La tabla se eliminó con éxito"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = "Eliminar tabla"
        mensaje = "No se encontró tabla para borrar"
        messagebox.showerror(titulo, mensaje)


class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.id = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
    
    def __str__(self):
        return f'Pelicula [{self.nombre}, {self.duracion}, {self.genero}]'
    

def guardar(pelicula):
    conexion = conection_db()

    sql = f"""INSERT INTO peliculas (nombre, duracion, genero)
        VALUES('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}')"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = "Registro de película"
        mensaje = "La tabla Películas aun no ha sido creada"
        messagebox.showerror(titulo, mensaje)


def getPeliculas():
    conexion = conection_db()
    sql = 'SELECT * FROM peliculas'
    lista = []
    try:
        conexion.cursor.execute(sql)
        lista = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = "Registro de película"
        mensaje = "La tabla Películas aun no ha sido creada"
        messagebox.showwarning(titulo, mensaje)
    
    return lista

def editar(pelicula, id):
    conexion = conection_db()

    sql = f"""UPDATE peliculas
    set nombre = '{pelicula.nombre}', 
    duracion = '{pelicula.duracion}', 
    genero = '{pelicula.genero}'
    WHERE id = {id}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = "Editar película"
        mensaje = "No se ha podido crear este registro"
        messagebox.showerror(titulo, mensaje)

def eliminar(id):
    conexion = conection_db()

    sql = f"DELETE FROM peliculas WHERE id = {id}"

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = "Eliminar película"
        mensaje = "No se ha podido crear este registro"
        messagebox.showerror(titulo, mensaje)