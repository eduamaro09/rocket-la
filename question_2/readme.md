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
