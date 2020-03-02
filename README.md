# PML-Scraper
Codigo para descargar el Precio Marginal Local del CENACE


Lo que hace esta version es unicamente:

Ingresas fecha de inicio y fecha final de determinado plazo
Se ingresa: sistema, proceso y nodo

Crea una lista de los URLs para la consulta, la idea es utilizar un get.request, pandas, json (?) para extraer los archivos JSON de cada URL y darle formato como CSV, DataFrame, Excel, .txt   -> investigar que es lo más util


Return: lista de URLs
