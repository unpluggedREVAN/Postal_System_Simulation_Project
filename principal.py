#Elaborado por: Needler Bonilla Serrano
#               Jose Pablo Agüero Mora
#Fecha de Creación: 11/11/2021 6:00pm 
#Fecha de última Modificación: 29/11/2021 00:00pm
#Versión: 3.9.6

###################### Sección de notas importantes ########################
#1) Se decidió generar los nombre de los clientes con el formato ocupando  #
#   tres espacios en una tupla.                                            #
#                                                                          #
#2) En la creación del archivo pdf se utilizó el segundo nombre del        #
#   cliente como nombre del archivo .pdf                                   #
#   -Se dió por entendido que en el ejemplo ""                             #
#                                                                          #
#3) Las cédulas 8 y 9 se dirijirán a la provincia de San José por          #
#   solicitud de la profesora en la ultima reunión.                        #
#                                                                          #
#4)                                                                        #
#                                                                          #
#5)                                                                        #
############################################################################

# Importación de librerías
from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
from funciones import *
from archivos import *

#------------------------------Funciones especiales--------------------------------
def mensajeFrases (tit, cont):
    """
    Funcion: Muestra un mensaje respectivo.
    Entrada: Parámetro - tit, cont.
    Salida: Muestra el mensaje.
    """
    totalFrases = Toplevel()
    totalFrases.minsize(500,150)
    totalFrases.resizable(width=NO,height=NO)
    totalFrases.title(tit)
    totalFrases.config( bg= "#455A64",cursor="circle")

    #Etiquetas
    mensaje = Label(totalFrases, text=cont)
    mensaje.config(font=('Arial 12'))
    mensaje.config(fg="white",bg="#455A64")
    mensaje.place(x=20,y=75)
    
def CargarImagen(nombre):  
    root = os.path.join('imagenes',nombre)#Nombre de carpeta de imagenes
    image = tk.PhotoImage(file=root)
    return image

#-----------------------------Funciones especiales----------------------------------
def VentanaPrincipal(x, y):
    """
    Funcion: Despliega la interfaz gráfica del menú principal.
    Entrada: Parámetro - y, estado de los botones.
    Salida: N/D
    """
    #ventana principal
    canvas=Canvas(ventana,width= 546,height=496,bg="#455A64")
    canvas.place(x=0,y=0)

    #Etiquetas
    canvas.create_text((275),50,
                       fill="white",
                       font= "Arial 18 bold",
                       text="Correos de Costa Rica")
    #Botones
    bCargar = Button(canvas,
                     text = "Cargar Códigos Postales",
                     command = lambda:[cargaCodAux (ventana)],state = tk.NORMAL).place(x=100,y=100) #1

    bRegistrar = Button(canvas,
                        text = "Registrar Clientes",
                        command = registrarClientes, state = tk.NORMAL).place(x=330,y=100) #2

    bCrear = Button(canvas,
                    text = "Crear Clientes",
                    command= crearClientes, state = x).place(x=130,y=180) #3

    bGenerar = Button(canvas,
                      text = "Generar Etiqueta",
                      command= generaEtiqueta, state = y).place(x=330,y=180) #4

    bEnviar = Button(canvas,
                     text = "Enviar Correo",
                     command= enviaCorreo, state = y).place(x=130,y=260) #5

    bExportar = Button(canvas,
                       text = "Exportar Códigos",command= exportarCodigos, state = x ).place(x=330,y=260) #6

    bReportes = Button(canvas,
                       text = "    Reportes    ",command= reportes, state = y).place(x=130,y=340) #7
    
    bCredenciales = Button(canvas,
                           text = "Credenciales",
                           command= credencialAutor,state = tk.NORMAL).place(x=340,y=340) #8

    bSalir = Button(canvas,
                    text = "      Salir      ",
                    command = lambda: salirPrincipal(ventana),state = tk.NORMAL).place(x=250,y=420) #9

def salirPrincipal(ventana):
    """
    Funcion: Cierra el menú principal / termina el programa.
    Entrada: Parámetro - ventana.
    Salida: N/D
    """
    ventana.destroy()

