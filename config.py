import os
import json

class Config:
    pass


class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

# load config file and return application configs
def load_config():

    # get config file
    CONFIG_FOLDER = os.path.dirname(os.path.abspath(__file__))
    conf_file = os.path.join(CONFIG_FOLDER, 'config.json')

    # open config file
    with open(conf_file) as config_file:
        config = json.load(config_file)

    return config