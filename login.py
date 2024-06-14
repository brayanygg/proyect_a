from tkinter import *
from inAout import *

root = Tk()

root.title('Login')
root.geometry('925x450+450+250')
root.configure(bg="#fff")
root.resizable(False, False)

img = PhotoImage(file='./assets/login.png')
Label(root, image=img, bg='white').place(x=120, y=80)

frameAutenticador = Frame(root, width=350, height=350, bg='white')

frameAutenticador.place(x=480, y=70)

cabecera = Label(frameAutenticador, text='Iniciar sesión', fg='#57a1f8', bg='white', font=('TKDefaultFont', 23, 'bold'))
cabecera.place(x=55, y=5)

global errorMsg
errorMsg = 0

def autenticar():
    nombre=usuario.get()
    password=contrasena.get()

    if nombre == 'admin' and password == 'admin':
        screen=Toplevel(root)
        screen.title('App')
        screen.geometry('925x450+450+250')
        screen.config(bg='white')

        root.withdraw()

        screen.mainloop()

    else:
        global errorMsg

        errorMsg = Label(frameAutenticador, text='Usuario sin el permiso requerido', fg='red', bg='white')
        errorMsg.place(x='30', y='250')

# entry del nombre de usuario y posicionamiento
usuario = Entry(frameAutenticador, width=31, fg='gray', highlightthickness=0, relief=FLAT, font=('TKDefaultFont', 11))
usuario.place(x=30, y=80)
usuario.insert(0,'Nombre de usuario')
usuario.bind('<FocusIn>', lambda e: dentro(e, "user", usuario, lineaUsuario, errorMsg))
usuario.bind('<FocusOut>',lambda e: fuera(e, "user", usuario, lineaUsuario))

# linea debajo del usernameInput
lineaUsuario = Frame(frameAutenticador,width=295,height=2,bg='gray')
lineaUsuario.place(x=25, y=107)

# entry de la contraseña y posicionamiento
contrasena = Entry(frameAutenticador, width=31, fg='gray', highlightthickness=0, relief=FLAT, font=('TKDefaultFont', 11))
contrasena.place(x=30, y=150)
contrasena.insert(0,'Contraseña')
contrasena.bind('<FocusIn>', lambda e: dentro(e, "pass", contrasena, lineaContra, errorMsg))
contrasena.bind('<FocusOut>', lambda e: fuera(e, "pass", contrasena, lineaContra))

# linea debajo del contraseña input
lineaContra = Frame(frameAutenticador,width=295,height=2,bg='gray')
lineaContra.place(x=25, y=177)

Button(frameAutenticador, width=29, pady=7, text='Verificar', bg='#57a1f8', cursor='hand2', fg='white', border=0, command=autenticar).place(x=45, y=204)

root.mainloop()