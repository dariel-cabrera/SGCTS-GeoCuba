from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion= ConexionDB()

    sql= '''
    CREATE TABLE tla(
        id_tla INTERGER,
        ubicacion VARCHAR(100),
        constante_K REAL,
        densidad_mar  REAL,
        densidad_arena REAL ,
        coeficiente_porocidad REAL,
        altura REAL,
        angulo_rompiente REAL,
        indice_rompiente REAL,
        acelaración_gravitacional REAL,
        resultado REAL,  
        PRIMARY KEY(id_sgcts AUTOINCREMENT)
    )
    '''
    conexion.cursor.execute(sql)
    conexion.cerrar()

def borrar_tabla():
    conexion= ConexionDB()

    sql='DROP TABLE tla'
     
    conexion.cursor.execute(sql)
    conexion.cerrar()