#---------------------------Cargar Códigos Postales----------------------------------------
def cargaCodAux (ventana): #1
    """
    Funcion: Valida que el archivo infoCodigos exista en la maquina y la refresca la ventana principal.
    Entrada: Parámetro ventana (Ventana Principal)
    Salida: Llamado a función cargaCodPostal.
    """
    if existeArchivo("infoCodigos")==False:
        cargaCodPostal ()
    else:
        tit = "Notificación"
        cont = "El archivo infoCodigos ya existe en el sistema."
        mensajeFrases (tit, cont)
        
def cargaCodPostal (): #1.1
    """
    Funcion: Llama a la función encargada de generar el pdf con los datos solicitados y retroalimenta.
    Entrada: N/D
    Salida: Mensaje de retroalimentación y creación de documento pdf.
    """
    try:
        infoCodigos = leeArchivo ()

        if existeArchivo("BD") == True:
            y = tk.NORMAL
        else:
            y = tk.DISABLED
        
        VentanaPrincipal (tk.NORMAL, y)
        tit = "Notificación"
        cont = "El archivo infoCodigos se creó satisfactoriamente."
        mensajeFrases (tit, cont)
    except:
        tit = "Notificación"
        cont = "No existe archivo txt en la carpeta actual."
        mensajeFrases (tit, cont)
    
#-------------------------------Registrar Clientes---------------------------------------------
def registrarClientes (): #2
    """
    Funcion: Ventana donde se ingresa los datos necesarios para registrar un solo cliente a la BD.
    Entrada: N/D
    Salida: Ventana con los datos solicitadosa.
    """
    reCliente = Toplevel()
    reCliente.minsize(500, 300)
    reCliente.resizable(width=NO,height=NO)
    reCliente.title("Registrar Clientes")
    reCliente.config( bg= "#455A64")

    #Etiquetas
    Lmensaje = Label(reCliente, text="Complete lo solicitado para Registrar al Cliente a la base de datos.")
    Lmensaje.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lmensaje.place(x=20,y=20)
    
    Lcedula = Label (reCliente,text = "Cédula----------------------------------------------")
    Lcedula.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lcedula.place(x=18,y=70)

    Lnombre = Label (reCliente,text = "Nombre Completo------------------------------")
    Lnombre.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lnombre.place(x=18,y=100)

    Lespecifica = Label (reCliente,text = "Dirección Específica---------------------------")
    Lespecifica.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lespecifica.place(x=18,y=130)

    Lgeneral = Label (reCliente,text = "Dirección General-------------------------------")
    Lgeneral.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lgeneral.place(x=18,y=160)

    Lpostal = Label (reCliente,text = "Código Postal------------------------------------")
    Lpostal.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lpostal.place(x=18,y=190)

    Lcorreo = Label (reCliente,text = "Correo Electrónico------------------------------")
    Lcorreo.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lcorreo.place(x=18,y=220)
    
    #Cuadros de texto
    cedula = ttk.Entry(reCliente,width=25)
    cedula.place(x=320, y=70)
    
    nombre = ttk.Entry(reCliente,width=25)
    nombre.place(x=320, y=100)
    
    dirEspecifica = ttk.Entry(reCliente,width=25)
    dirEspecifica.place(x=320, y=130)
    
    dirGeneral = ttk.Entry(reCliente,width=25)
    dirGeneral.place(x=320, y=160)
    
    codPostal = ttk.Entry(reCliente,width=25)
    codPostal.place(x=320, y=190)
    
    correo = ttk.Entry(reCliente,width=25)
    correo.place(x=320, y=220)

    #Botón
    registrar=Button ( reCliente,
                   text="Registrar Cliente",
                   command = lambda:[validaReClientes (reCliente,
                                                           cedula.get(),
                                                           nombre.get(),
                                                           dirEspecifica.get(),
                                                           dirGeneral.get(),
                                                           codPostal.get(),
                                                           correo.get() ) ] ).place(x=200,y=250)
    reCliente.mainloop()

