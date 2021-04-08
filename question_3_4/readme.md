# API REST POKEMÓN

### Tecnologías
* **Python**: `v3.8.5`


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