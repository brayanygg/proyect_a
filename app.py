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
k=0
clientes = []

while k < 15:

    clientes.append(User('30853248','brayan', 'gafaro', '04141754875', 'romulo', True))

    k = k+1
# user2=User('30853853','stiven', 'gonzales', '04241654275', 'hoyo', False)
# user3=User('30658975', 'samuel','bueno', '04248964785', 'tariba', True)

# clientes = [user1,user2,user3]

class AppMain(Top):

    def __init__(self, root,titulo, posYUbi, colorFondo):
        super().__init__(root,titulo, posYUbi, colorFondo)

        self.ventana.resizable(0, 0)
        self.navBar()
        self.mainContent()

    def navBar(self):
        self.navFrame = Frame(self.ventana,bg="#171a4a")
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

        self.framePrincipal = Frame(self.ventana,bg="#fff")
        self.framePrincipal.pack(side=TOP, fill=BOTH, expand=1)

        self.myCanvas = Canvas(self.framePrincipal, bg='#fff')
        self.myCanvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.myScrollbar = Scrollbar(self.framePrincipal, orient=VERTICAL, command=self.myCanvas.yview)
        self.myScrollbar.pack(side=RIGHT, fill=Y)

        self.myCanvas.configure(yscrollcommand=self.myScrollbar.set)
        self.myCanvas.bind('<Configure>',lambda e: self.myCanvas.configure(scrollregion=self.myCanvas.bbox(ALL)))

        self.frameContenedor = Frame(self.myCanvas)

        self.myCanvas.create_window((0,0), window=self.frameContenedor, anchor=NW)

        self.frameContenedor.columnconfigure(0, weight=2)  
        self.frameContenedor.columnconfigure(1, weight=2)  
        self.frameContenedor.columnconfigure(2, weight=2)  
        self.frameContenedor.columnconfigure(3, weight=2)
        self.frameContenedor.columnconfigure(4, weight=2)  
        self.frameContenedor.columnconfigure(5, weight=2)  
        self.frameContenedor.columnconfigure(6, weight=1)  
        self.frameContenedor.columnconfigure(7, weight=1)

        self.nombreC = Label(self.frameContenedor, text=('Nombre'),font=('TKDefaultFont', 14), bg='#57a1f8', fg='#fff', width=10)
        self.nombreC.grid(column=0,row=0,sticky="nsew")

        self.apellidoC = Label(self.frameContenedor, text=('Apellido'),font=('TKDefaultFont', 14), bg='#57a1f8', fg='#fff', width=10)
        self.apellidoC.grid(column=1,row=0, sticky="nsew")

        self.cedulaC = Label(self.frameContenedor, text=('Cedula'),font=('TKDefaultFont', 14), bg='#57a1f8', fg='#fff', width=10)
        self.cedulaC.grid(column=2,row=0, sticky="nsew")
        
        self.telefonoC = Label(self.frameContenedor, text=('Telefono'),font=('TKDefaultFont', 14), bg='#57a1f8', fg='#fff', width=12)
        self.telefonoC.grid(column=3,row=0,sticky="nsew")

        self.solvenciaC = Label(self.frameContenedor, text=('Solvencia'),font=('TKDefaultFont', 14), bg='#57a1f8', fg='#fff', width=8)
        self.solvenciaC.grid(column=4,row=0,sticky="nsew")

        self.direccionC = Label(self.frameContenedor, text=('Direccion'),font=('TKDefaultFont', 14), bg='#57a1f8', fg='#fff', width=10)
        self.direccionC.grid(column=5,row=0,sticky="nsew")

        self.botonesDuoC = Frame(self.frameContenedor, bg='#57a1f8')
        self.botonesDuoC.grid(column=6, row=0, columnspan=2, sticky=NSEW)

        limite = len(clientes)
        i = 0
        while(i < limite ):
            
            Label(self.frameContenedor, text=(clientes[i].nombre),font=('TKDefaultFont', 12), bg="#fff").grid(column=0,row=i+1,sticky=NSEW, )
            Label(self.frameContenedor, text=(clientes[i].apellido),font=('TKDefaultFont', 12), bg="#fff").grid(column=1,row=i+1, sticky=NSEW, )
            Label(self.frameContenedor, text=(clientes[i].cedula),font=('TKDefaultFont', 12), bg="#fff").grid(column=2,row=i+1, sticky=NSEW, )
            Label(self.frameContenedor, text=(clientes[i].telefono),font=('TKDefaultFont', 12), bg="#fff").grid(column=3,row=i+1,sticky=NSEW, )
            Label(self.frameContenedor, text=('Si'),font=('TKDefaultFont', 12), bg="#fff").grid(column=4,row=i+1,sticky=NSEW, )
            Label(self.frameContenedor, text=(clientes[i].direccion),font=('TKDefaultFont', 12), bg="#fff").grid(column=5,row=i+1,sticky=NSEW, )
            Button(self.frameContenedor,text='Modificar',font=('TKDefaultFont', 10), bg='#2f2c79', fg="#fff", highlightthickness=0, relief=FLAT, cursor="hand2").grid(column=6,row=i+1, pady=(4,0))
            Button(self.frameContenedor,text='Eliminar',font=('TKDefaultFont', 10), bg='#2f2c79',fg="#fff", highlightthickness=0, relief=FLAT, cursor="hand2").grid(column=7,row=i+1, pady=(2,0), padx=(4,0))
            
            i = i+1