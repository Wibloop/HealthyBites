import tkinter as tk
from tkinter import ttk, messagebox
import util.generic as utl
from controller.ingredient_controller import ingredientes
from controller.recipe_controller import recetas_posibles

import tkinter as tk
from tkinter import ttk

class MasterPanel:
    def limpiar_lista(self):
        self.lista_ingredientes.delete(0, tk.END)
        self.ingredientes_seleccionados = []

    def agregar_ingrediente(self):
        ingrediente = self.combobox_ingrediente.get()
        if ingrediente != "" and ingrediente not in self.ingredientes_seleccionados:
            self.lista_ingredientes.insert(tk.END, ingrediente)
            self.ingredientes_seleccionados.append(ingrediente)

    def buscar_recetas(self):
        self.limpiar_tabla()
        recetas = recetas_posibles( self.ingredientes_seleccionados )

        for receta in recetas:
            self.tabla_recetas.insert("", "end", text=receta[0], values=(receta[2], receta[3], receta[4], receta[5]))

    def limpiar_tabla(self):
        self.tabla_recetas.delete(*self.tabla_recetas.get_children())

    def __init__(self):
        self.ingredientes_seleccionados = []  
        # Crear ventana
        ventana = tk.Tk()
        ventana.title("Healty Bites")

        # Crear frame principal
        frame = ttk.Frame(ventana, padding="20")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Título
        titulo = ttk.Label(frame, text="Healty Bites", font=("Helvetica", 20))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Frame izquierdo
        frame_izquierdo = ttk.Frame(frame)
        frame_izquierdo.grid(row=1, column=0, padx=10)

        # Combobox y botón "Agregar"
        self.combobox_ingrediente = ttk.Combobox(frame_izquierdo, values = ingredientes, width=20, state="readonly")
        self.combobox_ingrediente.grid(row=0, column=0, padx=5, pady=5)
        self.combobox_ingrediente.set(ingredientes[0])

        boton_agregar = ttk.Button(frame_izquierdo, text="Agregar", command=self.agregar_ingrediente)
        boton_agregar.grid(row=0, column=1, padx=5, pady=5)

        # Lista de ingredientes agregados
        self.lista_ingredientes = tk.Listbox(frame_izquierdo, height=5)
        self.lista_ingredientes.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=(tk.W, tk.E))

        # Botones "Limpiar" y "Buscar recetas"
        boton_limpiar = ttk.Button(frame_izquierdo, text="Limpiar", command=self.limpiar_lista)
        boton_limpiar.grid(row=2, column=0, padx=5, pady=5)

        boton_buscar_recetas = ttk.Button(frame_izquierdo, text="Buscar recetas", command=self.buscar_recetas)
        boton_buscar_recetas.grid(row=2, column=1, padx=5, pady=5)

        # Frame derecho
        frame_derecho = ttk.Frame(frame)
        frame_derecho.grid(row=1, column=1, padx=10)

        # Label "Recetas disponibles"
        label_recetas_disponibles = ttk.Label(frame_derecho, text="Recetas disponibles")
        label_recetas_disponibles.pack()

        # Tabla con scroll vertical para recetas disponibles
        self.tabla_recetas = ttk.Treeview(frame_derecho, columns=("Nombre", "kcal", "carbohidratos", "grasas", "proteinas"))

        self.tabla_recetas.heading("#0", text="Receta")
        self.tabla_recetas.column("#0", width=200)
        self.tabla_recetas.heading("#1", text="kcal")
        self.tabla_recetas.column("#1", width=100)
        self.tabla_recetas.heading("#2", text="carbohidratos")
        self.tabla_recetas.column("#2", width=100)
        self.tabla_recetas.heading("#3", text="grasas")
        self.tabla_recetas.column("#3", width=100)
        self.tabla_recetas.heading("#4", text="proteinas")
        self.tabla_recetas.column("#4", width=100)
        self.tabla_recetas.pack(fill=tk.BOTH, expand=True)

        ventana.mainloop()