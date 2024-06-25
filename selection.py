from tkinter import *
from topV import *
from registroB import *

class Menu(Top):

    def __init__(self, root,titulo, posYUbi, colorFondo):
        super().__init__(root,titulo, posYUbi, colorFondo)

        self.ventana.resizable(0,0)
        self.root = root
        self.selectorZone()
    
    def selectorZone(self):
        self.frameSelector = Frame(self.ventana, width=400, height=350, bg='#fff')
        self.frameSelector.place(relx=0.5, rely=0.5,anchor=CENTER)

        self.titulo = Label(self.frameSelector, text="Menu de selección", fg="#57a1f8", bg="#fff",font=('TKDefaultFont', 16, 'bold'))
        self.titulo.place(relx=0.5, y=20, anchor=CENTER)

        self.toRegist = Button(self.frameSelector, text="Registrar Cliente", height=3, cursor="hand2", bg='#57a1f8', fg='white', border=0,command=self.registrar)
        self.toRegist.place(relx=0.3, rely=0.5, anchor=CENTER)

        self.toApp = Button(self.frameSelector, text="Ver Datos", width=15, height=3, bg='#57a1f8', cursor='hand2', fg='white', border=0)
        self.toApp.place(relx=0.7, rely=0.5, anchor=CENTER)
    
    def registrar(self):
        
        self.registro = RegistroU(self.root, 'Registrar cliente','925x450+450+250','#fff')
        self.registro.setImg('#fff','./assets/login.png', 120, 80)
        self.ventana.destroy()
