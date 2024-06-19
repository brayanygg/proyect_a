from tkinter import *
from topV import *

class Menu(Top):
        def __init__(self, root,titulo, posYUbi, colorFondo, bWindow=False):
            super().__init__(root,titulo, posYUbi, colorFondo, bWindow=False)

            self.ventana.resizable(False, False)
            self.registrationFrame()

        def setImg(self, colorFondo, path, posX, posY):
        
            self.img = PhotoImage(file=path)
        
            Label(self.ventana, image=self.img, bg=colorFondo).place(x=posX, y=posY)

        def registrationFrame(self):
             
            self.frameRegist = Frame(self.ventana, width=400, height=350, bg='red')
            self.frameRegist.place(x=460, y=70)

            self.titulo = Label(self.frameRegist, text='Registrarse', fg='#57a1f8', bg='white', font=('TKDefaultFont', 23, 'bold'))
            self.titulo.place(x=95, y=5)

            # entry del nombre y posicionamiento
            self.nombre = Entry(self.frameRegist, width=20, fg='gray', highlightthickness=0, relief=FLAT, font=('TKDefaultFont', 11))
            self.nombre.place(x=10, y=80)
            self.nombre.insert(0,'Nombre')
            # self.nombre.bind('<FocusIn>', lambda e: dentro(e, "user", self.nombre, self.lineaUsuario, errorMsg))
            # self.nombre.bind('<FocusOut>',lambda e: fuera(e, "user", self.nombre, self.lineaUsuario))

            # linea debajo del usernameInput
            self.lineaNombre = Frame(self.frameRegist,width=190,height=2,bg='gray')
            self.lineaNombre.place(x=8, y=107)

            # entry del nombre y posicionamiento
            self.nombre = Entry(self.frameRegist, width=20, fg='gray', highlightthickness=0, relief=FLAT, font=('TKDefaultFont', 11))
            self.nombre.place(x=210, y=80)
            self.nombre.insert(0,'Apellido')

            # linea debajo del usernameInput
            self.lineaNombre = Frame(self.frameRegist,width=190,height=2,bg='gray')
            self.lineaNombre.place(x=208, y=107)

            