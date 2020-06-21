# PML-Scraper
Codigo para descargar el Precio Marginal Local del CENACE

Esta es una herramienta para acceder al Servicio Web del CENACE y descargar los PML o PEND de manera mas facil. Se siguio la metodología de los manuales mencionados al final del readme.

***

## Descripción
> El Servicio Web está basado en el estilo arquitectónico “REST” (en inglés, REpresentation State Transfer). En la
invocación del SW-PEND se utiliza el método GET para obtener información de un recurso.

> El formato de invocación del SW-PEND es:
> https://ws01.cenace.gob.mx:8082/SWPEND/SIM/parámetros

Parámetros para la invocación del SW-PEND o SW-PML:

- sistema: SIN, BCA o BCS
- proceso MDA o MTR
- lista_zc: clave de nodo o zona de carga
- año incial: año inicial del periodo AAAA
- mes inicial: mes inicial del periodo MM
- dia inicial: dia inicial del periodo DD
- año fin: año fin del periodo AAAA
- mes fin: mes fin del periodo MM
- dia fin: dia fin del periodo DD
- formato XML o JSON (este programa usa JSON)

Ejemplo de URL de consulta: https://ws01.cenace.gob.mx:8082/SWPEND/SIM/SIN/MDA/AGUASCALIENTES/2017/04/19/2017/04/19/JSON

Las consultas solo pueden ser de una semana (7 días), por ejemplo; si quieres consultar del 1 al 31 de enero del NodoP "01PLO-115", se haran 5 consultas de la siguiente manera:

Basicamente toma la fecha de inicio y le suma 6 dias para ir haciendo intervalos de 7 (por eso a veces no termina exactamente en la fecha seleccionada)
- consulta 1: 1 al 7 de enero
- consulta 2: 8 al 14 de enero
- consulta 3: 15 al 21 de enero
- consulta 4: 22 al 28 de enero
- consulta 5: 29 al 04 de enero
 
Asi se verìan los URLS de los cuales se obtendrían los archivos JSON
1. 'https://ws01.cenace.gob.mx:8082/SWPML/SIM/SIN/MDA/01PLO-115/2019/01/01/2019/01/07/JSON'
2. 'https://ws01.cenace.gob.mx:8082/SWPML/SIM/SIN/MDA/01PLO-115/2019/01/08/2019/01/14/JSON'
3. 'https://ws01.cenace.gob.mx:8082/SWPML/SIM/SIN/MDA/01PLO-115/2019/01/15/2019/01/21/JSON'
4. 'https://ws01.cenace.gob.mx:8082/SWPML/SIM/SIN/MDA/01PLO-115/2019/01/22/2019/01/28/JSON'
5. 'https://ws01.cenace.gob.mx:8082/SWPML/SIM/SIN/MDA/01PLO-115/2019/01/29/2019/02/04/JSON'

Finalmente, el programa por cada URL crea un "Data Frame" utilizando la libería Pandas y los concatena; después los exporta a un archivo CSV para la manipulación del usuario.

***

## Ideas para futuras versiones
- [ ] Regresa minimo, maximo y promedio de los valores consultados
- [ ] Creación de graficas/reporte utilizando matplotlib
- [ ] Consulta con multiples parametros de "zona de carga"

### MANUALES:
[Manual Técnico Uso de Servicio Web para descarga de Precios de Energía en Nodos Distribuidos (SW-PEND)](https://www.cenace.gob.mx/DocsMEM/2020-01-14%20Manual%20T%C3%A9cnico%20SW-PEND.pdf)

[Manual Técnico Uso de Servicio Web para descarga de Precios Marginales Locales (SW-PML)](https://www.cenace.gob.mx/DocsMEM/2020-01-14%20Manual%20T%C3%A9cnico%20SW-PML.pdf)