def validaReClientes (reCliente, cedula, nombre, especifica, general, postal, correo ): #<<<<<<--------------------------
    """
    Funcion: Función de validación ligada a los datos registrados en la ventana de registrarClientes.
    Entrada: Parámetros reCliente (nombre ventana), cedula, nombre, especifica (dirección), general (dirección), postal (codigo) y correo
    Salida: Mensaje de retroalientación y llamado a la función insertarCliente.
    """
    if existeArchivo("infoCodigos") == True:
        x = tk.NORMAL
    else:
        x = tk.DISABLED
    if  cedula !="" and nombre !="" and especifica !="" and general !="" and postal !="" and correo !="":
        if validaCedula(cedula) == True:
            if validaNombre(nombre) == True:
                if validaDireccionEsp (especifica) == True:
                    if validaDireccionGen (general) == True:
                        if validaCodigoPostal(postal) == True:
                            if validaCorreo(correo) == True:
                                if existeArchivo("BD") == True:
                                    if existeCedula(cedula) == False:
                                        if existeCorreo(correo) == False:
                                            if valInicialPostal(cedula, postal) == True:
                                                nombre=tuple(nombre.split())
                                                general= general.split(",")
                                                instertarCliente(cedula, nombre, especifica, general, postal, correo)
                                                reCliente.destroy () #Cambiar colo emergente
                                                VentanaPrincipal (x, tk.NORMAL)
                                                tit = "Notificación"
                                                cont = "Se guardó el cliente correctamente en la BD."
                                                mensajeFrases (tit, cont)
                                            else:
                                                tit = "Notificación"
                                                cont = "El primer dígito de la cédula y el código deben coincidir."
                                                mensajeFrases (tit, cont)
                                        else:
                                            tit = "Notificación"
                                            cont = "Ya existe un usuario registrado con este correo."
                                            mensajeFrases (tit, cont)
                                    else:
                                        tit = "Notificación"
                                        cont = "Ya existe un usuario registrado con esta cédula."
                                        mensajeFrases (tit, cont)
                                else:
                                    if valInicialPostal(cedula, postal) == True:
                                        nombre=tuple(nombre.split())
                                        general= general.split(",")
                                        instertarCliente(cedula, nombre, especifica, general, postal, correo)
                                        reCliente.destroy () #Cambiar colo emergente
                                        VentanaPrincipal (x, tk.NORMAL)
                                        tit = "Notificación"
                                        cont = "Se guardó el cliente correctamente en la BD."
                                        mensajeFrases (tit, cont)
                                    else:
                                        tit = "Notificación"
                                        cont = "El primer dígito de la cédula y el código deben coincidir."
                                        mensajeFrases (tit, cont)
                            else:
                                tit = "Formato incorrecto"
                                cont = "Debe ingresar un correo válido."
                                mensajeFrases (tit, cont)
                        else:
                            tit = "Formato incorrecto"
                            cont = "Debe ingresar un codigo postal valido."
                            mensajeFrases (tit, cont)
                    else:
                        tit = "Formato incorrecto"
                        cont = "Debe ingresar  una dirección general valida."
                        mensajeFrases (tit, cont)
                else:
                    tit = "Formato incorrecto"
                    cont = "Debe ingresar una dirección específica valida."
                    mensajeFrases (tit, cont)  
            else:
                tit = "Formato incorrecto"
                cont = "Debe ingresar un nombre valida."
                mensajeFrases (tit, cont)
        else:
            tit = "Formato incorrecto"
            cont = "Debe ingresar una cédula valida."
            mensajeFrases (tit, cont)
    else:
        tit = "Formato incorrecto"
        cont = "Se deben completar todos los datos."
        mensajeFrases (tit, cont)   

#------------------------------------Crear Clientes-----------------------------------------
def crearClientes (): #3
    """
    Funcion: Ventana que genera una cantidad de clientes determinada por un número ingresado.
    Entrada:  N/D
    Salida: Ventana con los datos a solicitar y llamado a función creaClienteAux con botón.
    """
    creaClientes = Toplevel()
    creaClientes.minsize(500, 100)
    creaClientes.resizable(width=NO,height=NO)
    creaClientes.title("Crear Clientes")
    creaClientes.config( bg= "#455A64")

    #Etiquetas
    Lmensaje = Label(creaClientes, text="Ingrese la cantidad de clientes que deséa crear y agregar.")
    Lmensaje.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lmensaje.place(x=40,y=20)

    #Cuadro de Texto
    cantidad = ttk.Entry(creaClientes,width=25)
    cantidad.place(x=170, y=70)
    
    crear=Button ( creaClientes,
                   text="Crear Cliente",
                   command = lambda:[creaClienteAux (creaClientes, cantidad.get() ) ] ).place(x=210,y=130)
    creaClientes.mainloop()

