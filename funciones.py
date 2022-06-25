#Elaborado por: Needler Bonilla Serrano
#               Jose Pablo Agüero Mora
#Fecha de Creación: 11/11/2021 6:00pm 
#Fecha de última Modificación: 29/11/2021 00:00pm
#Versión: 3.9.6

# Importe de librerías #

import re
import names
import random
from archivos import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import datetime
from fpdf import FPDF
from xml.dom import minidom

# Definición de funciones #
#-------------------------- Estructura de objetos ------------------------------------------

class Cliente:
    """Definición de Atributos de la clase"""

    def __init__(self):
        """
        Función: Inicialización de atributos.
        Entradas:N/D
        Salida: Retorno de atributos.
        """
        self.cedula = ""
        self.nombre = ""
        self.dirEsp = ""
        self.dirGen = ""
        self.postal = ""
        self.correo = ""
        return

    def asignarCedula(self, pcedula):
        """
        Función: Agregar el nombre al atributo.
        Entradas: Parámetro cedula.
        Salidas: Retorno de artibuto.
        """
        self.cedula = pcedula
        return

    def asignarNombre(self, pnombre):
        """
        Función: Agregar el nombre al atributo.
        Entradas: Parámetro nombre.
        Salidas: Retorno de artibuto.
        """
        self.nombre = pnombre
        return

    def asignarDirEsp(self, pdirEsp):
        """
        Función: Agregar el nombre al atributo.
        Entradas: Parámetro dirección específica.
        Salidas: Retorno de artibuto.
        """
        self.dirEsp = pdirEsp
        return

    def asignarDirGen(self, pdirGen):
        """
        Función: Agregar el nombre al atributo.
        Entradas: Parámetro dirección general.
        Salidas: Retorno de artibuto.
        """
        self.dirGen = pdirGen
        return

    def asignarPostal(self, ppostal):
        """
        Función: Agregar el nombre al atributo.
        Entradas: Parámetro código postal.
        Salidas: Retorno de artibuto.
        """
        self.postal = ppostal
        return

    def asignarCorreo(self, pcorreo):
        """
        Función: Agregar el nombre al atributo.
        Entradas: Parámetro correo electrónico.
        Salidas: Retorno de artibuto.
        """
        self.correo = pcorreo
        return

    def indicaCedula(self):
        """
        Función: Ubica el altributo cédula.
        Entradas: N/D
        Salidas: Retorno de cédula.
        """
        return self.cedula

    def indicaNombre(self):
        """
        Función: Ubica el altributo nombre.
        Entradas: N/D
        Salidas: Retorno de nombre.
        """
        return self.nombre

    def indicaDirEsp(self):
        """
        Función: Ubica el altributo dirección especial.
        Entradas: N/D
        Salidas: Retorno de dirección especial.
        """
        return self.dirEsp

    def indicaDirGen(self):
        """
        Función: Ubica el altributo dirección general.
        Entradas: N/D
        Salidas: Retorno de dirección general.
        """
        return self.dirGen

    def indicaPostal(self):
        """
        Función: Ubica el altributo dirección postal.
        Entradas: N/D
        Salidas: Retorno de dirección postal.
        """
        return self.postal

    def indicaCorreo(self):
        """
        Función: Ubica el altributo correo electrónico.
        Entradas: N/D
        Salidas: Retorno de correo electrónico.
        """
        return self.correo

# Registrar un cliente #
# ------------------Función para agregar cliente (objetos) ------------------------------------------
def cuentaRep(num, lista):
    """
    Función: Cuenta la cantidad de elementos repetidos en una lista.
    Entradas: Parámetro - num, número a buscar y lista.
    Salidas: Contador.
    """
    cont = 0
    for elem in lista:
        if num == elem:
            cont += 1
    return cont

def cualUsuarioCorreo(correo):
    """
    Función: Indica el usuario correspondiente a un correo indicado.
    Entradas: Parámetro - correo.
    Salidas: Objeto correspondiente a ese correo.
    """
    for objeto in listaGeneral:
        if objeto.indicaCorreo() == correo:
            return objeto

def procesaRepetidos(plista):
    """
    Función: Elimina los usuarios con correos repetidos generados aleatoriamente.
    Entradas: Parámetro - plista.
    Salidas: Elimina los repetidos y llama a la función que genera nuevos clientes.
    """
    for x in plista:
        objeto = cualUsuarioCorreo(x)
        listaGeneral.remove(objeto)
        generaClienteInfo()
        
