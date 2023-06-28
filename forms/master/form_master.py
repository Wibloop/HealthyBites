import tkinter as tk
import util.generic as utl

class MasterPanel: 
    
    def __init__(self):   
             
        self.ventana = tk.Tk()                             
        self.ventana.title('HealthyBites')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        #Esto sirve para que la ventana se abra en pantalla completa
        self.ventana.config(bg='#fff0d3')
        self.ventana.resizable(width=0, height=0)            
        
        logo =utl.leer_imagen('./static/imagenes/logo.png', (200, 200))
        label = tk.Label(self.ventana, image=logo,bg='#fff0d3' )
        label.place(x=0,y=0,relwidth=1, relheight=1)
        #Esto sirve para que la imagen se adapte al tamaño del label
        #label en español es etiqueta

        
        self.ventana.mainloop()
        #Esto sirve para que la ventana se mantenga abierta