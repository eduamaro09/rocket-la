#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import json
import csv


def filter_data(dir_file, dir_file_csv, filter_slot=2):
    try:
        print('Se inicia proceso para filtrar archivo json')
        # Línea para abrir archivo
        filename = open('%s' % (dir_file), 'r')
        json_output = filename.read()
        data = json.loads(json_output)
        pokemon_slot = [] 
        for pokemon in data['pokemon']:
            slot = pokemon.get('slot', 0)
            if slot == filter_slot:
                pokemon_slot.append(pokemon['pokemon'])

        # Guardar datos en CSV
        if len(pokemon_slot) == 0:
            raise Exception('No existan pokemon con slot %s' % filter_slot)
        csv_file = open(dir_file_csv, 'w')
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        header = pokemon_slot[0].keys()
        csv_writer.writerow(header)
        for row in pokemon_slot:
           csv_writer.writerow(row.values())
        csv_file.close()
        print('Se ha guardado el archivo %s' % dir_file_csv)
    except Exception as error:
        print('============ Mensaje de Error ============')
        print(error)


if __name__ == '__main__':
    # Debe existir el directorio downloads con el archivo (pokeGround.json)
    filter_data(
        dir_file='./downloads/pokeGround.json',
        dir_file_csv='./downloads/twoslotgroundpokemons.csv')
