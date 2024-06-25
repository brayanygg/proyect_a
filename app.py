from tkinter import *
from topV import *

class AppMain(Top):

    def __init__(self, root,titulo, posYUbi, colorFondo):
        super().__init__(root,titulo, posYUbi, colorFondo)

        self.ventana.resizable(False, False)