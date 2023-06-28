import tkinter as tk
from tkinter import ttk, messagebox
import util.generic as utl
from forms.login.form_login_designer import FormLoginDesigner
from forms.master.form_master import MasterPanel



class FormLogin(FormLoginDesigner):
    
    def verificar(self):
        if self.usuario.get() == 'admin' and self.contraseña.get() == 'admin':
            messagebox.showinfo('Login', 'Login exitoso')
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror('Login', 'Usuario o contraseña incorrectos')

    def registrar(self):
        pass


    def __init__(self):
        super().__init__() #11:16