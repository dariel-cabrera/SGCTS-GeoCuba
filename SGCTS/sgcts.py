import tkinter as tk
from cliente.interfaz import Frame,barra_menu

# Funcion Principal
def main():
    #Ventana o Raiz
    root= tk.Tk()
    
    #Para agg el titulo
    root.title("SGCTS-GeoCuba")
    # Para cambiar el icono se usa una foto con .ico
    root.iconbitmap('img/estrellita.ico')
    # para que no se mueva la ventana
    root.resizable(0,0)

    barra_menu(root)

    app= Frame(root = root)
   
    

    # Esta instruccion tiene que estar al final
    app.mainloop()

if __name__ == '__main__':
    main()