def verificaNum(cantidad):
    """
    Funcion: Valida que la cantidad ingresada esté entre los parámetros esperados (num >0, num = int)
    Entrada: Parámetro cantidad (cantidad de clientes a crear)
    Salida: Retorno de Flags o banderas según el caso.
    """
    try:
        num = int(cantidad)
        if num > 0:
            return True
        else:
            return False
    except:
        return False

def creaClienteAux (creaClientes,cantidad):
    """
    Funcion: Revisa que la cantidad de clientes cumpla con el formato solicitada y crea los clientes retroalimentando.
    Entrada: Parámetros  creaClientes (Ventana) y cantidad.
    Salida: Llamado a función y mensaje de retroalimentación.
    """
    if verificaNum(cantidad) == True:
        cantidad= int(cantidad)
        cicloGeneraCliente (cantidad)
        
        if existeArchivo("infoCodigos") == True:
            x = tk.NORMAL
        else:
            x = tk.DISABLED
        
        VentanaPrincipal (x, tk.NORMAL)
        creaClientes.destroy()
        tit = "Notificación"
        cont = "Se han registrado los clientes satisfactoriamente."
        mensajeFrases (tit, cont)
    else:
        tit = "Formato incorrecto"
        cont = "Debe ingresar un número entero positivo"
        mensajeFrases (tit, cont)

#---------------------------------Generar Etiqueta------------------------------------------
def cambiaDirec(dirGen):
    """
    Funcion: Convierte el contenido de en un string y lo acomoda en una lista.
    Entrada: Parámetro dirGen
    Salida: Retorno de valor posicional de la lista.
    """
    final= ""
    for elemento in dirGen:
        final += elemento + ", "
    return final [:-2]

def determinaSeleccion(pcliente):
    """
    Funcion: Re-acomoda la lista dentro de la BD en tiempo real para ser usada para generar el archivo pdf
    Entrada: Parámetro pcliente
    Salida: Retorno de los contenidos de las listas sub divididas.
    """
    bd = lee("BD")
    cedula = pcliente[:11]
    for elemento in bd:
        actual = elemento.indicaCedula()
        if cedula == actual:
            dirEsp = elemento.indicaDirEsp()
            dirGen = elemento.indicaDirGen()
            postal = elemento.indicaPostal()
    dirGenFinal = cambiaDirec(dirGen)
    return dirEsp, dirGenFinal, postal

def finalizaNombre(nombre):
    """
    Funcion: Toma el parámetro y elimina los espacios sub dividiendolo.
    Entrada: Parámetro nombre.
    Salida: Retorna el parámetro nombre en string sin comillas.
    """
    final = ""
    for elemento in nombre:
        final += elemento + " "
    return final.title()[:-1]
        
def genSeleccionEt():
    """
    Funcion: Genera un valor de la lista general con la cedula y nombre en una sola posición.
    Entrada: N/D
    Salida: Retorna una tupla con los datos cédula y nombre del cliente.
    """
    nueva = []
    bd = lee("BD")
    for objeto in bd:
        nombre = objeto.indicaNombre()
        nombre2 = finalizaNombre(nombre)
        cedula = objeto.indicaCedula()
        final = cedula + " - " + nombre2
        nueva.append(final)
    return tuple(nueva)


