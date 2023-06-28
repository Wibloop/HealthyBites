from PIL import ImageTk, Image
from tkinter import ttk, messagebox

def leer_imagen(path, size): 
        return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ANTIALIAS))  
        #Esto sirve para leer una imagen y redimensionarla


def centrar_ventana(ventana, aplicacion_ancho, aplicacion_largo):    
    pantall_ancho = ventana.winfo_screenwidth()
    pantall_largo = ventana.winfo_screenheight()
    posicion_x = int((pantall_ancho/2) - (aplicacion_ancho/2))
    posicion_y = int((pantall_largo/2) - (aplicacion_largo/2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{posicion_x}+{posicion_y}")
    #Esto sirve para centrar la ventana


