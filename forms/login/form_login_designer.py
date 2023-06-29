import tkinter as tk
from tkinter import ttk, messagebox
import util.generic as utl

class FormLoginDesigner:
    #Esta clase sirve para crear el diseño de la ventana de inicio de sesion
    #Esta clase va a ser la clase hereada por la clase Form_Login


    def verificar_inicio(self):
        pass
    #Dejamos las funciones vacias para que no de error al ejecutar el programa

    def registrar_usuario(self):
        pass
    #Las funciones se invocan para que no exista error al ejecutar el programa


    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('HealthyBites')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fff0d3')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800, 500)
        #Esto sirve para centrar la ventana
        
        logo = utl.leer_imagen('./static/imagenes/logo.png', (330, 350))
        
        #Este frame se posicionara dentro de la ventana. Es el frame o pestania del logo
        frame_logo = tk.Frame(self.ventana, bd=0, bg='#fff0d3', width=300, relief=tk.SUNKEN, padx=10, pady=10)
        #Esto sirve para crear un frame
        frame_logo.pack(side='right', expand=tk.NO, fill=tk.BOTH)
        #Esto sirve para que el frame se adapte al tamaño de la ventana
        label = tk.Label(frame_logo, image=logo, bg='#fff0d3')
        #Esto sirve para crear una etiqueta
        label.place(x=0, y=0, relwidth=1, relheight=1)

        #Este frame se posicionara dentro de la ventana. Es el frame o pestania del formulario
        frame_formulario = tk.Frame(self.ventana, bd=0, bg='#fff0d3', width=300, relief=tk.SUNKEN, padx=10, pady=10)
        frame_formulario.pack(side='left', expand=tk.YES, fill=tk.BOTH)
        #Cuadrado(frame) de la ventana opuesta al logo

        #Este frame se posicionara dentro del frame_formulario. Es el frame o pestania del formulario para iniciar sesion
        frame_formulario_top = tk.Frame(frame_formulario, height=50, bd=0, bg='#fff0d3', width=300, relief=tk.SUNKEN, padx=10, pady=10)
        frame_formulario_top.pack(side='top', expand=tk.NO, fill=tk.X)
        title = tk.Label(frame_formulario_top, text='Iniciar Sesión', bg='#fff0d3', fg="#567159", font=('Forte', 40))
        title.pack(side='top', expand=tk.YES, fill=tk.BOTH)
        #Letras de inicio de sesion y su fondo

        #Este frame se posicionara dentro del frame_formulario y justo debajo del frame_formulario_top. Es el frame o pestania del formulario para iniciar sesion
        frame_formulario_bottom = tk.Frame(frame_formulario, bd=0, bg='#fff0d3', width=300, relief=tk.SUNKEN, padx=10, pady=10)
        frame_formulario_bottom.pack(side='bottom', expand=tk.YES, fill=tk.BOTH)

        #Titulo de la etiqueta de Usuario y sus colores
        etiqueta_usuario = tk.Label(frame_formulario_bottom, text='Usuario', bg='#fff0d3', fg="#567159", font=('Forte', 20), anchor=tk.W)
        etiqueta_usuario.pack(fill=tk.X, padx=10, pady=10)
        self.usuario = tk.Entry(frame_formulario_bottom, bg='#d8c9ac', fg="#567159", font=('Gill Sans MT', 20))
        #Se usa entry cuando se quiere ingresar texto en un cuadro de texto
        self.usuario.pack(fill=tk.X, padx=10, pady=10)

        #Titulo de la etiqueta de Contraseña y sus colores
        etiqueta_contraseña = tk.Label(frame_formulario_bottom, text='Contraseña', bg='#fff0d3', fg="#567159", font=('Forte', 20), anchor=tk.W)
        etiqueta_contraseña.pack(fill=tk.X, padx=10, pady=10)
        self.contraseña = tk.Entry(frame_formulario_bottom, bg='#d8c9ac', fg="#567159", font=('Arial', 20), show='*')
        self.contraseña.pack(fill=tk.X, padx=10, pady=10)

        #Boton de Iniciar Sesion y sus colores
        boton_iniciar_sesion = tk.Button(frame_formulario_bottom, text='Iniciar Sesión', bg='#567159', fg="#fff0d3", font=('Forte', 20), command = lambda: self.verificar_inicio())
        boton_iniciar_sesion.pack(fill=tk.X, padx=10, pady=10)

        registrarse = tk.Button(frame_formulario_bottom, text='Registrarse', bg='#567159', fg="#fff0d3", font=('Forte', 20), command = lambda: self.registrar_usuario())
        registrarse.pack(fill=tk.X, padx=10, pady=10,)

        self.ventana.mainloop()