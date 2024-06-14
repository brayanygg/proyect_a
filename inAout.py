def dentro(e, zone, contenido, linea, errorMsg):

    if zone == "user":

        if contenido.get() == "Nombre de usuario":
            contenido.delete(0, 'end')
            contenido.configure(fg="black")
            linea.configure(bg="black")
    elif zone == "pass":

        if contenido.get() == "Contraseña":
            contenido.delete(0, 'end')
            contenido.configure(fg="black", show="*")
            linea.configure(bg="black")

    if errorMsg:
        errorMsg.destroy()

def fuera(e, zone, contenido, linea):
    if zone == "user":

        if contenido.get() == "":
            contenido.insert(0,'Nombre de usuario')
            contenido.configure(fg="gray")
            linea.configure(bg="gray")

    elif zone == "pass":

        if contenido.get() == "":
            contenido.insert(0,'Contraseña')
            contenido.configure(fg="gray", show="")
            linea.configure(bg="gray")