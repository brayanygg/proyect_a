from tkinter import *

class Top():
    def __init__(self, root,titulo, posYUbi, colorFondo):

        super().__init__()
        self.ventana = Toplevel(root)
        self.ventana.title(titulo)
        self.ventana.geometry(posYUbi)
        self.ventana.config(bg=colorFondo)