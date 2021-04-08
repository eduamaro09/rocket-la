# API REST ROCKET.LA

### Tecnologías
* **Python**: `v3.8.5`


* **El proyecto se divide en dos secciones,question_2 es donde se tiene  el script en bash para descargar el json de pokemones**
* Se deben ejecutar los siguientes pasos para descargar y generar el parseo de datos

# Script para descargar y filtrar información

### Tecnologías
* **Python**: `v2.7`


### Descargar información en formato jsons
* `./download_pokemon.sh` debe tener permisos de ejecución
* Dentro del archivo están explicadas las variables que se requiere configurar
```bash
: '
Este archivo permite descargar información y guardarla en un archivo
'
> chmod +x download_pokemon.sh
```

### Filtrar datos con slot 2
* El archivo `pokemon_filter.py` permite filtrar la información con slot 2 y guardar la información
en un archivo csv, depende de la descarga del archivo JSON
```bash
: '
En el archivo se comentan las variables y datos necesarios para su ejecución
'
> python pokemon_filter.py
```



### Instalación de la aplicación
```bash
> pip install -r requirements.txt
```


### Iniciar la aplicación
* **Nota** deben existir los archivos (`./data/pokeGround.json`, `./data/twoslotgroundpokemons.csv`)
* El archivo `./config.py` contiene la definición de las variables del proyecto
* **Iniciar la app** `> python app`


### Api REST
* **Cargar archivo csv**
    * POST => `api/v1/upload/pokemons`
    * Se dede mandar el archivo por medio del parámetro `file`
    ```bash
    curl --location --request POST 'api/v1/upload/pokemons' \
    --form 'file=@"/temp/twoslotgroundpokemons.csv"'
    ```
* **Buscar pokemones en archivo json**
    * GET => `api/v1/pokemons?filter=sand`
* **Buscar pokemones en archivo csv**
    * GET => `/api/v1/csv/pokemons?filter=sand`