def verCorreosRepetidos():
    """
    Función: Calcula una lista con los correos repetidos de la BD.
    Entradas: N/D
    Salidas: Llama a la función procesaRepetidos() con la lista de repetidos.
    """
    bd = lee("BD")
    total = []
    sinRepetidos = []
    indices = []
    noRep = []
    for elemento in bd:
        total.append(elemento.indicaCorreo())

    for correo in total:
        if correo not in sinRepetidos:
            sinRepetidos.append(correo)

    for x in sinRepetidos:
        if cuentaRep(x, total) >= 2:
            indices.append(x)
 
    return procesaRepetidos(indices)

def cicloGeneraCliente(num):
    """
    Función: Genera clientes aleatorios en un ciclo definido.
    Entradas: Parámetro - num, cantidad de clientes a generar.
    Salidas: Llama a la función que genera clientes aleatorios.
    """
    for i in range(num):
        generaClienteInfo()
    verCorreosRepetidos()

def instertarCliente(cedula, nombre, dirEsp, dirGen, postal, correo):
    """
    Funciones: Asigna los atributos al objeto.
    Entradas: N/D
    Salidas: Edita los atributos.
    """
    cliente = Cliente()

    cliente.asignarCedula(cedula)
    cliente.asignarNombre(nombre)
    cliente.asignarDirEsp(dirEsp)
    cliente.asignarDirGen(dirGen)
    cliente.asignarPostal(postal)
    cliente.asignarCorreo(correo)

    listaGeneral.append(cliente)
    graba(listaGeneral, "BD")
    return

# ------------------------ Validaciones Generales ----------------------------------------
def validaCedula(nCedula):
    """
    Funcion: Valida que el parámetro ingresado sea el mismo que el de una cedula.
    Entrada: Parámetro nCedula
    Salida: Retorno de banderas
    """
    if re.search("^[1-9]{1}\-{1}\d{4}\-{1}\d{4}$", nCedula):
        return True
    else:
        return False

def validaNombre(sNombre):
    """
    Funcion: Valida que el parámetro sea de tres palabras
    Entrada: Parámetro sNombre
    Salida: Retorno de banderas true o false
    """
    if len(sNombre.split()) == 3:
        return True
    else:
        return False

def validaDireccionEsp(sDir1):
    """
    Funcion: Valdia que el parámetro sea el mismo que el formato de la dirección específica.
    Entrada: Parámetro sDir1
    Salida: Retorno de banderas true o false
    """
    if re.search("^(Ca){1}\s{1}\d{2}\s{1}(Av){1}\s{1}\d{2}\s{1}(#){1}\s{1}\d{2}$", sDir1):
        if int(sDir1[3:5]) <= 60 and int(sDir1[9:11]) and int(sDir1[14:16]):
            return True
        else:
            return False
    else:
        return False

def validaDireccionGen(sDir2):
    """
    Funcion: Valida que el parámetro sea el correcto para la dirección general. (tres palabras)
    Entrada:Parámetros sDir2
    Salida:Retorno de vanderas true o false
    """
    if len(sDir2.split(",")) == 3:
        return True
    else:
        return False

def validaCodigoPostal(nPostal):
    """
    Funcion: Valida que el parámetro sea el correcto para el código postal
    Entrada: Parámetro nPostal 
    Salida: Retorno de bandera true o false
    """
    if re.search("^[1-7]{1}\d{4}$", nPostal):
        return True
    else:
        return False

def validaCorreo(sCorreo):
    """
    Funcion: Valida que el parámetro sea el correcto para el Correo electrónico
    Entrada: Parámetro sCorreo
    Salida: Retorno de bandera true o false
    """
    if re.search("^\w+(@gmail|@hotmail){1}(.com){1}$", sCorreo):
        return True
    else:
        return False

def existeCedula(pCedula):
    """
    Funcion: Verifica que el parámetro sea el mismo que la cédula en la base de datos
    Entrada: Parámetro pCedula
    Salida: Retorno de banderas true o false
    """
    bd = lee("BD")
    for elemento in bd:
        if str(pCedula) == str(elemento.indicaCedula()):
            return True
    return False

