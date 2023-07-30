import tkinter as tk
from tkinter import ttk, messagebox
import util.generic as utl
from forms.login.form_login_designer import FormLoginDesigner
from forms.master.form_master import MasterPanel
from controller.user_controller import iniciar_sesion, crear_cuenta

from util.auth_verification import validate_credentials


class FormLogin(FormLoginDesigner):

    # Función para verificar el inicio de sesión
    def verificar_inicio(self):
        # Obtenemos los datos del usuario y contraseña ingresados en los campos
        usuario = self.usuario.get()
        contrasena = self.contrasena.get()

        # Llamamos a la función iniciar_sesion del controlador de usuarios para validar las credenciales
        if iniciar_sesion(usuario, contrasena):
            # Si las credenciales son válidas, mostramos un mensaje de éxito y cerramos la ventana de inicio de sesión
            messagebox.showinfo('Login', 'Login exitoso')
            self.ventana.destroy()
            # Abrimos la ventana del panel principal del programa (MasterPanel)
            MasterPanel()
        else:
            # Si las credenciales no son válidas, mostramos un mensaje de error
            messagebox.showerror('Login', 'Usuario o contraseña incorrectos')

    # Función para registrar un nuevo usuario
    def registrar_usuario(self):
        # Obtenemos los datos del usuario y contraseña ingresados en los campos
        usuario = self.usuario.get()
        contrasena = self.contrasena.get()

        # Validamos los datos ingresados llamando a la función de verificación de credenciales
        es_valido, error = validate_credentials(usuario, contrasena)

        if not es_valido:
            # Si los datos no son válidos, mostramos un mensaje de error con el motivo
            messagebox.showerror('Registro', error)
            return

        # Si los datos son válidos, intentamos crear la cuenta del usuario llamando a la función del controlador
        cuenta_creada = crear_cuenta(usuario, contrasena)

        if cuenta_creada:
            # Si se creó la cuenta exitosamente, mostramos un mensaje de éxito
            messagebox.showinfo('Registro', 'Registro exitoso')
        else:
            # Si el usuario ya existe, mostramos un mensaje de error
            messagebox.showerror('Registro', 'El usuario ya existe')

    # Constructor de la clase
    def __init__(self):
        # Llamamos al constructor de la clase padre (FormLoginDesigner) para inicializar la interfaz gráfica
        super().__init__()
    