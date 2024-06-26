from tkinter import *
from topV import *

class User():
    def __init__(self,cedula, nombre, apellido, telefono, direccion, solvencia):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.solvencia = solvencia

user1=User('30853248','brayan', 'gafaro', '04141754875', 'romulo', True)
user2=User('30853853','stiven', 'gonzales', '04241654275', 'hoyo', False)
user3=User('30658975', 'samuel','bueno', '04248964785', 'tariba', True)

clientes = [user1,user2,user3]

class AppMain(Top):

    def __init__(self, root,titulo, posYUbi, colorFondo):
        super().__init__(root,titulo, posYUbi, colorFondo)

        self.ventana.resizable(1, 1)
        self.navBar()
        self.mainContent()

    def navBar(self):
        self.navFrame = Frame(self.ventana,bg="black")
        self.navFrame.pack(side=TOP,  fill=X)
        
        self.navFrame.columnconfigure(0, weight=9)  # gap column
        self.navFrame.columnconfigure(1, weight=1)  # admin button
        self.navFrame.columnconfigure(2, weight=1)  # reports button
        self.navFrame.columnconfigure(3, weight=9)  # gap column

        Button(self.navFrame,text="Añadir admin",bg='#57a1f8', cursor='hand2', fg='white', highlightthickness=0, relief=FLAT).grid(row=0, column=1, sticky="nsew", padx=5, pady=12)
        Button(self.navFrame,text="Imprimir reportes",bg='#57a1f8', cursor='hand2', fg='white', highlightthickness=0, relief=FLAT).grid(row=0, column=2, sticky="nsew", padx=5, pady=12)

    def mainContent(self):

        self.separador = Frame(self.ventana, bg='#fff', height=5)
        self.separador.pack(fill=X)

        self.mainFrame = Frame(self.ventana, bg='white', padx=5)
        self.mainFrame.pack(fill=X)

        self.mainFrame.columnconfigure(0, weight=2)  
        self.mainFrame.columnconfigure(1, weight=2)  
        self.mainFrame.columnconfigure(2, weight=2)  
        self.mainFrame.columnconfigure(3, weight=2)
        self.mainFrame.columnconfigure(4, weight=2)  
        self.mainFrame.columnconfigure(5, weight=2)  
        self.mainFrame.columnconfigure(6, weight=1)  
        self.mainFrame.columnconfigure(7, weight=1)

        Label(self.mainFrame, text=('Nombre'),font=('TKDefaultFont', 14), bg='#24489C', fg='#fff').grid(column=0,row=0,sticky="nsew")
        Label(self.mainFrame, text=('Apellido'),font=('TKDefaultFont', 14), bg='#24489C', fg='#fff').grid(column=1,row=0, sticky="nsew")
        Label(self.mainFrame, text=('Cedula'),font=('TKDefaultFont', 14), bg='#24489C', fg='#fff').grid(column=2,row=0, sticky="nsew")
        Label(self.mainFrame, text=('Telefono'),font=('TKDefaultFont', 14), bg='#24489C', fg='#fff').grid(column=3,row=0,sticky="nsew")
        Label(self.mainFrame, text=('Solvencia'),font=('TKDefaultFont', 14), bg='#24489C', fg='#fff').grid(column=4,row=0,sticky="nsew")
        Label(self.mainFrame, text=('Direccion'),font=('TKDefaultFont', 14), bg='#24489C', fg='#fff').grid(column=5,row=0,sticky="nsew")
        Frame(self.mainFrame, bg='#24489C').grid(column=6, row=0, columnspan=2, sticky=NSEW)

        Frame(self.mainFrame,height=2,bg='black').grid(column=0, row=1, columnspan=8, sticky=EW)

        Label(self.mainFrame, text=('brayan'),font=('TKDefaultFont', 12)).grid(column=0,row=2,sticky="nsew")
        Label(self.mainFrame, text=('gafaro'),font=('TKDefaultFont', 12)).grid(column=1,row=2, sticky="nsew")
        Label(self.mainFrame, text=('30853248'),font=('TKDefaultFont', 12)).grid(column=2,row=2, sticky="nsew")
        Label(self.mainFrame, text=('04141754875'),font=('TKDefaultFont', 12)).grid(column=3,row=2,sticky="nsew")
        Label(self.mainFrame, text=('Si'),font=('TKDefaultFont', 12)).grid(column=4,row=2,sticky="nsew")
        Label(self.mainFrame, text=('romulo'),font=('TKDefaultFont', 12)).grid(column=5,row=2,sticky="nsew")
        Button(self.mainFrame,text="Modificar",font=('TKDefaultFont', 10), bg='yellow', highlightthickness=0, relief=FLAT).grid(column=6,row=2)
        Button(self.mainFrame,text="Eliminar",font=('TKDefaultFont', 10), bg='red', highlightthickness=0, relief=FLAT).grid(column=7,row=2)