### To Do's ###
# - Preguntar donde almacenar consulta
# Por default que se guarde en Desktop
# Hacer una GUI para seleccionar más facil la info
# auto generacion de reporte sobre rango de consulta


# MODULOS
import datetime
from datetime import timedelta
import pandas as pd
import re
# from difflib import get_close_matches    --> vale la pena explorar esto
import time

# =================================== FUNCIONES =========================================================== #

# Convierte en lista el archivo con los nombres de nodos
def txt_to_list(txt_file):
    with open(txt_file) as file:
        lines = file.readlines()
    node_list = [line.replace("\n", "") for line in lines]
    return node_list


# Esta función convierte el contenido JSON del URL en una Data Frame
def url_into_df(url):
    json = pd.read_json(url)["Resultados"][0]["Valores"]
    data_frame = pd.DataFrame(json)
    return data_frame


# Crea una lista de URLs para el rango de fechas dado. Recordar que la API solo permite consultar hasta 7 días.
def date_to_url(startDate, endDate, url):
    url_list = []
    x = startDate
    while x <= endDate:
        datestr = x.strftime("%Y/%m/%d")
        delta = x + timedelta(days=6)
        deltastr = delta.strftime("%Y/%m/%d")
        url_list.append(url.format(datestr, deltastr))
        x = delta + timedelta(days=1)
    return url_list


# =================================== MAIN =========================================================== #

# Simplemente pide las fechas del plazo de la consulta
dia_i = int(input("Dia inicio: "))
mes_i = int(input("Mes inicio: "))
anio_i = int(input("Año inicio: "))

dia_f = int(input("Dia fin: "))
mes_f = int(input("Mes fin: "))
anio_f = int(input("Año fin: "))

nodoD_lista = txt_to_list("nodosD.txt")

# Seleccionar el sistema, aunque escribas en minuscula, lo convierte en mayuscula
while True:
    sistema = input("SIN BCA o BCS: ").upper()
    if sistema in ("SIN", "BCA", "BCS"):
        break
    else:
        continue

# Seleccionar si es MDA o MTR
while True:
    proceso = input("MDA o MTR: ").upper()
    if proceso in ("MDA", "MTR"):
        break
    else:
        continue

# Selecciona si es nodo P o nodo Distribuido
while True:
    tipo_nodo = input("Nodo P o D: ").upper()
    if tipo_nodo in ("P", "D"):
        break
    else:
        continue

if tipo_nodo == "D":
    tipo_request = "SWPEND"

    while True:
        nodo = input("Introduce nombre nodo: ").upper().replace(" ", "-")
        if nodo in txt_to_list("nodosD.txt"):
            break
        else:
            print("Nombre de nodo equivocado, intenta de nuevo:  ")
            continue

else:
    tipo_request = "SWPML"
    while True:
        nodo = input("Inserta NodoP: ").upper()
        if re.match("^[0-9]{2}[A-Z]{3}-[0-9]{3}$", nodo):
            break
        else:
            print("El formato debe ser ##XXX-###")
            continue

# Plantilla de URL para las consultas
url_base = (
    "https://ws01.cenace.gob.mx:8082/"
    + tipo_request
    + "/SIM/"
    + sistema
    + "/"
    + proceso
    + "/"
    + nodo
    + "/{}/{}/"
    + "JSON"
)

# convierte en formato de fecha los valores ingresados en el inicio
start_date = datetime.datetime(anio_i, mes_i, dia_i)
end_date = datetime.datetime(anio_f, mes_f, dia_f)

lista_urls = date_to_url(start_date, end_date, url_base)

# A un DataFrame vació le voy agregando los DataFrame de cada URL consultado
df = pd.DataFrame()
for urlz in lista_urls:
    new_df = url_into_df(urlz)
    df = pd.concat((df, new_df))


df.to_csv(
    "{} {} {}.{}.{} - {}.{}.{}.csv".format(
        nodo, proceso, anio_i, mes_i, dia_i, anio_f, mes_f, dia_f
    )
)


print(
    "Se generó un archivo CSV con la consulta del nodo {} - {} de {} a {}".format(
        nodo, proceso, start_date, end_date
    )
)
time.sleep(7)
