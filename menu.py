from tkinter import *
from topV import *
from inAout import *

class Menu(Top):
        def __init__(self, root,titulo, posYUbi, colorFondo, bWindow=False):
            super().__init__(root,titulo, posYUbi, colorFondo, bWindow=False)

            self.ventana.resizable(False, False)
            self.registrationFrame()

        def setImg(self, colorFondo, path, posX, posY):
        
            self.img = PhotoImage(file=path)
        
            Label(self.ventana, image=self.img, bg=colorFondo).place(x=posX, y=posY)

        def registrationFrame(self):
             
            self.frameRegist = Frame(self.ventana, width=400, height=350, bg='white')
            self.frameRegist.place(x=460, y=70)

            self.titulo = Label(self.frameRegist, text='Registrarse', fg='#57a1f8', bg='white', font=('TKDefaultFont', 23, 'bold'))
            self.titulo.place(x=95, y=5)

            # entry del nombre y posicionamiento
            self.nombreEntry = Entry(self.frameRegist, width=20, fg='gray', highlightthickness=0, relief=FLAT, font=('TKDefaultFont', 11))
            self.nombreEntry.place(x=10, y=80)
            self.nombreEntry.insert(0,'Ingresar Nombre')
            self.nombreEntry.bind('<FocusIn>', lambda e: dentro(e, "Ingresar Nombre", self.nombreEntry, self.lineaNombre, 0))
            self.nombreEntry.bind('<FocusOut>',lambda e: fuera(e, "Ingresar Nombre", self.nombreEntry, self.lineaNombre))

            # linea debajo del usernameInput
            self.lineaNombre = Frame(self.frameRegist,width=190,height=2,bg='gray')
            self.lineaNombre.place(x=8, y=107)

            # entry del apellido y posicionamiento
            self.apellidoEntry = Entry(self.frameRegist, width=20, fg='gray', highlightthickness=0, relief=FLAT, font=('TKDefaultFont', 11))
            self.apellidoEntry.place(x=210, y=80)
            self.apellidoEntry.insert(0,'Ingresar Apellido')
            self.apellidoEntry.bind('<FocusIn>', lambda e: dentro(e, "Ingresar Apellido", self.apellidoEntry, self.lineaApellido, 0))
            self.apellidoEntry.bind('<FocusOut>',lambda e: fuera(e, "Ingresar Apellido", self.apellidoEntry, self.lineaApellido))

            # linea debajo del apellidoInput
            self.lineaApellido = Frame(self.frameRegist,width=190,height=2,bg='gray')
            self.lineaApellido.place(x=208, y=107)

            #entry de cedula y posicionamiento
            self.cedulaEntry = Entry(self.frameRegist, width=20, fg='gray', highlightthickness=0, relief=FLAT, font=('TKDefaultFont', 11))
            self.cedulaEntry.place(x=10, y=130)
            self.cedulaEntry.insert(0,'Ingresar Cedula')
            self.cedulaEntry.bind('<FocusIn>', lambda e: dentro(e, "Ingresar Cedula", self.cedulaEntry, self.lineaCedula, 0))
            self.cedulaEntry.bind('<FocusOut>',lambda e: fuera(e, "Ingresar Cedula", self.cedulaEntry, self.lineaCedula))

            #linea debajo de cedulainput
            self.lineaCedula = Frame(self.frameRegist,width=190,height=2,bg='gray')
            self.lineaCedula.place(x=8, y=157)

            #entry de tlf y posicionamiento
            self.tlfEntry = Entry(self.frameRegist, width=20, fg='gray', highlightthickness=0, relief=FLAT, font=('TKDefaultFont', 11))
            self.tlfEntry.place(x=210, y=130)
            self.tlfEntry.insert(0,'Ingresar telefono')
            self.tlfEntry.bind('<FocusIn>', lambda e: dentro(e, "Ingresar telefono", self.tlfEntry, self.lineaTlf, 0))
            self.tlfEntry.bind('<FocusOut>',lambda e: fuera(e, "Ingresar telefono", self.tlfEntry, self.lineaTlf))

            #linea debajo de tlf
            self.lineaTlf = Frame(self.frameRegist,width=190,height=2,bg='gray')
            self.lineaTlf.place(x=208, y=157)

            #entry de direccion y posicionamiento
            self.dirEntry = Entry(self.frameRegist, width=42, fg='gray', highlightthickness=0, relief=FLAT, font=('TKDefaultFont', 11))
            self.dirEntry.place(x=10, y=180)
            self.dirEntry.insert(0,'Ingresar dirección')
            self.dirEntry.bind('<FocusIn>', lambda e: dentro(e, "Ingresar dirección", self.dirEntry, self.lineaDir, 0))
            self.dirEntry.bind('<FocusOut>',lambda e: fuera(e, "Ingresar dirección", self.dirEntry, self.lineaDir))

            # linea debajo de direccion
            self.lineaDir = Frame(self.frameRegist,width=390,height=2,bg='gray')
            self.lineaDir.place(x=8, y=207)

            #Zona de seleccion genero
            self.tituloGenero = Label(self.frameRegist, text='Seleccione el genero', bg="#fff")
            self.tituloGenero.place(x=42, y=230)

            self.generoSeleccionado = StringVar()

            self.botonMasculino = Radiobutton(self.frameRegist, variable=self.generoSeleccionado, value="M", text="Masculino",bg="#fff",highlightthickness=0, relief=FLAT, font=('TKDefaultFont', 11))
            self.botonFemenino = Radiobutton(self.frameRegist, variable=self.generoSeleccionado, value="F", text="Femenino",bg="#fff",highlightthickness=0, relief=FLAT, font=('TKDefaultFont', 11))

            self.botonMasculino.place(x=8, y=260)
            self.botonFemenino.place(x=115, y=260)

            Button(self.frameRegist, width=15, pady=7, text='Enrolar huella', bg='#57a1f8', cursor='hand2', fg='white', border=0).place(x=247, y=235)

            Button(self.frameRegist, width=23, pady=7, text='Enviar', bg='#57a1f8', cursor='hand2', fg='white', border=0).place(x=100, y=298)