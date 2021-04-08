#!/bin/bash
: '
Se definen variables de conexión al API
'
hostname="https://pokeapi.co"
version="api/v2"
base_url="$hostname/$version"
# Enpoint a ejecutar
endpoint="type/5"

# Se define directorio y nombre del archivo donde se guardará la respuesta de la url
# Este directorio se utiliza en el archivo (question_2/pokemon_filter.py)
dirname="downloads"
filename="pokeGround.json"

# Se crea el directorio
mkdir -p "$dirname"

# Se ejecuta url y se guarda respuesta en archivo
curl -H "Content-Type: application/json" \
 -H "Accept: application/json" "$base_url/$endpoint" -o "$dirname/$filename"
