import tkinter as tk


#Barra de Menu Archivo Inicio Funcionalidades MiPerfil
def barra_menu(root):
    barra_menu=tk.Menu(root)
    root.config(menu= barra_menu,width=300,height=300)

    #Para que no haga espacio inecesario se agg tearoff
    #menu_inicio= tk.Menu(barra_menu,tearoff = 0)
    #barra_menu.add_cascade(Label ='Archivo',menu = menu_inicio)

    #menu_inicio.add_command(Label = 'Crear Registro en BD')
    #menu_inicio.add_command(Label = 'Eliminar Registro en BD')
    #menu_inicio.add_command(Label = 'Salir',command= root.desctroy)

    #barra_menu.add_cascade(Label ='Inicio')
    #barra_menu.add_cascade(Label ='Funcionalidades')
    #barra_menu.add_cascade(Label ='MiPerfil')


# Frame es un contenedor de los elementos que vamos a crear 
class Frame(tk.Frame):
    
    
    #Constructor
    def __init__ (self,root=None):
        # Heredando constructor dela clase Padre 
        super().__init__(root,width=800,height=500 )
        
        self.root=root
        self.pack()

        # Para Conf el ancho y la altura  bg es fondo de la ventana
        self.config(bg='blue')
        
        self.campo_variables()
    
    
    # Campos de variables
    def campo_variables(self):
        # Label de cada campo
        #Label Cálculo de Variación de Costa
        self.label_nombre= tk.Label(self,text= 'Cálculo de Variación de Costa ')
        # Config la letra 
        self.label_nombre.config(font= ('Arial',18,'bold'),bg='light blue')
        # Posicion de los Label
        # para separar un los label se usa padx y pady
        self.label_nombre.grid(row=0,column=0, padx=10,pady=10,columnspan= 5)
        
        # Densidad del mar
        self.label_nombre= tk.Label(self,text= 'Densidad del mar (ρ) : ')
        # Config la letra 
        self.label_nombre.config(font= ('Arial',12,'bold'),bg='blue')
        # Posicion de los Label
        # para separar un los label se usa padx y pady
        self.label_nombre.grid(row=1,column=0, padx=10,pady=10)
    
        # Label Densidad de la arena 
        self.label_nombre= tk.Label(self,text= 'Densidad de la arena (ρs) : ')
        # Config la letra 
        self.label_nombre.config(font= ('Arial',12,'bold'),bg='blue')
        # Posicion de los Label
        # para separar un los label se usa padx y pady
        self.label_nombre.grid(row=2,column=0, padx=10,pady=10)

        # Label Coeficiente de Porocidad
        self.label_nombre= tk.Label(self,text= 'Coeficiente de Porocidad (n) : ')
        # Config la letra 
        self.label_nombre.config(font= ('Arial',12,'bold'),bg='blue')
        # Posicion de los Label
        # para separar un los label se usa padx y pady
        self.label_nombre.grid(row=3,column=0, padx=10,pady=10)


        # Label de Altura
        self.label_nombre= tk.Label(self,text= 'Altura  (Hb) : ')
        # Config la letra 
        self.label_nombre.config(font= ('Arial',12,'bold'),bg='blue')
        # Posicion de los Label
        # para separar un los label se usa padx y pady
        self.label_nombre.grid(row=4,column=0, padx=10,pady=10)

        # Label Ángulo de Rompiente
        self.label_nombre= tk.Label(self,text= 'Ángulo de Rompiente (α) : ')
        # Config la letra 
        self.label_nombre.config(font= ('Arial',12,'bold'),bg='blue')
        # Posicion de los Label
        # para separar un los label se usa padx y pady
        self.label_nombre.grid(row=1,column=3, padx=10,pady=10)

         # Label Índice de Rompiente
        self.label_nombre= tk.Label(self,text= 'Índice de Rompiente (k) : ')
        # Config la letra 
        self.label_nombre.config(font= ('Arial',12,'bold'),bg='blue')
        # Posicion de los Label
        # para separar un los label se usa padx y pady
        self.label_nombre.grid(row=2,column=3, padx=10,pady=10)

         # Label Acelaración Gravitacional
        self.label_nombre= tk.Label(self,text= 'Acelaración Gravitacional (g) : ')
        # Config la letra 
        self.label_nombre.config(font= ('Arial',12,'bold'),bg='blue')
        # Posicion de los Label
        # para separar un los label se usa padx y pady
        self.label_nombre.grid(row=3,column=3, padx=10,pady=10)

        # Entrys de cada campo
        # Entrys Densidad_Mar
        self.densidad_mar= tk.StringVar()
        self.entry_densidad_mar= tk.Entry(self,textvariable= self.densidad_mar)
        self.entry_densidad_mar.config(width=10, font=('Arial',12))
        self.entry_densidad_mar.grid(row=1, column=1,padx=10,pady=10,columnspan= 2)

         # Entrys Densidad_Arena
        self.densidad_arena= tk.StringVar()
        self.entry_densidad_arena= tk.Entry(self,textvariable= self.densidad_arena)
        self.entry_densidad_arena.config(width=10, font=('Arial',12))
        self.entry_densidad_arena.grid(row=2, column=1,padx=10,pady=10,columnspan= 2)

        # Entrys coeficiente_porocidad
        self.coeficiente_porocidad= tk.StringVar()
        self.entry_coeficiente_porocidad= tk.Entry(self,textvariable= self.coeficiente_porocidad)
        self.entry_coeficiente_porocidad.config(width=10, font=('Arial',12))
        self.entry_coeficiente_porocidad.grid(row=3, column=1,padx=10,pady=10,columnspan= 2)

         # Entrys Altura
        self.altura= tk.StringVar()
        self.entry_altura= tk.Entry(self,textvariable= self.altura)
        self.entry_altura.config(width=10, font=('Arial',12))
        self.entry_altura.grid(row=4, column=1,padx=10,pady=10,columnspan= 2)

        # Entrys angulo_rompiente
        self.angulo_rompiente= tk.StringVar()
        self.entry_angulo_rompiente= tk.Entry(self,textvariable= self.angulo_rompiente)
        self.entry_angulo_rompiente.config(width=10, font=('Arial',12))
        self.entry_angulo_rompiente.grid(row=1, column=4,padx=10,pady=10,columnspan= 2)

         # Entrys indice_rompiente
        self.indice_rompiente= tk.StringVar()
        self.entry_indice_rompiente= tk.Entry(self,textvariable= self.indice_rompiente)
        self.entry_indice_rompiente.config(width=10, font=('Arial',12))
        self.entry_indice_rompiente.grid(row=2, column=4,padx=10,pady=10,columnspan= 2)

        # Entrys acelaración_gravitacional
        self.acelaración_gravitacional= tk.StringVar()
        self.entry_acelaración_gravitacional= tk.Entry(self,textvariable= self.acelaración_gravitacional)
        self.entry_acelaración_gravitacional.config(width=10, font=('Arial',12))
        self.entry_acelaración_gravitacional.grid(row=3, column=4,padx=10,pady=10,columnspan= 2)


        

