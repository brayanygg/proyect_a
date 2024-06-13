from tkinter import *
from tkinter import messagebox

root = Tk()

root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

img = PhotoImage(file='./assets/login.png')
Label(root, image=img, bg='white').place(x=120, y=80)

frameAutenticador = Frame(root, width=350, height=350, bg='white')

frameAutenticador.place(x=480, y=70)

cabecera = Label(frameAutenticador, text='Iniciar sesión', fg='#57a1f8', bg='white', font=('TKDefaultFont', 23, 'bold'))
cabecera.place(x=55, y=5)

def autenticar():
    nombre=usuario.get()
    password=contrasena.get()

    if nombre == 'admin' and password == 'admin':
        print('acceso consedido rango admin')
    else:
        print('Error')

def dentro(e):
    nombre = usuario.get()
    if nombre == "Nombre de usuario":
        usuario.delete(0, 'end')
        usuario.configure(fg="black")
        lineaUsuario.configure(bg="black")

def fuera(e):
    nombre = usuario.get()
    if nombre == "":
        usuario.insert(0,'Nombre de usuario')
        usuario.configure(fg="gray")
        lineaUsuario.configure(bg="gray")

usuario = Entry(frameAutenticador, width=31, fg='gray', highlightthickness=0, relief=FLAT, font=('TKDefaultFont', 11))
usuario.place(x=30, y=80)
usuario.insert(0,'Nombre de usuario')
usuario.bind('<FocusIn>', dentro)
usuario.bind('<FocusOut>', fuera)

# linea debajo del usernameInput
lineaUsuario = Frame(frameAutenticador,width=295,height=2,bg='gray')
lineaUsuario.place(x=25, y=107)


def dentro(e):
    contra = contrasena.get()
    if contra == "Contraseña":
        contrasena.delete(0, 'end')
        contrasena.configure(fg="black")
        lineaContra.config(bg="black")

def fuera(e):
    contra = contrasena.get()
    if contra == "":
        contrasena.insert(0,'Contraseña')
        contrasena.configure(fg="gray")
        lineaContra.configure(bg="gray")

contrasena = Entry(frameAutenticador, width=31, fg='gray', highlightthickness=0, relief=FLAT, font=('TKDefaultFont', 11))
contrasena.place(x=30, y=150)
contrasena.insert(0,'Contraseña')
contrasena.bind('<FocusIn>', dentro)
contrasena.bind('<FocusOut>', fuera)

# linea debajo del contraseña input
lineaContra = Frame(frameAutenticador,width=295,height=2,bg='gray')
lineaContra.place(x=25, y=177)

Button(frameAutenticador, width=29, pady=7, text='Verificar', bg='#57a1f8', cursor='hand2', fg='white', border=0, command=autenticar).place(x=45, y=204)

root.mainloop()