def generaEtiqueta (): #4
    """
    Funcion: Ventana que solicita ingreso de datos para generar el archivo pdf.
    Entrada: N/D
    Salida: Ventana con los datos a solicitar y llamado a una función auxiliar.
    """
    genEtiqueta = Toplevel()
    genEtiqueta.minsize(500, 260)
    genEtiqueta.resizable(width=NO,height=NO)
    genEtiqueta.title(" Generar Etiquetas")
    genEtiqueta.config( bg= "#455A64")

    #Etiquetas
    Lmensaje = Label(genEtiqueta, text="Complete lo solicitado para generar una etiqueta en un PDF.")
    Lmensaje.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lmensaje.place(x=20,y=20)

    Lnombre = Label (genEtiqueta,text = "Nombre Completo--------------------------")
    Lnombre.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lnombre.place(x=18,y=70)

    Lespecifica = Label (genEtiqueta,text = "Dirección Específica-----------------")
    Lespecifica.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lespecifica.place(x=18,y=100)

    Lgeneral = Label (genEtiqueta,text = "Dirección General---------------------")
    Lgeneral.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lgeneral.place(x=18,y=130)

    Lpostal = Label (genEtiqueta,text = "Código Postal--------------------------")
    Lpostal.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lpostal.place(x=18,y=160)

    def on_combobox_select(event):
        """
        Funcion: Establece la conexión para que las frases dependan de la categoría.
        Entrada: Parámetro - event.
        Salida: Cambia los elementos de la segunda caja según la primera.
        """
        dirEspecifica.config(text=determinaSeleccion(nombre.get())[0])
        dirGeneral.config(text=determinaSeleccion(nombre.get())[1])
        codPostal.config(text=determinaSeleccion(nombre.get())[2])
    
    #Cuadros de Selección
    clientes=genSeleccionEt ()
    nombre=ttk.Combobox (genEtiqueta, width="30", state="readonly", values=clientes)
    nombre. place (x=290,y=70)
    nombre.bind("<<ComboboxSelected>>", on_combobox_select)

    #Cuadros de texto
    
    dirEspecifica = Label (genEtiqueta)
    dirEspecifica.config(font=('Arial 12'),fg="white",bg="#455A64")
    dirEspecifica.place(x=260,y=100)

    dirGeneral = Label (genEtiqueta)
    dirGeneral.config(font=('Arial 12'),fg="white",bg="#455A64")
    dirGeneral.place(x=260,y=130)

    codPostal = Label (genEtiqueta)
    codPostal.config(font=('Arial 12'),fg="white",bg="#455A64")
    codPostal.place(x=260,y=160)

    #Botón
    registrar=Button ( genEtiqueta,
                   text="Generar PDF",
                   command = lambda:[validaGenEtiq (genEtiqueta,
                                                           nombre.get() ) ] ).place(x=200,y=220)
    genEtiqueta.mainloop()

def tomaDatos(nombre):
    """
    Funcion:Toma la cedula y el nombre para extraer los datos restantes para generar la etiqueta.
    Entrada: Parámetro nombre.
    Salida: Retorno de datos perteneciente al parámetro.
    """
    name = nombre[14:]
    resto = determinaSeleccion(nombre)
    return name, resto[0], resto[1], resto[2]

def validaGenEtiq (genEtiqueta, nombre):
    """
    Funcion: Valida que los datos ingresados en la ventan anterior sean iguales al formato solicitado.
    Entrada: Parámetros genEtiqueta, nombre, dirEspecifica, dirGeneral y codPostal.
    Salida: Retroalimentación y llamado a la función encargada de insertar los dartos ingresados.
    """
    if  nombre !="":
        dFinales = tomaDatos(nombre)
        generaPDF(dFinales[0], dFinales[1], dFinales[2], dFinales[3])
        genEtiqueta.destroy ()
        tit = "Notificación"
        cont = "Se generó la etiqueta corectamente."
        mensajeFrases (tit, cont)
    else:
        tit = "Formato incorrecto"
        cont = "Se deben completar todos los datos."
        mensajeFrases (tit, cont)

#-----------------------------Enviar Correo------------------------------------------
def enviaCorreo (): #5
    """
    Funcion: Ventana que solicita la cédila del cliente para enviar
    Entrada: N/D
    Salida:  Llamada a función auxiliar y extracción de datos. 
    """
    enCorreo = Toplevel()
    enCorreo.minsize(500, 100)
    enCorreo.resizable(width=NO,height=NO)
    enCorreo.title("Enviar Correo")
    enCorreo.config( bg= "#455A64")
    
    #Etiquetas
    Lmensaje = Label(enCorreo, text="Ingrese la cédula del cliente para  enviar un correo.")
    Lmensaje.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lmensaje.place(x=10,y=20)

    Lcedula = Label (enCorreo,text = "Cédula del Cliente---------------------------------")
    Lcedula.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lcedula.place(x=18,y=100)

    #Cuadro de Texto
    cedula = ttk.Entry(enCorreo,width=25)
    cedula.place(x=320, y=105)

    envia=Button ( enCorreo,
                   text="Enviar Correo",
                   command = lambda:[validaCorreoTk (enCorreo,cedula.get() ) ] ).place(x=210,y=150)
    enCorreo.mainloop()
    
