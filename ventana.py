from tkinter import Tk

class Ventana(Tk):
    def __init__(self,title,posYUbi,colorFondo):

        super().__init__()

        self.title(title)
        self.geometry(posYUbi)
        self.config(bg=colorFondo)