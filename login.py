from tkinter import *
from inAout import *
from ventana import *
from registroB import *
from selection import *
from app import *

global errorMsg
errorMsg = 0

class Login(Ventana):

    def __init__(self,title,posYUbi,colorFondo,isResizableX,isResizableY):
        super().__init__(title,posYUbi,colorFondo)
        
        self.resizable(isResizableX,isResizableY)
    def setImg(self, colorFondo, path, posX, posY):
        
        self.img = PhotoImage(file=path)

        Label(self, image=self.img, bg=colorFondo).place(x=posX, y=posY)

    def autenticar(self):
        # self.nombre = self.usuario.get()
        # self.password = self.contrasena.get()

        # if self.nombre == 'admin' and self.password == 'admin':

        #    self.menu = Menu(self,'Menu','550x450+650+250','#fff')
            self.app = AppMain(self, 'app','925x450+450+250','#fff')
        #     self.withdraw()

        # else:
        #     global errorMsg

        #     errorMsg = Label(self.frameAutenticador, text='Usuario sin el permiso requerido', fg='red', bg='white')
        #     errorMsg.place(x='30', y='250')

    def autenticationFrame(self):
        
        self.frameAutenticador = Frame(self, width=350, height=350, bg='white')
        self.frameAutenticador.place(x=480, y=70)

        self.cabecera = Label(self.frameAutenticador, text='Iniciar sesión', fg='#57a1f8', bg='white', font=('TKDefaultFont', 23, 'bold'))
        self.cabecera.place(x=55, y=5)

        # entry del nombre de usuario y posicionamiento
        self.usuario = Entry(self.frameAutenticador, width=31, fg='gray', highlightthickness=0, relief=FLAT, font=('TKDefaultFont', 11))
        self.usuario.place(x=30, y=80)
        self.usuario.insert(0,'Nombre de usuario ')
        self.usuario.bind('<FocusIn>', lambda e: dentro(e, "Nombre de usuario ", self.usuario, self.lineaUsuario, errorMsg))
        self.usuario.bind('<FocusOut>',lambda e: fuera(e, "Nombre de usuario ", self.usuario, self.lineaUsuario))

        # linea debajo del usernameInput
        self.lineaUsuario = Frame(self.frameAutenticador,width=295,height=2,bg='gray')
        self.lineaUsuario.place(x=25, y=107)

        # entry de la contraseña y posicionamiento
        self.contrasena = Entry(self.frameAutenticador, width=31, fg='gray', highlightthickness=0, relief=FLAT, font=('TKDefaultFont', 11))
        self.contrasena.place(x=30, y=150)
        self.contrasena.insert(0,'Contraseña ')
        self.contrasena.bind('<FocusIn>', lambda e: dentro(e, "Contraseña ", self.contrasena, self.lineaContra, errorMsg))
        self.contrasena.bind('<FocusOut>', lambda e: fuera(e, "Contraseña ", self.contrasena, self.lineaContra))

        # linea debajo del contraseña input
        self.lineaContra = Frame(self.frameAutenticador,width=295,height=2,bg='gray')
        self.lineaContra.place(x=25, y=177)

        Button(self.frameAutenticador, width=29, pady=7, text='Verificar', bg='#57a1f8', cursor='hand2', fg='white', border=0, command=self.autenticar).place(x=45, y=204)


miLogin = Login("Login", "925x450+450+250", "#fff",0,0)

miLogin.setImg('#fff','./assets/login.png', 120, 80)

miLogin.autenticationFrame()

miLogin.mainloop()