def existeCorreo(pCorreo):
    """
    Funcion: Verifica que el parámetro sea el mismo que el correo en la base de datos
    Entrada: Parámetro pCorreo
    Salida: Retorno de banderas true o false
    """
    bd = lee("BD")
    for elemento in bd:
        if str(pCorreo) == str(elemento.indicaCorreo()):
            return True
    return False

def valInicialPostal(cedula, postal):
    if postal[0] == "1":
        if cedula[0] in ["1", "8", "9"]:
            return True
        else:
            return False
    elif cedula[0] == postal[0]:
        return True
    else:
        return False
    
#---------------------------- Extrae los datos -------------------------------------
def extraeCodigos():
    """
    Función: Extrae todos los códigos del txt.
    Entrada: N/D
    Salida: Lista con todos los códigos.
    """
    codigos = []
    listaCompleta = leeArchivo()
    for elemento in listaCompleta:
        codigos.append(elemento[-1])
    return codigos

#--------------------------- Genera dinámicamente ----------------------------------#
def randomSpawn():
    """
    Funcion: Genera numero aleatoriamente con un formato específico
    Entrada: N/D
    Salida: Retorno de lista general 
    """
    num = random.randint(1, 9999)
    if len(str(num)) == 1:
        final = "000" + str(num)
    elif len(str(num)) == 2:
        final = "00" + str(num)
    elif len(str(num)) == 3:
        final = "0" + str(num)
    else:
        final = str(num)
    return final

def generaCedula(codigo):
    """
    Funcion: Genera de forma aleatória una cédula con un formato correcto
    Entrada: Parámetro codigo.
    Salida: Retorno de la cédula generada
    """
    digito = codigo[0]
    opciones = ["1", "8", "9"]
    if digito == "1":
        rand = random.randint(0, 2)
        dFinal = opciones[rand]
    else:
        dFinal = digito
        
    num1 = randomSpawn()
    num2 = randomSpawn()
    cedula = dFinal + "-" + num1 + "-" + num2
    return cedula

def generaNombre():
    """
    Función: Genera de forma aleatoria dos nombre y dos apellidos de una librería (names)
    Entrada: N/D
    Salida: Nombre generado aleatoriamente.
    """
    nombre1=names.get_first_name()
    nombre2=names.get_first_name()
    Papellido=names.get_last_name()
    Sapellido=names.get_last_name()

    nombre = nombre1.lower() + " " + nombre2.lower()
    Papellido = Papellido.lower()
    Sapellido = Sapellido.lower()

    nomCompleto=[nombre,Papellido,Sapellido]
    nombre=tuple(nomCompleto)
    return nombre

def spawn2():
    """
    Funcion: Genera de forma aleatória un número de dirección específica.
    Entrada: N/D
    Salida: Retorno de lista general.
    """
    num = random.randint(1, 60)
    if len(str(num)) == 1:
        final = "0" + str(num)
    else:
        final = str(num)
    return final

def generaDirEsp():
    """
    Funcion: Genera de forma aleatória la dirección específica.
    Entrada: N/D
    Salida: Retorno de lista general con los valores generados
    """
    num1 = spawn2()
    num2 = spawn2()
    num3 = spawn2()
    final = "Ca " + num1 + " Av " + num2 + " # " + num3
    return final
    
def generaDirGen(codigo):
    """
    Funcion: Genera una dirección general extrallendo datos dentro de la base de datos.
    Entrada: Parámetro codigo
    Salida:Retorno de variable con la lista de la dirección general
    """
    listaCodigos = extraeCodigos()
    listaCompleta = leeArchivo()
    indice = listaCodigos.index(codigo)
    direccion = listaCompleta[indice][:-1]
    return direccion    

def generaCorreo(nombre):
    """
    Funcion: Genera correos según el formato solicitado (Inicial del nombre y primer apellido).
    Entrada: Parámetro nombre
    Salida: Retorno de variable con el correo 
    """
    inicial = nombre[0][0].lower()
    apellido = nombre[1].lower()
    final = inicial + apellido + "@" + "gmail.com"
    return final

def generaClienteInfo():
    """
    Funcion: Llama funciones y genera todos los datos para crear un cliente. 
    Entrada: N/D
    Salida: Retorno de función con el cliente generado
    """
    listaCodigos = extraeCodigos()
    indice = random.randint(0, (len(listaCodigos) - 1))
    codigo = listaCodigos[indice]

    cedula = generaCedula(codigo)
    
##    print (cedula)
    nombre = generaNombre()
##    print (nombre)
    dirEsp = generaDirEsp()
