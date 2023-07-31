import tkinter as tk
from tkinter import ttk, messagebox
import util.generic as utl
from controller.ingredient_controller import ingredientes
from controller.recipe_controller import recetas_posibles
from controller.instruction_controller import obtener_instruccion

import tkinter as tk
from tkinter import ttk

class MasterPanel:


    def limpiar_texto_instrucciones(self):
        self.texto_instrucciones.delete(1.0, tk.END)


    def limpiar_lista(self):
        self.lista_ingredientes.delete(0, tk.END)
        self.ingredientes_seleccionados = []
        self.limpiar_texto_instrucciones()
        self.limpiar_tabla()


    def agregar_ingrediente(self):
        ingrediente = self.combobox_ingrediente.get()
        if ingrediente != "" and ingrediente not in self.ingredientes_seleccionados:
            self.lista_ingredientes.insert(tk.END, ingrediente)
            self.ingredientes_seleccionados.append(ingrediente)


    def buscar_recetas(self):
        self.limpiar_tabla()
        self.limpiar_texto_instrucciones()
        recetas = recetas_posibles( self.ingredientes_seleccionados )
        if len(recetas) == 0:
            messagebox.showinfo("Recetas","No se encontraron recetas con los ingredientes seleccionados")

        for receta in recetas:
            self.tabla_recetas.insert("", "end", text=receta[0], values=(receta[0], receta[2], receta[3] + 'gr', receta[4] + 'gr', receta[5] + 'gr'))


    def mostrar_instruccion(self, event):
        receta_seleccionada = self.tabla_recetas.selection()

        if receta_seleccionada:
            receta = receta_seleccionada[0]
            nombre_receta = self.tabla_recetas.item(receta, 'values')[0]
            instruccion = obtener_instruccion(nombre_receta)

            # Limpiar las instrucciones anteriores
            self.texto_instrucciones.delete(1.0, tk.END)

            # Reemplazar los caracteres especiales "\n" con saltos de línea reales
            instruccion_formateada = instruccion.replace("\\n", "\n")

            # Insertar las nuevas instrucciones en el widget Text
            self.texto_instrucciones.insert(tk.END, instruccion_formateada)

    
    def limpiar_tabla(self):
        self.tabla_recetas.delete(*self.tabla_recetas.get_children())



    def cerrar_aplicacion(self):
        self.ventana.destroy()
    
    
    
    def __init__(self):
        self.ingredientes_seleccionados = []  
        # Crear ventana
        self.ventana = tk.Tk()
        self.ventana.title("Healty Bites")
        self.ventana.geometry("931x515")
        self.ventana.config(bg="#fff0d3")
        #ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 931, 505)

        # Crear frame principal
        frame = ttk.Frame(self.ventana, padding="20")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Título
        titulo = ttk.Label(frame, text="Healty Bites", font=("Forte", 20))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Botón "Cerrar Aplicación"
        boton_cerrar = tk.Button(frame, text="Cerrar Aplicación", command=self.cerrar_aplicacion)
        boton_cerrar.grid(row=0, column=1, padx=5, pady=5, sticky='E')

        # Frame izquierdo
        frame_izquierdo = ttk.Frame(frame)
        frame_izquierdo.grid(row=1, column=0, padx=10)

        # Combobox y botón "Agregar"
        self.combobox_ingrediente = ttk.Combobox(frame_izquierdo, values = ingredientes, width=20, state="readonly")
        self.combobox_ingrediente.grid(row=0, column=0, padx=5, pady=5)
        self.combobox_ingrediente.set(ingredientes[0])

        boton_agregar = tk.Button(frame_izquierdo, text="Agregar", command=self.agregar_ingrediente)
        boton_agregar.grid(row=0, column=1, padx=5, pady=5)


        # Lista de ingredientes agregados
        self.lista_ingredientes = tk.Listbox(frame_izquierdo, height=5)
        self.lista_ingredientes.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=(tk.W, tk.E))


        # Botones "Limpiar" y "Buscar recetas"
        boton_limpiar = tk.Button(frame_izquierdo, text="Limpiar", command=self.limpiar_lista)
        boton_limpiar.grid(row=2, column=0, padx=5, pady=5)


        boton_buscar_recetas = tk.Button(frame_izquierdo, text="Buscar recetas", command=self.buscar_recetas)
        boton_buscar_recetas.grid(row=2, column=1, padx=5, pady=5)


        # Frame derecho
        frame_central = tk.Frame(frame)
        frame_central.grid(row=1, column=1, padx=10)

        # Etiqueta "Recetas disponibles"
        label_recetas_disponibles = tk.Label(frame_central, text="Recetas disponibles")
        label_recetas_disponibles.pack()


        # Crear un Treeview con 5 columnas
        self.tabla_recetas = ttk.Treeview(frame_central, columns=("Receta", "kcal", "carbohidratos", "grasas", "proteinas"), show="headings")


        # Configurar cada columna
        self.tabla_recetas.heading("Receta", text="Receta")
        self.tabla_recetas.column("Receta", width=200)

        self.tabla_recetas.heading("kcal", text="kcal")
        self.tabla_recetas.column("kcal", width=100)

        self.tabla_recetas.heading("carbohidratos", text="carbohidratos")
        self.tabla_recetas.column("carbohidratos", width=100)

        self.tabla_recetas.heading("grasas", text="grasas")
        self.tabla_recetas.column("grasas", width=100)

        self.tabla_recetas.heading("proteinas", text="proteinas")
        self.tabla_recetas.column("proteinas", width=100)

        # Añadir la tabla al frame
        self.tabla_recetas.pack(fill=tk.BOTH, expand=True)

        self.tabla_recetas.bind('<<TreeviewSelect>>', self.mostrar_instruccion)

        # Crear un widget Text para mostrar las instrucciones
        self.texto_instrucciones = tk.Text(frame_central, wrap=tk.WORD, height=10, width=50)
        self.texto_instrucciones.pack(fill=tk.BOTH, expand=True)


        self.ventana.mainloop()