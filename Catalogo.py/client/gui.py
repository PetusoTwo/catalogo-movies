from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from PIL import ImageTk, Image
import sys
sys.path.append('C:/Users/Usuario/Desktop/Apps_py/Catalogo_movies_app/Catalogo.py/model')
from model.pelicula_dao import crear_tabla, borrar_tabla
import webbrowser
import random
from model.pelicula_dao import Pelicula, guardar, lista, editar, eliminar
def menu_ventana(root):
    menu_ventana =  Menu(root, background="#d6fffa")
    root.config(menu = menu_ventana, width = 280, height = 280)
    
    def contacto_creador():
        webbrowser.open_new("https://github.com/PetusoTwo")
    
    def info_crear_db():
        showinfo(title="Base de datos", message="Base de datos creada correctamente")
        crear_tabla()
    
    def info_borrar_db(): 
        showinfo(title="Base de datos", message="La base de datos ha sido eliminada")
        borrar_tabla()
        
    # def cambiar_bg():
    #     #colores = []
    #     root.config(background="cyan")
    #Menus Anclados
    
    menu_inicio = Menu(menu_ventana, tearoff=0, bg="#8f99fb", fg="#11028d")
    menu_ventana.add_cascade(label="Inicio", menu=menu_inicio)
    menu_inicio.add_command(label="Crear base de Datos", command= info_crear_db)
    menu_inicio.add_command(label="Eliminar base de Datos", command= info_borrar_db)
    menu_inicio.add_command(label="Salir", command= root.destroy)
    
    menu_configuracion = Menu(menu_ventana, tearoff=0, bg="#8f99fb", fg="#11028d")
    menu_ventana.add_cascade(label="Configuracion", menu=menu_configuracion)
    menu_configuracion.add_command(label="Cambiar tema")
    
    menu_ayuda = Menu(menu_ventana, tearoff=0, bg="#8f99fb", fg="#11028b")
    menu_ventana.add_cascade(label="Ayuda", menu=menu_ayuda)
    menu_ayuda.add_command(label="Contactar al creador", command=contacto_creador)
    
#Marco
    
