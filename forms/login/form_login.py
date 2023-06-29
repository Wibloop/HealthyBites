import tkinter as tk
from tkinter import ttk, messagebox
import util.generic as utl
from forms.login.form_login_designer import FormLoginDesigner
from forms.master.form_master import MasterPanel
from controller.user_controller import iniciar_sesion, crear_cuenta


class FormLogin(FormLoginDesigner):

    def verificar_inicio(self): #-> bool(Funcionando)
        usuario = self.usuario.get()
        contraseña = self.contraseña.get()
        if iniciar_sesion(usuario, contraseña):
            messagebox.showinfo('Login', 'Login exitoso')
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror('Login', 'Usuario o contraseña incorrectos')


    def registrar_usuario(self):
        usuario = self.usuario.get()
        contraseña = self.contraseña.get()
        if crear_cuenta(usuario, contraseña):
            messagebox.showinfo('Registro', 'Registro exitoso')
        else:
            messagebox.showerror('Registro', 'El usuario ya existe')
        

    def __init__(self):
        super().__init__() 
    