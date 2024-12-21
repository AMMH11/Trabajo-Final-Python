Gestión de Datos Financieros con Python
Descripción del Proyecto
Este proyecto es una aplicación en Python que permite interactuar con datos financieros utilizando la API de Polygon.io. Su propósito principal es proporcionar una herramienta sencilla para descargar, almacenar y visualizar datos históricos de acciones.

El programa está diseñado para:

Descargar datos históricos de precios de acciones desde la API de Polygon.io.
Guardar los datos descargados en una base de datos SQLite.
Mostrar un resumen de los datos almacenados.
Graficar los precios históricos de las acciones seleccionadas.
Características Principales
Descarga de Datos desde Polygon.io:

El programa solicita al usuario un ticker (como AAPL) y un rango de fechas.
Los datos se obtienen a través de una API y se guardan en una base de datos SQL para su posterior uso.
Almacenamiento en Base de Datos:

Los datos descargados se almacenan en una base de datos SQLite (stocks.db).
La tabla incluye columnas como ticker, fecha, apertura, máximo, mínimo, cierre, y volumen.
Resumen de Datos:

Se puede consultar un resumen de los tickers almacenados junto con el rango de fechas disponible para cada uno.
Visualización de Datos:

El programa permite graficar los precios de cierre de un ticker específico en función del tiempo, utilizando matplotlib.
Estructura del Proyecto
El proyecto está estructurado en módulos para mantener un diseño limpio y modular:

main.py: Punto de entrada del programa. Presenta un menú principal que permite seleccionar entre las opciones de actualizar datos, visualizar datos o salir.

api_client.py: Módulo encargado de la comunicación con la API de Polygon.io para descargar los datos financieros.

database.py: Módulo para la gestión de la base de datos SQLite. Crea la tabla de datos y maneja la inserción y consulta de registros.

plotter.py: Módulo encargado de graficar los datos históricos de precios utilizando matplotlib.

.gitignore: Archivo que especifica qué elementos deben ignorarse en el repositorio (por ejemplo, la carpeta del entorno virtual y archivos temporales).

requirements.txt: Archivo con las dependencias necesarias para el proyecto (requests, pandas, matplotlib).

Ejemplo de Uso
Al ejecutar el programa, verás un menú como este:

markdown

--- Menú Principal ---
1. Actualizar datos
2. Visualizar datos
3. Salir
Elige una opción:
Actualizar Datos:



Ingrese ticker a pedir:
AAPL
Ingrese fecha de inicio (YYYY-MM-DD):
2022-01-01
Ingrese fecha de fin (YYYY-MM-DD):
2022-07-01
Resumen de Datos:



Los tickers guardados en la base de datos son:
AAPL - 2022-01-01 <-> 2022-07-01
MSFT - 2021-01-01 <-> 2021-12-31
Gráfico:


Ingrese el ticker a graficar:
AAPL
Se generará un gráfico del precio de cierre de la acción AAPL para el rango de fechas solicitado.

Requerimientos
Python 3.8 o superior.
Librerías de Python:
requests
pandas
matplotlib
