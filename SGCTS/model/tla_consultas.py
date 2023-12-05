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
   #Para evitar que por consola me mande un error cuando ya la tabla ya esta creada se usa try 
    try: 
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo="Crear Registro"
        mensaje= "Se creo la tabla en la base de datos"
        messagebox.showinfo(titulo,mensaje)
    except:
        titulo="Crear Registro"
        mensaje= "La tabla ya esta creada" 
        messagebox.showerror(titulo,mensaje)
def borrar_tabla():
    conexion= ConexionDB()

    sql='DROP TABLE tla'
    try: 
        conexion.cursor.execute(sql)
        conexion.cerrar()

        titulo= 'Borrar Registro'
        mensaje= 'La tabla de la Base de Datos se borro con exito'
        messagebox.showinfo(titulo,mensaje)
    except:
        titulo= 'Borrar Registro'
        mensaje= 'No hay tabla para borrar'
        messagebox.showerror(titulo,mensaje)

class tla:
    
    def init (self,ubicacion,constante_K,densidad_mar,densidad_arena,coeficiente_porocidad,altura,angulo_rompiente,indice_rompiente,acelaración_gravitacional,resultado):
        self.id_tla= None
        self.ubicacion= ubicacion
        self.constante_K= constante_K
        self.densidad_mar= densidad_mar
        self.densidad_arena= densidad_arena
        self.coeficiente_porocidad= coeficiente_porocidad
        self.altura= altura
        self.angulo_rompiente= angulo_rompiente
        self.indice_rompiente= indice_rompiente
        self.acelaración_gravitacional= acelaración_gravitacional
        self.resultado= resultado
    
    def str (self):
        return f'tla[{self.ubicacion},{self.constante_K},{self.densidad_mar},{self.densidad_arena},{self.coeficiente_porocidad},{self.altura},{self.angulo_rompiente},{self.indice_rompiente},{self.acelaración_gravitacional},{self.resultado}]'