def enCorreoAux (enCorreo, cedula):
    """
    Funcion: Verifica que la cedula ingresada esté en la base de datos.
    Entrada: Parámetros enCorreo y cedula.
    Salida: Llamada a función y retorno  de retroalimentación
    """
    if calculaCorreo(cedula)!=False:
        correoF = calculaCorreo(cedula)
        genCorreo (correoF)
        enCorreo.destroy()
        tit = "Notificación"
        cont = "El correo se ha enviado satisfactoriamente."
        mensajeFrases (tit, cont)
    else:
        tit = "Notificación"
        cont = "La cédula no se encuentra en la Base de datos."
        mensajeFrases (tit, cont)
    
def validaCorreoTk (enCorreo, cedula):
    """
    Funcion: Valida que el correo ingresado sea el correcto según el formato indicado.
    Entrada: Parámetros enCorreo y cedula.
    Salida: Llamado a función y mesaje de retroalimentación para el usuario.
    """
    if  cedula !="":
        if validaCedula(cedula) == True:
            enCorreoAux (enCorreo, cedula)
        else:
            tit = "Formato incorrecto"
            cont = "Debe ingresar una cedula valida."
            mensajeFrases (tit, cont)
    else:
        tit = "Formato incorrecto"
        cont = "Se deben completar todos los datos."
        mensajeFrases (tit, cont)
        
#---------------------------Exportar Códigos------------------------------------
def exportarCodigos (): #6
    """
    Funcion: Crea el archivo xml con los datos previamente ingresados
    Entrada: N/D
    Salida: Mensaje de retroalimentación.
    """
    tit = "Notificacaión"
    cont = "Se generó satisfactoriamente el reporte xml."
    mensajeFrases (tit, cont)
    creaXML()

#--------------------------------Reportes---------------------------------------------------
def reportes (): #7 
    """
    Funcion: Ventana que muestra tres botones con las opciones ligadas a reportes.
    Entrada: N/D
    Salida: Botones con llamadas según el tipo de reporte seleccionado.
    """
    reportes = Toplevel()
    reportes.minsize(500, 100)
    reportes.resizable(width=NO,height=NO)
    reportes.title("Reportes")
    reportes.config( bg= "#455A64")
    
    #Etiquetas
    Lmensaje = Label(reportes, text="Seleccione el reporte a generar")
    Lmensaje.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lmensaje.place(x=120,y=60)

    #Botones
    bProvincia=Button ( reportes,
                   text="Clientes de una provincia",
                   command = lambda:[provinciaAux (reportes)] ).place(x=20,y=100)
    
    bCedula=Button ( reportes,
                   text="Buscar un cliente específico ",
                   command = lambda:[cedulaAux (reportes)] ).place(x=180,y=100)
    
    bCodigo=Button ( reportes,
                     text="Clientes según código",
                     command = lambda:[codigoAux (reportes)] ).place(x=350,y=100)
    
    reportes.mainloop()
#-------------------------------------
def provinciaAux (reportes):
    """
    Funcion: Cierra la ventana de reportes y abre el seleccionado funcionando como puente
    Entrada: Parámetro reportes.
    Salida: Lamada a la función destino.
    """
    reportes.destroy()
    provincia()

def cedulaAux (reportes):
    """
    Funcion: Cierra la ventana de reportes y abre el seleccionado funcionando como puente
    Entrada: Parámetro reportes.
    Salida: Lamada a la función destino.
    """    
    reportes.destroy()
    cedula()

def codigoAux (reportes):
    """
    Funcion: Cierra la ventana de reportes y abre el seleccionado funcionando como puente
    Entrada: Parámetro reportes.
    Salida: Lamada a la función destino.
    """  
    reportes.destroy()
    codigo()
#-------------------------------------
    
def provincia ():
    """
    Funcion: Asigna un valor numérico a la provincia encontrada en el parámetro ingresado.
    Entrada: Parámetro cProvincia.
    Salida: Retorno de un número según la provincia.
    """
    provincia = Toplevel()
    provincia.minsize(500, 100)
    provincia.resizable(width=NO,height=NO)
    provincia.title("Reportes provincia")
    provincia.config( bg= "#455A64")

    #Etiquetas
    Lmensaje = Label(provincia, text="Ingrese los datos para generar el reporte")
    Lmensaje.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lmensaje.place(x=120,y=60)

    Lcedula = Label (provincia,text = "Provincia----------------------------------------------")
    Lcedula.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lcedula.place(x=18,y=105)

    #Cuadros de selección
    provincias=("San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón",)
    cProvincia=ttk.Combobox (provincia, width="22", state="readonly", values=provincias)
    cProvincia. place (x=320,y=105)
    
    #Botones
    bCodigo=Button ( provincia,
                     text="Generar Reporte",
                     command = lambda:[repoProvinciaAux(provincia, cProvincia.get() )] ).place(x=200,y=150)

    provincia.mainloop()

