import tkinter as tk
from tkinter import ttk, messagebox
from model.pelicula_dao import crear_tabla, borrar_tabla, Pelicula, guardar, getPeliculas, editar, eliminar

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 1000, height=100)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    menu_consulta = tk.Menu(barra_menu, tearoff=0)
    menu_configuracion = tk.Menu(barra_menu, tearoff=0)
    menu_ayuda = tk.Menu(barra_menu, tearoff=0)

    barra_menu.add_cascade(label="Inicio", menu=menu_inicio)
    barra_menu.add_cascade(label="Consulta", menu=menu_consulta)
    barra_menu.add_cascade(label="Configuración", menu=menu_configuracion)
    barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

    menu_inicio.add_command(label="Nuevo registro", command=crear_tabla)
    menu_inicio.add_command(label="Eliminar registro", command=borrar_tabla)
    menu_inicio.add_command(label="Salir", command=root.destroy)


class Frame(tk.Frame):
    def __init__(self, root= None):
        super().__init__(root, width=900, height=800, background="#212121")
        self.root = root
        self.pack()
        self.config()
        self.campos_label()
        self.deshabilitar_campos()
        self.tabla()
        self.id = None
    
    def campos_label(self):

        # definicion de los campos de ingreso de datos
        self.label_nombre = tk.Label(self, text="Nombre")
        self.label_nombre.config(font=("Arial", 12, "bold"), fg="white", bg="#212121")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_duracion = tk.Label(self, text="Durancion (min)")
        self.label_duracion.config(font=("Arial", 12, "bold"), fg="white", bg="#212121")
        self.label_duracion.grid(row=1, column=0, padx=10, pady=10)

        self.label_genero= tk.Label(self, text="Genero")
        self.label_genero.config(font=("Arial", 12, "bold"), fg="white", bg="#212121")
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)

        #definicion de inputs o entradas
        self.in_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.in_nombre)
        self.entry_nombre.config(width=50, font=("Arial", 12))
        self.entry_nombre.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

        self.in_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable=self.in_duracion)
        self.entry_duracion.config(width=50, font=("Arial", 12))
        self.entry_duracion.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        self.in_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable=self.in_genero)
        self.entry_genero.config(width=50, font=("Arial", 12))
        self.entry_genero.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

        #botones
        self.boton_nuevo = tk.Button(self, text="Nuevo", command= self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=("Arial", 12, "bold"), fg="#DAD5D6", bg="#158145",           cursor="hand2", activebackground="#35BD6F")
        self.boton_nuevo.grid(row=3, column=0, padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text="Guardar", command=self.guardar_datos)
        self.boton_guardar.config(width=20, font=("Arial", 12, "bold"), fg="#DAD5D6", bg="#1558A2", cursor="hand2", activebackground="#3586DF")
        self.boton_guardar.grid(row=3, column=1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(self, text="Cancelar", command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=("Arial", 12, "bold"), fg="#DAD5D6", bg="#BD152E", cursor="hand2", activebackground="#E15370")
        self.boton_cancelar.grid(row=3, column=2, padx=10, pady=10)

        #funciones habiulitar y deshabilitar

    def habilitar_campos(self):
        self.in_nombre.set("")
        self.in_duracion.set("")
        self.in_genero.set("")

        self.entry_nombre.config(state="normal")
        self.entry_duracion.config(state="normal")
        self.entry_genero.config(state="normal")
        self.boton_guardar.config(state="normal")
        self.boton_cancelar.config(state="normal")

    def deshabilitar_campos(self):
        self.in_nombre.set("")
        self.in_duracion.set("")
        self.in_genero.set("")
        
        self.id = None

        self.entry_nombre.config(state="disabled")
        self.entry_duracion.config(state="disabled")
        self.entry_genero.config(state="disabled")
        self.boton_guardar.config(state="disabled")
        self.boton_cancelar.config(state="disabled")
    
    def guardar_datos(self):

        pelicula = Pelicula(
            self.in_nombre.get(), 
            self.in_duracion.get(), 
            self.in_genero.get()
        )

        if self.id == None:
            guardar(pelicula)
        else:
            editar(pelicula, self.id)
        
        self.tabla()
        self.deshabilitar_campos()
    
    def tabla(self):
        self.lista = getPeliculas()
        self.lista.reverse()

        self.tabla_peli = ttk.Treeview(self, columns= ("Nombre", "Duración", "Genero"))
        self.tabla_peli.grid(row=4, column=0, columnspan=4, sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla_peli.yview)
        self.scroll.grid(row=4, column=4, sticky='nse')
        self.tabla_peli.configure(yscrollcommand=self.scroll.set)

        self.tabla_peli.heading("#0", text="ID")
        self.tabla_peli.heading("#1", text="Nombre")
        self.tabla_peli.heading("#2", text="Duración")
        self.tabla_peli.heading("#3", text="Genero")

        for p in self.lista:
            self.tabla_peli.insert("", 0, text=p[0], values=(p[1], p[2], p[3]))

        self.boton_editar = tk.Button(self, text="Editar", command=self.editar_datos)
        self.boton_editar.config(width=20, font=("Arial", 12, "bold"), fg="#DAD5D6", bg="#158145",           cursor="hand2", activebackground="#35BD6F")
        self.boton_editar.grid(row=5, column=0, padx=10, pady=10)

        self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.eliminar_registro)
        self.boton_eliminar.config(width=20, font=("Arial", 12, "bold"), fg="#DAD5D6", bg="#BD152E", cursor="hand2", activebackground="#E15370")
        self.boton_eliminar.grid(row=5, column=1, padx=10, pady=10)
    

    def editar_datos(self):
        try:
            self.id = self.tabla_peli.item(self.tabla_peli.selection())["text"]
            self.nombre = self.tabla_peli.item(self.tabla_peli.selection())["values"][0]
            self.duracion = self.tabla_peli.item(self.tabla_peli.selection())["values"][1]
            self.genero = self.tabla_peli.item(self.tabla_peli.selection())["values"][2]

            self.habilitar_campos()

            self.entry_nombre.insert(0, self.nombre)
            self.entry_duracion.insert(0, self.duracion)
            self.entry_genero.insert(0, self.genero)

        except:
            titulo = "Editar película"
            mensaje = "No se ha seleccionado registro"
            messagebox.showwarning(titulo, mensaje)
    
    def eliminar_registro(self):
        self.id = self.tabla_peli.item(self.tabla_peli.selection())["text"]
        eliminar(self.id)
        self.tabla()
        self.id = None