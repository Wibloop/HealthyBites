
import tkinter as tk
from tkinter import ttk, messagebox
import util.generic as utl



class FormLoginDesigner:

    def obteniendo_texto( self,nombre_archivo ):
        texto = utl.obtener_texto( nombre_archivo )
        return texto

    def verificar_inicio(self):
        pass

    def registrar_usuario(self):
        pass

    def aceptar_advertencia(self):
        self.ventana_adv.destroy()
        self.init_ventana_login()

    def rechazar_advertencia(self):
        self.ventana_adv.destroy()
        self.ventana.destroy()

    def init_advertencia(self):
        CONDICIONES_DE_USO = self.obteniendo_texto( "./persistence/advertencia_de_uso.txt" )
        self.ventana_adv = tk.Toplevel(self.ventana)
        self.ventana_adv.title('Advertencias de uso')
        self.ventana_adv.geometry('800x500')
        self.ventana_adv.config(bg='#fff0d3')
        self.ventana_adv.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana_adv, 800, 500)

        label_adv = tk.Label(self.ventana_adv, text=CONDICIONES_DE_USO, wraplength=750, bg='#fff0d3', fg="#567159", font=('Arial', 14), justify='center')
        label_adv.pack(expand=True)

        boton_aceptar = tk.Button(self.ventana_adv, text='Aceptar', bg='#567159', fg="#fff0d3", font=('Forte', 20), command = lambda: self.aceptar_advertencia())
        boton_aceptar.pack(side='left', expand=True)

        boton_rechazar = tk.Button(self.ventana_adv, text='Rechazar', bg='#567159', fg="#fff0d3", font=('Forte', 20), command = lambda: self.rechazar_advertencia())
        boton_rechazar.pack(side='right', expand=True)

    def init_ventana_login(self):
        self.ventana.title('HealthyBites')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fff0d3')
        self.ventana.resizable(width=0, height=0)
        self.ventana.deiconify()  # Volvemos a mostrar la ventana principal.
        # Esto sirve para centrar la ventana
        utl.centrar_ventana(self.ventana, 800, 500)
        
        self.logo = utl.leer_imagen('./static/imagenes/logo.png', (330, 350))
        # Este frame se posicionara dentro de la ventana. Es el frame o pestania del logo
        frame_logo = tk.Frame(self.ventana, bd=0, bg='#fff0d3', width=300, relief=tk.SUNKEN, padx=10, pady=10)
        # Esto sirve para crear un frame
        frame_logo.pack(side='right', expand=tk.NO, fill=tk.BOTH)
        # Esto sirve para que el frame se adapte al tamaño de la ventana
        label = tk.Label(frame_logo, image=self.logo, bg='#fff0d3')
        # Esto sirve para crear una etiqueta
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # Este frame se posicionara dentro de la ventana. Es el frame o pestania del formulario
        frame_formulario = tk.Frame(self.ventana, bd=0, bg='#fff0d3', width=300, relief=tk.SUNKEN, padx=10, pady=10)
        frame_formulario.pack(side='left', expand=tk.YES, fill=tk.BOTH)
        # Cuadrado(frame) de la ventana opuesta al logo

        # Este frame se posicionara dentro del frame_formulario. Es el frame o pestania del formulario para iniciar sesion
        frame_formulario_top = tk.Frame(frame_formulario, height=50, bd=0, bg='#fff0d3', width=300, relief=tk.SUNKEN, padx=10, pady=10)
        frame_formulario_top.pack(side='top', expand=tk.NO, fill=tk.X)
        title = tk.Label(frame_formulario_top, text='Iniciar Sesión', bg='#fff0d3', fg="#567159", font=('Forte', 40))
        title.pack(side='top', expand=tk.YES, fill=tk.BOTH)
        # Letras de inicio de sesion y su fondo

        # Este frame se posicionara dentro del frame_formulario y justo debajo del frame_formulario_top. Es el frame o pestania del formulario para iniciar sesion
        frame_formulario_bottom = tk.Frame(frame_formulario, bd=0, bg='#fff0d3', width=300, relief=tk.SUNKEN, padx=10, pady=10)
        frame_formulario_bottom.pack(side='bottom', expand=tk.YES, fill=tk.BOTH)

        # Titulo de la etiqueta de Usuario y sus colores
        etiqueta_usuario = tk.Label(frame_formulario_bottom, text='Usuario', bg='#fff0d3', fg="#567159", font=('Forte', 20), anchor=tk.W)
        etiqueta_usuario.pack(fill=tk.X, padx=10, pady=10)
        self.usuario = tk.Entry(frame_formulario_bottom, bg='#d8c9ac', fg="#567159", font=('Gill Sans MT', 20))
        # Se usa entry cuando se quiere ingresar texto en un cuadro de texto
        self.usuario.pack(fill=tk.X, padx=10, pady=10)

        # Titulo de la etiqueta de Contraseña y sus colores
        etiqueta_contraseña = tk.Label(frame_formulario_bottom, text='Contraseña', bg='#fff0d3', fg="#567159", font=('Forte', 20), anchor=tk.W)
        etiqueta_contraseña.pack(fill=tk.X, padx=10, pady=10)
        self.contrasena = tk.Entry(frame_formulario_bottom, bg='#d8c9ac', fg="#567159", font=('Arial', 20), show='*')
        self.contrasena.pack(fill=tk.X, padx=10, pady=10)

        # Boton de Iniciar Sesion y sus colores
        boton_iniciar_sesion = tk.Button(frame_formulario_bottom, text='Iniciar Sesión', bg='#567159', fg="#fff0d3", font=('Forte', 20), command = lambda: self.verificar_inicio())
        boton_iniciar_sesion.pack(fill=tk.X, padx=10, pady=10)

        registrarse = tk.Button(frame_formulario_bottom, text='Registrarse', bg='#567159', fg="#fff0d3", font=('Forte', 20), command = lambda: self.registrar_usuario())
        registrarse.pack(fill=tk.X, padx=10, pady=10,)


    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.withdraw()  # Escondemos la ventana principal hasta que el usuario acepte las advertencias.
        self.init_advertencia()
        self.ventana.mainloop()

