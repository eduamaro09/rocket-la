from flask import Flask
from flask import jsonify
from flask import request
from config import config
import json
import csv
import os
import pathlib
import logging


def create_app(enviroment):
    app = Flask(__name__)
    app.config.from_object(enviroment)
    return app


enviroment = config['development']
app = create_app(enviroment=enviroment)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Pokémon API</h1><p>Permite consultar información de pokemones.</p>"


'''
Permite la búsqueda sobre el archivo JSON descargado
'''
@app.route('/api/v1/pokemons', methods=['GET'])
def get_pokemons_in_json():
    try:
        query = request.args.get('filter') if 'filter' in request.args.keys() else ''
        # Se abre el archivo pokeGround.json y se convierte a un diccionario el contenido
        dir_file = os.path.join(app.config['POKEMON_FILENAME_JSON'])
        filename = json.loads(open(dir_file, 'r').read())
        # Se obtiene la lista de pokemones
        data = filename.get('pokemon', [])
        pokemons = data
        if len(query) > 0:
            # Si el parametro de búsqueda (filter) contiene algo se busca el valor en los registros             
            pokemons = []
            # buscar pokemon en archivo
            for row in data:
                try:
                    pokemon = row.get('pokemon', None)
                    if pokemon:
                        # Se convierte el nombre del pokemón a minúscula al igual que el valor de la búsqueda
                        search = pokemon.get('name').lower().find(query.lower())
                        if search >= 0:
                            '''
                            Cuando existen coincidencias se agregan a la variable pokemons para ser
                            mostradas al usuario
                            '''
                            pokemons.append(row)
                except Exception as error:
                    # Si existe un error en el proceso se muestra en el log
                    logging.error(error)
                    # pass => se continua con el flujo
                    pass
        if len(pokemons) == 0:
            return jsonify({'detail': 'No existen pokemones para la búsqueda (%s)' % query}), 404
        response = {'count': len(pokemons), 'results': pokemons}
        return jsonify(response), 200
    except Exception as error:
        return jsonify({'detail': str(error)}), 404


'''
Permite la búsqueda sobre el archivo CSV, este archivo contiene solo datos
con slot: 2
'''
@app.route('/api/v1/csv/pokemons', methods=['GET'])
def get_pokemons_in_csv():
    try:
        query = request.args.get('filter') if 'filter' in request.args.keys() else ''
        pokemons = []
        dir_file = os.path.join(app.config['POKEMON_FILENAME_CSV'])
        csv_file = csv.reader(open(dir_file, 'r'), delimiter=',')
        headers = next(csv_file)
        if len(query) > 0:
            # buscar pokemon en archivo
            for row in csv_file:
                try:
                    search = row[0].lower().find(query.lower())
                    if search >= 0:
                        key, value = row
                        pokemons.append({headers[0]: key, headers[1]: value})
                except Exception as error:
                    print(error)
                    pass
        else:
            for row in csv_file:
                key, value = row
                pokemons.append({headers[0]: key, headers[1]: value})
            # pokemons.append(list(csv_file))
        if len(pokemons) == 0:
            raise ValueError('No existen pokemones para la búsqueda (%s)' % (query))
        response = {'count': len(pokemons), 'results': pokemons}
        return jsonify(response), 200
    except Exception as error:
        return jsonify({'detail': str(error)}), 404


@app.route('/api/v1/upload/pokemons', methods=['POST'])
def upload_filename():
    try:
        file = request.files['file'] if 'file' in request.files else None
        if file is None:
            return jsonify({'detail': 'Debes proporcionar el parámetro file'}), 400
        # file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.file)
        filename = file.filename.lower()
        if filename.endswith('.csv') is False:
            return jsonify({'detail': 'Solo se aceptan archivos con extensión (.csv)'}), 400
        '''
        Se crea el directorio definido en el archivo (./question_3/config.py) en la variable
        UPLOADED_FILES
        '''
        pathlib.Path(app.config['UPLOADED_FILES']).mkdir(exist_ok=True)
        # Se guarda el archivo en el directorio(UPLOADED_FILES) con el nombre con el que se cargo
        file.save(os.path.join(app.config['UPLOADED_FILES'], filename))
        response = {'detail': 'Se ha cargado exitosamente el archivo (%s)' % filename}
        return jsonify(response)
    except Exception as error:
        return jsonify({'detail': str(error)}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0')