##    print (dirEsp)
    dirGen = generaDirGen(codigo)
##    print (dirGen)
##    print (codigo)
    correo = generaCorreo(nombre)
##    print (correo)

    return instertarCliente(cedula, nombre, dirEsp, dirGen, codigo, correo)

#------------------------------- Correo ----------------------------------------------
def calculaCorreo(cedula):
    """
    Funcion: Verifica que el correo pertenesca a la cédula del cliente a buscar.
    Entrada: Parámetro cedula
    Salida: Retorno de bandera true o false
    """
    for elemento in listaGeneral:
        actual = elemento.indicaCedula()
        if cedula == actual:
            return elemento.indicaCorreo()
    return False

def generaFecha():
    """
    Función: Genera la fecha actual y la fecha del día siguiente usando librería
    Entrada: N/D
    Salida: Retorno de fechas
    """
    hoy = datetime.date.today()
    manana = hoy + datetime.timedelta(1)
    return hoy, manana

def creaMensaje():
    """
    Función: Genera el mensaje dinámico que se incluye en el correo electrónico.
    Entrada: N/D
    Salida: Mensaje completo.
    """
    hoy = str(generaFecha()[0])
    manana = str(generaFecha()[1])

    message = "No fue posible hacer la entrega el día " + hoy + ". La nueva entrega se hará el día " + str(manana) + "."
    return message

def genCorreo(correo):
    """
    Función: Envía el correo a la dirección correspondiente.
    Entrada: Parámetro - correo, destinatario.
    Salida: Envío del correo.
    """
    msg = MIMEMultipart()
    message = creaMensaje()

    # Configuración de parámetros del mensaje
    password = "ultimoProyecto"
    msg['From'] = "ProyectoPruebaN3@gmail.com"
    msg['To'] = correo
    msg['Subject'] = "Cambio de fecha de entrega de paquete"

    # Agrega el cuerpo del mensaje
    msg.attach(MIMEText(message, 'plain'))
    
    #Crea el servidor
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Ingresa las credenciales para enviar el correo
    server.login(msg['From'], password)

    # Envia el mensaje por el servidor
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print ("Se ha enviado satisfactóriamente %s:" % (msg['a']))

# Sección HTML #
#------------------------------Templates ----------------------------------------
template1 = """
<center>
    <h1>----------</h1>
    <table border width="50%">
        <tr>
            <th colspan=6 style= "font-size:150%">Reporte - Por provincia</th>
        </tr>
        <tr>
            <td style="font-size:150%">Cédula</td> <td style="font-size:150%">Nombre completo</td> <td style="font-size:150%">DirEspec</td> <td style="font-size:150%">DisGen</td> <td style="font-size:150%">CodP</td>
        </tr>
"""

template2 = """
<center>
    <h1>----------</h1>
    <table border width="50%">
        <tr>
            <th colspan=6 style= "font-size:150%">Reporte - Por cliente</th>
        </tr>
        <tr>
            <td style="font-size:150%">Nombre completo</td> <td style="font-size:150%">DirEpec</td> <td style="font-size:150%">DisGen</td> <td style="font-size:150%">CodP</td>
        </tr>
"""
template3 = """
<center>
    <h1>----------</h1>
    <table border width="50%">
        <tr>
            <th colspan=6 style= "font-size:150%">Reporte - Por código postal</th>
        </tr>
        <tr>
            <td style="font-size:150%">Cédula</td> <td style="font-size:150%">Nombre completo</td> <td style="font-size:150%">DirEspec</td> <td style="font-size:150%">DisGen</td> <td style="font-size:150%">CodP</td>
        </tr>
"""

def crearHTML(nombreArchivo, template):
    """
    Función: Crea un HTML y determina las pocisiones de las sublistas dentro del mismo.
    Entrada: N/D
    Salida: Documento HTML Con todos los elementos de SubLista.
    """
    f = open(nombreArchivo, 'w')
    html_template = template
    f.write(html_template) 
    f.close()

def leer2(nombreArchivo):   
    """
    Función: Lee el contenido del HTML
    Entrada:N/D
    Salida: Retorno de variable content
    """
    with open(nombreArchivo, "r") as file:
        content = file.read()
        return content

