#Elaborado por: Needler Bonilla Serrano
#               Jose Pablo Agüero Mora
#Fecha de Creación: 11/11/2021 6:00pm 
#Fecha de última Modificación: 29/11/2021 00:00pm
#Versión: 3.9.6

# Importe de librerías
import pickle
import requests

# Definición de funciones:

############################# Manejo de archivos ###########################
def existeArchivo(nomArchLeer):
    """
    Función: Verifica que exista un archivo con el nombre indicado.
    Entradas: Parámetro - Nombre del archivo (nomArchLeer).
    Salidas: True si existe el archivo en la carpeta, False si no existe el archivo.
    """
    try:
        f=open(nomArchLeer,"rb")
        pickle.load(f)
        f.close()
        return True
    except:
        return False

def lee(nomArchLeer):
    """
    Función: Lee los datos del archivo indicado.
    Entradas: Parámetro - Nombre del archivo (nomArchLeer).
    Salidas: Retorna los datos (codigos) del archivo indicado.
    """
##    try:
    f=open(nomArchLeer,"rb")
    codigos = pickle.load(f)
    f.close()
    return codigos
##    except:
##        print("Error al leer el archivo: ", nomArchLeer)
##    return

def graba(lista, nomArchGrabar):
    """
    Función: Crea el archivo inicial con la lista de códigos.
    Entradas: Parámetro - Nombre de la lista (lista).
    Salidas: Crea el archivo o envía un mensaje de error en caso de que no sea posible.
    """
    try:
        f=open(nomArchGrabar,"wb")
        pickle.dump(lista,f)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)
    return

def grabaFinal(content, nombreArchivo):
    """
    Función: Abre el documento HTML y agrega todos los elemento dentro del documento.
    Entrada: Parámetro - (content) Contenido acumulado hasta el momento.
    Salida: N/D
    """
    with open(nombreArchivo, "w") as file:
        file.write(content)

def leeArchivo():
    """
    Función: Retorna el contenido dentro del txt al programa.
    Entrada: N/D
    Salida: Contenido dentro del txt en una lista.
    """
    datos = []
    with open ("BDPostalCR.txt","r") as salida:
        for linea in salida:
            datos.append(linea[:-1].split(";"))
    graba (datos, "infoCodigos")
    return datos
