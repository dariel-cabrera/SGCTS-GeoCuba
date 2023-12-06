import tkinter as tk
from tkinter  import ttk
from model.tla_consultas import crear_tabla, borrar_tabla
from model.tla_consultas import tla

#Barra de Menu Archivo Inicio Funcionalidades MiPerfil
def barra_menu(root):
    barra_menu=tk.Menu(root)
    root.config(menu=barra_menu,width=300,height=300)

    #Para que no haga espacio inecesario se agg tearoff
    #menu_inicio= tk.Menu(barra_menu)
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
        self.config(bg='#004a74')
        
        self.campo_variables()
        self.desabilitar_campos()
        self.tabla_listado_calculos()
        
    
    
    # Campos de variables
    def campo_variables(self):
        # Label de cada campo
        #Label Cálculo de Variación de Costa
        self.label_calculo_variacion= tk.Label(self,text= 'Cálculo de Variación de Costa ')
        # Config la letra 
        self.label_calculo_variacion.config(font= ('Arial',18,'bold'),bg='#02d3e4')
        # Posicion de los Label
        # para separar un los label se usa padx y pady
        self.label_calculo_variacion.grid(row=0,column=0, padx=10,pady=10,columnspan= 5)
        
        # Densidad del mar
        self.label_constante_K= tk.Label(self,text= 'Densidad del mar (ρ) : ')
        # Config la letra 
        self.label_constante_K.config(font= ('Arial',12,'bold'),bg='#0299e4')
        # Posicion de los Label
        # para separar un los label se usa padx y pady
        self.label_constante_K.grid(row=1,column=0, padx=10,pady=10)
    
        # Label Densidad de la arena 
        self.label_densidad_arena= tk.Label(self,text= 'Densidad de la arena (ρs) : ')
        # Config la letra 
        self.label_densidad_arena.config(font= ('Arial',12,'bold'),bg='#0299e4')
        # Posicion de los Label
        # para separar un los label se usa padx y pady
        self.label_densidad_arena.grid(row=2,column=0, padx=10,pady=10)

        # Label Coeficiente de Porocidad
        self.label_coeficiente_porocidad= tk.Label(self,text= 'Coeficiente de Porocidad (n) : ')
        # Config la letra 
        self.label_coeficiente_porocidad.config(font= ('Arial',12,'bold'),bg='#0299e4')
        # Posicion de los Label
        # para separar un los label se usa padx y pady
        self.label_coeficiente_porocidad.grid(row=3,column=0, padx=10,pady=10)


        # Label de Altura
        self.label_altura= tk.Label(self,text= 'Altura  (Hb) : ')
        # Config la letra 
        self.label_altura.config(font= ('Arial',12,'bold'),bg='#0299e4')
        # Posicion de los Label
        # para separar un los label se usa padx y pady
        self.label_altura.grid(row=4,column=0, padx=10,pady=10)

        # Constante K
        self.label_constante_K= tk.Label(self,text= 'Constante (K) : ')
        # Config la letra 
        self.label_constante_K.config(font= ('Arial',12,'bold'),bg='#0299e4')
        # Posicion de los Label
        # para separar un los label se usa padx y pady
        self.label_constante_K.grid(row=5,column=0, padx=10,pady=10)

        # Label Ángulo de Rompiente
        self.label_angulo= tk.Label(self,text= 'Ángulo de Rompiente (α) : ')
        # Config la letra 
        self.label_angulo.config(font= ('Arial',12,'bold'),bg='#0299e4')
        # Posicion de los Label
        # para separar un los label se usa padx y pady
        self.label_angulo.grid(row=1,column=2, padx=10,pady=10)

         # Label Índice de Rompiente
        self.label_indice= tk.Label(self,text= 'Índice de Rompiente (k) : ')
        # Config la letra 
        self.label_indice.config(font= ('Arial',12,'bold'),bg='#0299e4')
        # Posicion de los Label
        # para separar un los label se usa padx y pady
        self.label_indice.grid(row=2,column=2, padx=10,pady=10)

         # Label Acelaración Gravitacional
        self.label_aceleracion= tk.Label(self,text= 'Acelaración Gravitacional (g) : ')
        # Config la letra 
        self.label_aceleracion.config(font= ('Arial',12,'bold'),bg='#0299e4')
        # Posicion de los Label
        # para separar un los label se usa padx y pady
        self.label_aceleracion.grid(row=3,column=2, padx=10,pady=10)

        # Label Ubicacion
        self.label_ubicacion= tk.Label(self,text= 'Ubicacion  : ')
        # Config la letra 
        self.label_ubicacion.config(font= ('Arial',12,'bold'),bg='#0299e4')
        # Posicion de los Label
        # para separar un los label se usa padx y pady
        self.label_ubicacion.grid(row=4,column=2, padx=10,pady=10)

        # Entrys de cada campo
        # Entrys Densidad_Mar
        self.mi_densidad_mar= tk.StringVar()
        self.entry_densidad_mar= tk.Entry(self,textvariable= self.mi_densidad_mar)
        self.entry_densidad_mar.config(width=20, font=('Arial',12))
        self.entry_densidad_mar.grid(row=1, column=1,padx=10,pady=10)

         # Entrys Densidad_Arena
        self.mi_densidad_arena= tk.StringVar()
        self.entry_densidad_arena= tk.Entry(self,textvariable= self.mi_densidad_arena)
        self.entry_densidad_arena.config(width=20, font=('Arial',12))
        self.entry_densidad_arena.grid(row=2, column=1,padx=10,pady=10)

        # Entrys coeficiente_porocidad
        self.mi_coeficiente_porocidad= tk.StringVar()
        self.entry_coeficiente_porocidad= tk.Entry(self,textvariable= self.mi_coeficiente_porocidad)
        self.entry_coeficiente_porocidad.config(width=20, font=('Arial',12))
        self.entry_coeficiente_porocidad.grid(row=3, column=1,padx=10,pady=10)

         # Entrys Altura
        self.mi_altura= tk.StringVar()
        self.entry_altura= tk.Entry(self,textvariable= self.mi_altura)
        self.entry_altura.config(width=20, font=('Arial',12))
        self.entry_altura.grid(row=4, column=1,padx=10,pady=10)

         # Entrys Constante K
        self.mi_constante_K= tk.StringVar()
        self.entry_constante_K= tk.Entry(self,textvariable= self.mi_constante_K)
        self.entry_constante_K.config(width=20, font=('Arial',12))
        self.entry_constante_K.grid(row=5, column=1,padx=10,pady=10)

        # Entrys angulo_rompientes
        self.mi_angulo_rompiente= tk.StringVar()
        self.entry_angulo_rompiente= tk.Entry(self,textvariable= self.mi_angulo_rompiente)
        self.entry_angulo_rompiente.config(width=20, font=('Arial',12))
        self.entry_angulo_rompiente.grid(row=1, column=3,padx=10,pady=10)

         # Entrys indice_rompiente
        self.mi_indice_rompiente= tk.StringVar()
        self.entry_indice_rompiente= tk.Entry(self,textvariable= self.mi_indice_rompiente)
        self.entry_indice_rompiente.config(width=20, font=('Arial',12))
        self.entry_indice_rompiente.grid(row=2, column=3,padx=10,pady=10)

        # Entrys acelaración_gravitacional
        self.mi_acelaración_gravitacional= tk.StringVar()
        self.entry_acelaración_gravitacional= tk.Entry(self,textvariable= self.mi_acelaración_gravitacional)
        self.entry_acelaración_gravitacional.config(width=20, font=('Arial',12))
        self.entry_acelaración_gravitacional.grid(row=3, column=3,padx=10,pady=10)
        
        # Entrys ubicacion
        self.mi_ubicacion= tk.StringVar()
        self.entry_mi_ubicacion= tk.Entry(self,textvariable= self.mi_ubicacion)
        self.entry_mi_ubicacion.config(width=20, font=('Arial',12))
        self.entry_mi_ubicacion.grid(row=4, column=3,padx=10,pady=10)


        #Boton Nuevo 
        self.boton_nuevo= tk.Button(self,text="Nuevo",command =self.habilitar_campos)
        self.boton_nuevo.config(width=15,
        # en htmlcolorcodes.com se obtienen los colores 
        # fg- color de letra bg - color de fondo
        # cursor='hand2' cambiar el curso de flecha a manito
        # activebackground - Para cambiar el color cuando le de al boton 
        font=('Arial',12,'bold'),fg='white',bg='#0299e4',cursor='hand2',activebackground= 'gray')
        self.boton_nuevo.grid(row=6, column=1,padx=10,pady=10)
        
        # Boton Procesar
        self.boton_procesar= tk.Button(self,text="Procesar",command= self.guardar_datos)
        self.boton_procesar.config(width=15,
        # en htmlcolorcodes.com se obtienen los colores 
        # fg- color de letra bg - color de fondo
        # cursor='hand2' cambiar el curso de flecha a manito
        # activebackground - Para cambiar el color cuando le de al boton 
        font=('Arial',12,'bold'),fg='white',bg='#0299e4',cursor='hand2',activebackground= 'gray')
        self.boton_procesar.grid(row=6, column=2,padx=10,pady=10)

         # Boton Cancelar
        self.boton_cancelar= tk.Button(self,text="Cancelar",command = self.desabilitar_campos)
        self.boton_cancelar.config(width=15,
        # en htmlcolorcodes.com se obtienen los colores 
        # fg- color de letra bg - color de fondo
        # cursor='hand2' cambiar el curso de flecha a manito
        # activebackground - Para cambiar el color cuando le de al boton 
        font=('Arial',12,'bold'),fg='red',bg='white',cursor='hand2',activebackground= 'gray')
        self.boton_cancelar.grid(row=6, column=3,padx=10,pady=10)

         # Metodos para habilitar los campos
    # La funcion se activa cuando le dan al boton a nuevo
    def habilitar_campos(self):
         self.mi_densidad_mar.set('')
         self.mi_densidad_arena.set('')
         self.mi_coeficiente_porocidad.set('')
         self.mi_altura.set('')
         self.mi_angulo_rompiente.set('')
         self.mi_indice_rompiente.set('')
         self.mi_acelaración_gravitacional.set('')


         self.entry_densidad_mar.config(state='normal')
         self.entry_densidad_arena.config(state='normal')
         self.entry_coeficiente_porocidad.config(state='normal')
         self.entry_altura.config(state='normal')
         self.entry_angulo_rompiente.config(state='normal')
         self.entry_indice_rompiente.config(state='normal')
         self.entry_acelaración_gravitacional.config(state='normal')

         self.boton_procesar.config(state='normal')
         self.boton_cancelar.config(state='normal')


    def desabilitar_campos(self):
        self.mi_densidad_mar.set('')
        self.mi_densidad_arena.set('')
        self.mi_coeficiente_porocidad.set('')
        self.mi_altura.set('')
        self.mi_angulo_rompiente.set('')
        self.mi_indice_rompiente.set('')
        self.mi_acelaración_gravitacional.set('')

        self.entry_densidad_mar.config(state='disabled')
        self.entry_densidad_arena.config(state='disabled')
        self.entry_coeficiente_porocidad.config(state='disabled')
        self.entry_altura.config(state='disabled')
        self.entry_angulo_rompiente.config(state='disabled')
        self.entry_indice_rompiente.config(state='disabled')
        self.entry_acelaración_gravitacional.config(state='disabled')


        self.boton_procesar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')

    def guardar_datos(self):
        #tla = tla(
            #self.mi_densidad_arena.get()
            #self.mi_densidad_mar.get()
            #self.mi_coeficiente_porocidad()
        #)

        self.desabilitar_campos()

    def tabla_listado_calculos(self): 
        #Recuperar la lista de peliculas
        #self.lista_peliculas= listar()
        #self.lista_peliculas.reverse() 
        
        self.tabla= ttk.Treeview (self, column=('Ubicacion','ρ', 'ρs','n','Hb','α','k','g','K','Q'))
        self.tabla.grid(row=7,column=0,columnspan= 11)

        #Scrollbar para la tabla si excede 10 registros
        #self.scroll=ttk.Scrollbar(self,orient='vertical',command=self.tabla.ysiew)
        #self.scroll.grid(row=6,column=4,sticky='nse')
        #self.tabla.configure(yscrollcommand= self.scroll.set)


        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='UBICACION')
        self.tabla.heading('#2',text='ρ')
        self.tabla.heading('#3',text='ρs')
        self.tabla.heading('#4',text='n')
        self.tabla.heading('#5',text='Hb')
        self.tabla.heading('#6',text='α')
        self.tabla.heading('#7',text='k')
        self.tabla.heading('#8',text='g')
        self.tabla.heading('#9',text='K')
        self.tabla.heading('#10',text='Q')
        
        

        #Iterar la lista de peliculas
        #for p in self.lista_peliculas:
            #self.tabla.insert('', o, text= p[0])
            #values=(p[1],p[2],p[3])
        
        #Boton Editar 
        self.boton_editar= tk.Button(self,text="Editar")
        self.boton_editar.config(width=15,
        # en htmlcolorcodes.com se obtienen los colores 
        # fg- color de letra bg - color de fondo
        # cursor='hand2' cambiar el curso de flecha a manito
        # activebackground - Para cambiar el color cuando le de al boton 
        font=('Arial',12,'bold'),fg='white',bg='#0299e4',cursor='hand2',activebackground= 'gray')
        self.boton_editar.grid(row=8, column=1,padx=10,pady=10)
        
         # Boton Eliminar
        self.boton_eliminar= tk.Button(self,text="Eliminar")
        self.boton_eliminar.config(width=15,
        # en htmlcolorcodes.com se obtienen los colores 
        # fg- color de letra bg - color de fondo
        # cursor='hand2' cambiar el curso de flecha a manito
        # activebackground - Para cambiar el color cuando le de al boton 
        font=('Arial',12,'bold'),fg='red',bg='white',cursor='hand2',activebackground= 'gray')
        self.boton_eliminar.grid(row=8, column=2,padx=10,pady=10)


    
 

        