def agregaFilas1(lista):
    """
    Función: Agrega las filas de la tabla con sus respectivos valores.
    Entrada: Parámetro - (lista) Matriiz con todos los datos y
    (indice) que es el indicador de la columna.
    Salida: Edición del contenido HMTL.
    """
    content = """
        <tr>"""
    content += """
            <td>"""+str(lista[0])+"</td>"+" <td>"+str(lista[1])+"</td>"+" <td>"+str(lista[2])+"</td>" + " <td>"+str(lista[3])+"</td>" +" <td>"+str(lista[4])+"</td>"
    content += """
        </tr>"""
    return content

def agregaFilas2(lista):
    """
    Función: Agrega las filas de la tabla con sus respectivos valores.
    Entrada: Parámetro - (lista) Matriiz con todos los datos y
    (indice) que es el indicador de la columna.
    Salida: Edición del contenido HMTL.
    """
    content = """
        <tr>"""
    content += """
            <td>"""+str(lista[1])+"</td>"+" <td>"+str(lista[2])+"</td>"+ " <td>"+str(lista[3])+"</td>" +" <td>"+str(lista[4])+"</td>"
    content += """
        </tr>"""
    return content

def agregaFilas3(lista):
    """
    Función: Agrega las filas de la tabla con sus respectivos valores.
    Entrada: Parámetro - (lista) Matriiz con todos los datos y
    (indice) que es el indicador de la columna.
    Salida: Edición del contenido HMTL.
    """
    content = """
        <tr>"""
    content += """
            <td>"""+str(lista[0])+"</td>"+" <td>"+str(lista[1])+"</td>"+" <td>"+str(lista[2])+"</td>" + " <td>"+str(lista[3])+"</td>" +" <td>"+str(lista[4])+"</td>"
    content += """
        </tr>"""
    return content

def agregaEtiquetas():
    """
    Función: Agrega las líneas finales del HTML.
    Entrada: N/D
    Salida: Variable con las etiquetas.
    """
    content = """
    </table>
    <h1>----------</h1>
</center>"""
    return content

def grabaFinal(content, nombreArchivo):
    """
    Función: Abre el documento HTML y agrega todos los elemento dentro del documento.
    Entrada: Parámetro - (content) Contenido acumulado hasta el momento.
    Salida: N/D
    """
    with open(nombreArchivo, "w") as file:
        file.write(content)

# Ciclo filas #

def cicloFilas1(nombreArchivo, plista):
    """
    Función: Se encarga de llenar cada celda de la planilla con elementos deseados de la lista.
    Entrada: Parámetro lista.
    Salida: N/D
    """
    content = leer2(nombreArchivo)
    contador = 0
    while contador < len(plista):
        content += agregaFilas1(plista[contador])
        contador += 1

    content += agregaEtiquetas()
    grabaFinal(content, nombreArchivo)

def cicloFilas2(nombreArchivo, plista):
    """
    Función: Se encarga de llenar cada celda de la planilla con elementos deseados de la lista.
    Entrada: Parámetro lista.
    Salida: N/D
    """
    content = leer2(nombreArchivo)
    contador = 0
    while contador < len(plista):
        content += agregaFilas2(plista[contador])
        contador += 1

    content += agregaEtiquetas()
    grabaFinal(content, nombreArchivo)

def cicloFilas3(nombreArchivo, plista):
    """
    Función: Se encarga de llenar cada celda de la planilla con elementos deseados de la lista.
    Entrada: Parámetro lista.
    Salida: N/D
    """
    content = leer2(nombreArchivo)
    contador = 0
    while contador < len(plista):
        content += agregaFilas3(plista[contador])
        contador += 1

    content += agregaEtiquetas()
    grabaFinal(content, nombreArchivo)

# Clasificar sublistas #

def clasProvinciaAux(provincia):
    """
    Función: Crea una lista con los clientes pertenecientes a determinada provincia.
    Entrada: Parámetro - provincia.
    Salida: Lista con clientes.
    """
    final = []
    objetos = lee("BD")
    for elemento in objetos:
        if int(elemento.indicaCedula()[0]) == int(provincia):
            final.append(elemento)
        elif int(elemento.indicaCedula()[0]) == 8 and int(provincia) == 1:
            final.append(elemento)
        elif int(elemento.indicaCedula()[0]) == 9 and int(provincia) == 1:
            final.append(elemento)
    return final

def clasClienteAux(cliente):
    """
    Función: Busca un cliente específico según su cédula.
    Entrada: Parámetro - cliente, cédula.
    Salida: Cliente específico.
    """
    final = []
    objetos = lee("BD")
    for elemento in objetos:
        if str(elemento.indicaCedula()) == str(cliente):
            final.append(elemento)
    return final

