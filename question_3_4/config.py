class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    UPLOADED_FILES = './cdn'
    '''
    El directorio (data) debe existir y contener los
    archivos(pokeGround.json y twoslotgroundpokemons.csv)
    '''
    POKEMON_FILENAME_JSON = './data/pokeGround.json'
    POKEMON_FILENAME_CSV = './data/twoslotgroundpokemons.csv'


config = {
    'development': DevelopmentConfig,
}
