# Senamhi-estaciones
Spider en Scrapy para descargar datos de estaciones metereologicas en Amazonas, Cajamarca, Lambayeque y La Libertad

## Instalación, funciona con python 2.7
### Instalar entorno virtual

virtualenv env

### activar entorno

source env/bin/activate

### Instalar dependencias

pip install -r requirements.txt

### Ejecutar spider

scrapy crawl tables -o data.csv