def convertirProvincia (cProvincia):
    """
    Funcion: Asigna un valor numérico a la provincia encontrada en el parámetro ingresado.
    Entrada: Parámetro cProvincia.
    Salida: Retorno de un número según la provincia.
    """
    if cProvincia == "San José":
        return 1
    elif cProvincia == "Alajuela":
        return 2
    elif cProvincia == "Cartago":
        return 3
    elif cProvincia == "Heredia":
        return 4
    elif cProvincia == "Guanacaste":
        return 5
    elif cProvincia == "Puntarenas":
        return 6
    elif cProvincia == "Limón":
        return 7
    
def repoProvincia (provincia, cProvincia):
    """
    Funcion: Envia mensaje de retroalimentación y llama a funcion encargada de generar el reporte html
    Entrada: Parámetro cProvincia
    Salida: Llamada de funciones y mensaje de retroalimentación.
    """
    tit = "Notificación"
    cont = "Se creó correctamente el reporte por porvincia."
    mensajeFrases (tit, cont)
    
    provFinal=convertirProvincia(cProvincia)
    opcionHTML1(provFinal)
    provincia.destroy()

def repoProvinciaAux(provincia, cProvincia):
    """
    Funcion: Valida que los datos ingresados estén completos y validos.
    Entrada: Parámetro cProvincia.
    Salida: Llamado a función que genera reporte
    """
    if cProvincia != "":
        repoProvincia(provincia, cProvincia)
    else:
        tit = "Formato incorrecto"
        cont = "Debe completar todos los datos."
        mensajeFrases (tit, cont)

#******************************************************************
def cedula ():
    """
    Funcion: Ventana que solicita datos de entrada y llama una función auxiliar.
    Entrada: N/D
    Salida: Llamada de función auxiliar.
    """
    cedula = Toplevel()
    cedula.minsize(500, 100)
    cedula.resizable(width=NO,height=NO)
    cedula.title("Reportes cédula")
    cedula.config( bg= "#455A64")

    #Etiquetas
    Lmensaje = Label(cedula, text="Ingrese los datos para generar el reporte")
    Lmensaje.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lmensaje.place(x=120,y=60)

    Lcedula = Label (cedula,text = "Cédula----------------------------------------------")
    Lcedula.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lcedula.place(x=18,y=105)

    #Caja de Texto
    cCedula = ttk.Entry(cedula,width=25)
    cCedula.place(x=320, y=105)
    
    #Botones
    bCodigo=Button ( cedula,
                     text="Generar Reporte",
                     command = lambda:[repoCedulaAux(cedula, cCedula.get() )] ).place(x=200,y=150)

    cedula.mainloop()
    
#******************************************************************
def repoCedula (cCedula):
    """
    Funcion: Mensaje de retroalimentación y llamada a funcion que crea el reporte de html
    Entrada: Parámetro  cCedula.
    Salida: Mensaje retroalimentación y llamado a función.
    """
    tit = "Notificación"
    cont = "La Base de datos se creó satisfactoriamente en la carpeta principal."
    mensajeFrases (tit, cont)
    
    opcionHTML2(cCedula)

def repoCedulaAux(cedula,cCedula):
    """
    Funcion: Valida que la cedula ingresada sea igual al formato, cierra la vantana anterior y genera el reporte.
    Entrada: Parámetro cedula y cCedula
    Salida: Llamada a función y mensaje de retroalimentación.
    """
    if cCedula != "":
        if validaCedula(cCedula) == True:
            if existeCedula(cCedula) == True:
                cedula.destroy()
                repoCedula(cCedula)
            else:
                tit = "Notificación"
                cont = "No existe un cliente registrado con esta cédula."
                mensajeFrases (tit, cont)
        else:
            tit = "Formato incorrecto"
            cont = "Debe usar el formato de cédula correcto."
            mensajeFrases (tit, cont)
    else:
        tit = "Formato incorrecto"
        cont = "Debe completar todos los datos."
        mensajeFrases (tit, cont)
    
