def dentro(e, zone, contenido, linea, errorMsg):

    if contenido.get() == zone:
        contenido.delete(0, 'end')
        contenido.configure(fg="black")

    if zone == "Contraseña":

            contenido.configure(show="*")
            
    linea.configure(bg="black")
    
    if errorMsg:
        errorMsg.destroy()

def fuera(e, zone, contenido, linea):

    if contenido.get() == "":
        contenido.insert(0,zone)
        contenido.configure(fg="gray")

        if zone == "Contraseña":
            contenido.configure(show="")

    linea.configure(bg="gray")