class Frame(Frame):
    def __init__(self, root = None): 
        super().__init__(root, width=960, height=800)
        self.root = root
        self.config(bg="#d6fffa") #-------- Fondo de las letras
        self.pack()
        self.id_pelicula = None
        self.campo_movie()
        self.desactivar_campos()
        self.guardar_datos()
        self.tabla_movies()
        #self.activar_campos()
        
    def campo_movie(self):
        self.label_nombre = Label(self, text="Nombre de la pelicula: ")
        self.label_nombre.config(font=("garaldus", 15, "italic"))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        
        self.label_genero = Label(self, text="Genero de la pelicula: ")
        self.label_genero.config(font=("garaldus", 15, "italic"))
        self.label_genero.grid(row=1, column=0, padx=10, pady= 10)
        
        self.label_duracion = Label(self, text="Duración de la pelicula: ")
        self.label_duracion.config(font=("garaldus", 15, "italic"))
        self.label_duracion.grid(row=2, column=0, padx= 10, pady=10)
        
        #Entradas (INPUT)
        
        #Nombre de pelicula
        self.nombre = StringVar()
        self.entrada_nombre = Entry(self, textvariable= self.nombre)
        self.entrada_nombre.grid(row=0, column=1, padx= 20 , pady=10)
        self.entrada_nombre.config(width=40, font=("arial", 15, "italic"), background="ivory")
        
        #Genero de pelicula
        self.genero = StringVar()
        self.entrada_genero = Entry(self, textvariable= self.genero)
        self.entrada_genero.grid(row=1, column=1, padx= 20, pady=10)
        self.entrada_genero.config(width=40, font=("arial", 15, "italic"), background="ivory")
        
        #Duracion de pelicula
        self.duracion = StringVar()
        self.entrada_duracion = Entry(self, textvariable= self.duracion)
        self.entrada_duracion.grid(row=2, column=1, padx= 20, pady=10)
        self.entrada_duracion.config(width=40, font=("arial", 15, "italic"), background ="ivory")
        
        ##BOTONES
        #img = ImageTk.PhotoImage(Image.open("../Imagenes/new.ico"))
        self.boton_new = Button(self, text="Nuevo ", command=self.activar_campos)#, image=img)
        self.boton_new.grid(row= 0, column = 2, pady=7)
        self.boton_new.config(width = 20, font=("Arial", 15, "bold")
                            ,fg = "black",
                            bg= "darksalmon",
                            padx=10, cursor="hand2", activebackground="tomato")
        
        # self.boton_new = Button(Image = img)
        
        self.boton_save = Button(self, text="Guardar", #command= self.guardar_datos,
                                command = self.info_ventana_save)
        self.boton_save.grid(row=1, column=2, pady=7)
        self.boton_save.config(width=20, font=("Arial", 15, "bold")
                            ,fg= "black", bg="darksalmon",
                            padx=10, cursor="hand2", activebackground="tomato")
        
        self.boton_cacelar = Button(self, text="Cancelar", command=self.desactivar_campos)
        self.boton_cacelar.grid(row=2, column=2, pady=7)
        self.boton_cacelar.config(width=20, font=("Arial", 15, "bold"),
                                fg="black", bg="darksalmon",
                                padx=10, cursor="hand2", activebackground="tomato")

    def activar_campos(self):
        
        #Para que los entrys queden vacios
        
        self.nombre.set('')
        self.genero.set('')
        self.duracion.set('')
        
        #entradas normal
        
        self.entrada_nombre.config(state = "normal")
        self.entrada_genero.config(state = "normal")
        self.entrada_duracion.config(state = "normal")
        
        #botones desactivados
        
        self.boton_save.config(state = "normal")
        self.boton_cacelar.config(state= "normal")
    def desactivar_campos(self): 
        
        #Para que los entrys queden vacios
        self.id_pelicula = None
        self.nombre.set('')
        self.genero.set('')
        self.duracion.set('')
        
        #entradas desactivadas
        
        self.entrada_nombre.config(state = "disabled")
        self.entrada_genero.config(state = "disabled")
        self.entrada_duracion.config(state = "disabled")
        
        #botones desactivados
        
        self.boton_save.config(state = "disabled")
        self.boton_cacelar.config(state= "disabled")
        
    def guardar_datos(self):
        
        pelicula = Pelicula(
                            self.nombre.get(), 
                            self.duracion.get(),
                            self.genero.get(),
                            )
        
        
        if self.id_pelicula == None:
            guardar(pelicula)
        else:
            editar(pelicula, self.id_pelicula)
            
        self.tabla_movies()
        self.desactivar_campos()

    def tabla_movies(self):
        
        self.listar_movies= lista() 
        self.listar_movies.reverse()  
        
        self.tabla = ttk.Treeview(self, column = ("Nombre", "Duración", "Género"))
        self.tabla.grid(row=3 , column= 0, columnspan=4)
        
        self.scroll = ttk.Scrollbar(self, 
                                    orient="vertical", command=self.tabla.yview)
        self.scroll.grid(row=3, column=2)
        self.tabla.heading("#0", text= "Codigo")
        self.tabla.heading("#1", text= "Nombre")
        self.tabla.heading("#2", text= "Duración")
        self.tabla.heading("#3", text= "Género")
        
        #iterar la lista de movies
        for i in self.listar_movies:
            self.tabla.insert("", 0, text=i[0], 
                        values=(i[1], i[2], i[3]))
        
        #Botones 2
        ##Editar
        self.boton_edit = Button(self, text="Editar campo", command=self.editar_datos)
        self.boton_edit.grid( row=5,column=0,pady= 40, padx=10)
        self.boton_edit.config(width = 20, font=("Arial", 15, "bold")
                            ,fg = "#e4cbff",
                            bg= "#9a0200",
                            padx=30, cursor="hand2", activebackground="tomato")
        
        
        
        #Eliminar
        self.boton_eliminar = Button(self, text="Eliminar campo", command=self.info_ventana_eliminar)
        self.boton_eliminar.grid(row=5,column=2, pady=40, padx=10)
        self.boton_eliminar.config(width=20, font=("Arial", 15, "bold"),
                                fg="#e4cbff", bg="#9a0200",
                                padx=30, cursor="hand2", activebackground="tomato") 
        
        #Salir 
        self.boton_quit = Button(self, text= "Salir", command= self.root.destroy)
        self.boton_quit.grid(row=5, column=1, pady=40, padx=10)
        self.boton_quit.config(width=20, font=("Arial", 15, "bold"), 
                            fg="#e4cbff", bg="#9a0200", 
                            padx=30, cursor="hand2", activebackground="tomato")
        
    def info_ventana_save(self):
        respuesta = askquestion(title="Catalogo Movies", message="¿Desea guardar la información?")
        
        if respuesta == "no":
            showerror(title="Catalogo Movies", message="Informacion no guardada D:")
        else: 
            showinfo(title="Catalogo Movies", message="Informacion guardada :3")
            self.guardar_datos()
            
    def info_ventana_eliminar(self):
        respuesta1 = askquestion(title="Catalogo Movies", message="¿Desea eliminar la información seleccionada?")
        
        if respuesta1 == "no": 
            showinfo(title="Catalogo Movies", message="Informacion a salvo")
        else: 
            showwarning(title="Catalogo Movies", message="Informacion eliminada D:")
        self.eliminar_datos()
            
    def editar_datos(self): 
        try:
            
            self.nombre_pelicula = self.tabla.item(self.tabla.selection())["values"][0]
            self.duracion_pelicula = self.tabla.item(self.tabla.selection())["values"][1]
            self.genero_pelicula = self.tabla.item(self.tabla.selection())["values"][2]
            
            self.activar_campos()
            
            self.entrada_nombre.insert(0, self.nombre_pelicula)
            self.entrada_duracion.insert(0, self.duracion_pelicula)
            self.entrada_genero.insert(0, self.genero_pelicula) 
        except:
            showerror(title="Edicion de datos", message="No ha seleccionada ningun campo")
    def eliminar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())["text"]
            eliminar(self.id_pelicula)
            self.tabla_movies()
            self.id_pelicula = None
        except:
            showerror(title="Error de eliminacion", message="No has seleccionado ningun registro")
            