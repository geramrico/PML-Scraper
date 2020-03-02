import datetime
from datetime import timedelta

dia_i = 28  # int(input("Dia inicio: "))
mes_i = 5  # int(input("Mes inicio: "))
anio_i = 2019  # int(input("Año inicio: "))

dia_f = 9  # int(input("Dia fin: "))
mes_f = 1  # int(input("Mes fin: "))
anio_f = 2020  # int(input("Año fin: "))

sistema = "SIN"
proceso = "MDA"
nodo = "01PLO-115"
formato = "JSON"

url_base = "https://ws01.cenace.gob.mx:8082/SWPML/SIM/" + sistema + \
    "/" + proceso + "/" + nodo + "/{}/{}/{}/{}/{}/{}/" + formato

#convierte en formato de fecha los valores ingresados en el inicio
fecha_i = datetime.datetime(anio_i, mes_i, dia_i)
fecha_f = datetime.datetime(anio_f, mes_f, dia_f)

# regresa la cantidad de dias entre la fecha de inicio y la fecha final
plazo = (fecha_f - fecha_i).days + 1

# si el plazo es menor a una semana, solo hará 1 ronda (consulta minima es de 1 semana)
if plazo < 7:
    rondas = 1
# si el plazo es mayor a 7 días, se asignan rondas = al ultimo numero multiplo de 7 en el plazo
else:
    rondas = (plazo - plazo % 7) / 7

# con eso cubres los dias que no entran en las rondas (si plazo = 31, rondas = 4, dias_restantes = 3)
dias_restantes = plazo - rondas * 7


# lista con fechas de inicio de scraping
lista_1 = list()
for i in range(0, int(rondas)):
    lista_1.append((fecha_i + timedelta(days=(7*i))))

# lista con fecha de cierre en el scraper
lista_2 = list()
for i in range(0, int(rondas)):
    lista_2.append((fecha_i + timedelta(days=(7*i)) + timedelta(days=6)))

# considera los "dias restantes" que quedan fuera del rango
lista_3 = list()
for i in range(0, int(dias_restantes)):
    lista_3.append(fecha_i + timedelta(days=7*rondas) + timedelta(days=i))


lista_urls = list()
for i in range(0, int(rondas)):
    lista_urls.append(url_base.format(lista_1[i].year, lista_1[i].month, lista_1[i].day, lista_2[i].year, lista_2[i].month, lista_2[i].day))

lista_urls.append(url_base.format(lista_3[0].year, lista_3[0].month, lista_3[0].day, lista_3[-1].year, lista_3[-1].month, lista_3[-1].day))

for elem in lista_urls:
    print(elem)