def clasCodigoAux(codigo):
    """
    Función: Crea una lista con todos los clientes de un mismo código postal.
    Entrada: Parámetro - codigo.
    Salida: Lista con clientes.
    """
    final = []
    objetos = lee("BD")
    for elemento in objetos:
        if int(elemento.indicaPostal()) == int(codigo):
            final.append(elemento)
    return final

# Procesar datos #

def corrigeNombre(plista):
    """
    Función: Cambia las tuplas de nombres por str legibles.
    Entrada: Parámetro - plista, clientes.
    Salida: Lista con nombres procesados.
    """
    for elemento in plista:
        tupla = elemento[1]
        nombre = tupla[0] + " " + tupla[1] + " " + tupla[2]
        elemento[1] = nombre.title()
    return plista

def corrigeDirGen(plista):
    """
    Función: Cambia las listas de direcciones por str legibles.
    Entrada: Parámetro - plista, clientes.
    Salida: Lista con direcciones generales procesadas.
    """
    for elemento in plista:
        lista = elemento[3]
        direccion = lista[0] + ", " + lista[1] + ", " + lista[2]
        elemento[3] = direccion
    return plista

# Opciones HTML #

def opcionHTML1(provincia):
    """
    Función: Incluye todos los procesos necesarios a realizar cuando se
    elige la opción Generar documento HTML.
    Entrada: Parámetro - provincia, número de provincia.
    Salida: Realiza los procesos para crear y escribir automáticamente
    en el archivo HTML.
    """
    crearHTML("reporte_por_provincia.html", template1)
    plista = clasProvinciaAux(provincia) 
    plista = translate(plista)
    proceso1 = corrigeNombre(plista)
    proceso2 = corrigeDirGen(proceso1)
    cicloFilas1("reporte_por_provincia.html", plista)
    return ""

def opcionHTML2(cliente):
    """
    Función: Incluye todos los procesos necesarios a realizar cuando se
    elige la opción Generar documento HTML.
    Entrada: Parámetro - cliente, cédula.
    Salida: Realiza los procesos para crear y escribir automáticamente
    en el archivo HTML.
    """
    crearHTML("reporte_por_cliente.html", template2)
    plista = clasClienteAux(cliente)
    plista = translate(plista)
    proceso1 = corrigeNombre(plista)
    proceso2 = corrigeDirGen(proceso1)
    cicloFilas2("reporte_por_cliente.html", plista)
    return ""

def opcionHTML3(codigo):
    """
    Función: Incluye todos los procesos necesarios a realizar cuando se
    elige la opción Generar documento HTML.
    Entrada: Parámetro - codigo, código postal.
    Salida: Realiza los procesos para crear y escribir automáticamente
    en el archivo HTML.
    """
    crearHTML("reporte_por_codigo.html", template3)
    plista = clasCodigoAux(codigo)
    plista = translate(plista)
    proceso1 = corrigeNombre(plista)
    proceso2 = corrigeDirGen(proceso1)
    cicloFilas3("reporte_por_codigo.html", plista)
    
    return ""

# Fin Opciones HTML #

def translate(lista):
    """
    Función: Traduce cada objeto en una lista con cada dato legible.
    Entrada: Parámetro - lista, con todos los objetos de la BD.
    Salida: Lista traducida.
    """
    nueva = []
    for objeto in lista:
        sub = []
        sub.append(objeto.indicaCedula())
        sub.append(objeto.indicaNombre())
        sub.append(objeto.indicaDirEsp())
        sub.append(objeto.indicaDirGen())
        sub.append(objeto.indicaPostal())
        sub.append(objeto.indicaCorreo())

        nueva.append(sub)
    return nueva