#******************************************************************
def codigo ():
    """
    Funcion: Ventana que solicita el ingreso de datos .
    Entrada: N/D
    Salida: Llamada a función.
    """
    codigo = Toplevel()
    codigo.minsize(500, 100)
    codigo.resizable(width=NO,height=NO)
    codigo.title("Reportes código")
    codigo.config( bg= "#455A64")

    #Etiquetas
    Lmensaje = Label(codigo, text="Ingrese los datos para generar el reporte")
    Lmensaje.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lmensaje.place(x=120,y=60)

    Lcedula = Label (codigo,text = "Codigo----------------------------------------------")
    Lcedula.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lcedula.place(x=18,y=105)

    #Caja de Texto
    cCodigo = ttk.Entry(codigo,width=25)
    cCodigo.place(x=320, y=105)
    
    #Botones
    bCodigo=Button ( codigo,
                     text="Generar Reporte",
                     command = lambda:[repoCodigoAux(codigo, cCodigo.get() )] ).place(x=200,y=150)

    codigo.mainloop()

def codigosExistentes():
    """
    Funcion: Extrae los códigos redistrados en la BD.
    Entrada: N/D
    Salida: Lista con códigos postales registrados en la BD.
    """
    bd = lee("BD")
    codigosFinales = []
    for objeto in bd:
        actual = objeto.indicaPostal()
        codigosFinales.append(actual)
    return codigosFinales

def repoCodigoAux(codigo,cCodigo):
    """
    Funcion: Verifica que el codigo ingresado por parámetro séa el correcto y genera el archivo html.
    Entrada: Parámetros codigo y cCodigo.
    Salida: Mensaje de retroalimentación y archivo html
    """
    if cCodigo != "":
        if validaCodigoPostal(cCodigo) == True:
            codigosGen = codigosExistentes()
            if cCodigo in codigosGen:
                opcionHTML3(cCodigo)
                codigo.destroy()
                tit = "Notificaión"
                cont = "El reporte se generó correctamente."
                mensajeFrases (tit, cont)
            else:
                tit = "Notificación"
                cont = "Este código no está registrado en la base de datos."
                mensajeFrases (tit, cont)
        else:
            tit = "Formato incorrecto"
            cont = "Debe usar el formato de código correcto."
            mensajeFrases (tit, cont)
    else:
        tit = "Formato incorrecto"
        cont = "Debe completar todos los datos."
        mensajeFrases (tit, cont)

#----------------------------------Credenciales-------------------------------------------
def credencialAutor (): #8
    """
    Funcion: Ventana con las fotografías y descripción de los desarrolladores del programa.
    Entrada: N/D
    Salida: Ventana con fotos y nombres.
    """
    credencial = Toplevel()
    credencial.minsize(500, 300)
    credencial.resizable(width=NO,height=NO)
    credencial.title("Credenciales")
    credencial.config( bg= "#455A64")

    #Imagen Buscada   
    imagen= CargarImagen("needler.png")
    imagen1= CargarImagen("pablo.png")
    
    #Imagenes
    fondo=Label (credencial,image=imagen).place(x=30,y=50) 
    fondo=Label (credencial,image=imagen1).place(x=270,y=50)
    
    #Etiquetas
    mensaje= Label (credencial, text = "Co-desarrolladores de la propiedad intelectual:")
    mensaje.config(font=("Arial 12"),fg="White", bg="#455A64")
    mensaje.place (x=90,y=10)
    
    Lnombre1 = Label (credencial,text = "Needler Bonilla Serrano")
    Lnombre1.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lnombre1.place(x=40,y=260)

    Lnombre2 = Label (credencial,text = "Pablo Agüero Mora")
    Lnombre2.config(font=('Arial 12'),fg="white",bg="#455A64")
    Lnombre2.place(x=300,y=260)

    credencial.mainloop()
    
#---------------------------------------PP----------------------------------------------
infoCodigos = []

if __name__ == '__main__':
    ventana = Tk()  
    ventana.title("  ") 
    ventana.minsize(550, 500)
    ventana.resizable(width=NO, height=NO)
    ventana.config(bg="blue")
    ventana.overrideredirect(True)

    if existeArchivo("infoCodigos") == True:
        x =tk.NORMAL
    else:
        x = tk.DISABLED

    if existeArchivo("BD") == True:
        y =tk.NORMAL
    else:
        y = tk.DISABLED

    VentanaPrincipal(x, y)
