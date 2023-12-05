import sqlite3

class ConexionDB:
    def __init__(self):
        #Si no existe el archivo db el lo busca. Si no existe lo crea sino se conecta
        self.base_datos='database/tla.db'
        self.conexion= sqlite3.connect(self.base_datos)
        self.cursor= self.conexion.cursor()
    
    def cerrar(self): 
        self.conexion.commit()
        self.conexion.close()