#---------------------------- Sección PDF -------------------------------------------
def generaPDF (nombre, dirEspecifica, dirGeneral, codPostal):
    """
    Función: Genera el documento PDF con celdas según sus parámetros.
    Entrada: Parámetro - nombre / dirEspecifica / dirGeneral / codPostal
    Salida: Crea el archivo.
    """
    pdf = FPDF (orientation = "L", unit = "mm", format= "A4")
    pdf.add_page ()
    pdf.set_font("Arial","",12) 
    pdf.cell(w=150,h=15,txt="",border="TRL",ln=1,align="C",fill=0) 
    pdf.multi_cell(w=150,h=15,txt="",border="RL",align="C",fill=0)
    pdf.set_font("Arial","B",12) 
    pdf.multi_cell(w=150,h=8,txt="                "+ nombre,border="RL",align="L",fill=0)
    pdf.set_font("Arial","",12) 
    pdf.multi_cell(w=150,h=8,txt="                " + dirEspecifica ,border="RL",align="L",fill=0)
    pdf.multi_cell(w=150,h=8,txt="                " + dirGeneral,border="RL",align="L",fill=0)
    pdf.multi_cell(w=150,h=8,txt="                " + codPostal,border="RL",align="L",fill=0)
    pdf.multi_cell(w=150,h=8,txt="                " + "COSTA RICA",border="RL",align="L",fill=0)
    pdf.multi_cell(w=150,h=8,txt="",border="RBL",align="L",fill=0)

    pdf.image ("logo.png",x=125, y=20, w= 20, h= 20)
    nombre = nombre.split()
    pdf.output(nombre[0]+".pdf")

#------------------------------ Creación de XML -----------------------------------------

#----------Funcionamiento de XML----------

def eliminaElementoEspacio(listaPuntuacion):
    """
    Función: Busca y elimina los espacios dentro de la lista ya tokenizada y los almacena.
    Entrada: Parámetro listaPuntuación (Lista Tokenizada).
    Salida: Lista Final sin espacios en su interior.
    """
    listaFinal = []
    for elemento in listaPuntuacion:
        if elemento != "":
            listaFinal.append(elemento)
    
    return listaFinal

def quitaTildes(cadena):
    """
    Función: Lee cada elemento de una lista tíldada y los cambia por unos sin tílde.
    Entrada: Parámetro cadena (Oración Tokenizada).
    Salida: Retorno de lista ingresada como parámetro.
    """
    a,b = 'áéíóúüñÁÉÍÓÚÜÑ','aeiouunAEIOUUN'
    trans = str.maketrans(a,b)
    convertida = cadena.translate(trans)
    return convertida

def listaString (lista):
    """
    Función:Almacena las Sub-Listas tokenizadas y las combierte en string para ser utilizadas en XML.
    Entrada: Parámetro Lista.
    Salida: Lista Principal con todas las sub listas en su interior.
    """
    listaTotal=[]
    for elem in lista:
        provincia = (elem[0])
        
        canton = (elem[1])
        distrito = (elem[2])
        codigo = (elem[3])

        provincia = str(provincia)
        canton = str(canton)
        distrito = str(distrito)
        codigo = str(codigo)

        listaPrincipal=[quitaTildes(provincia),quitaTildes(canton),quitaTildes(distrito),codigo]
        listaTotal.append(listaPrincipal)
    return listaTotal

#----------Generación del XML----------
def creaXML ():
    """
    Función: Crea un xml y determina las pocisiones de las sublistas dentro del mismo
    Entrada: Parámetro lista (Lista principal con sub listas)
    Salida: Documento XML Con todos los elementos de listaPrincipal.
    """
    lista=leeArchivo()
    
    DOMimpl = minidom.getDOMImplementation()
    xmldoc= DOMimpl.createDocument(None,"Raiz",None)
    listaPrincipal=listaString (lista)
    doc_root = xmldoc.documentElement
    
    cont=0
    for elemento in listaPrincipal:

        nodo1 = xmldoc.createElement ("Codigo")
        nodo1.setAttribute("Postal",elemento[3]) 
        
        provincia = xmldoc.createElement ("Provincia") 
        provincia.appendChild(xmldoc.createTextNode(elemento[0]))
        nodo1.appendChild(provincia)

        canton = xmldoc.createElement ("Canton")
        canton.appendChild(xmldoc.createTextNode(elemento[1]))
        nodo1.appendChild(canton)

        distrito = xmldoc.createElement ("Distrito")
        distrito.appendChild(xmldoc.createTextNode(elemento[2]))
        nodo1.appendChild(distrito)

        doc_root.appendChild(nodo1)
        
        cont+=1
        
    fichero = open("Código Postal.xml","w")
    fichero.write(xmldoc.toxml ())
    fichero.close()

# Variables globales #

if existeArchivo("BD") == True:
    listaGeneral = lee("BD")
elif existeArchivo("BD") == False:
    listaGeneral = []
