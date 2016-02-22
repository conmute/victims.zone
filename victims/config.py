import os
import logging

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'logs/victims.log'
    LOGGING_LEVEL = logging.DEBUG
    CSRF_ENABLED = True
    MODE = 'base'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    MODE = 'development'

class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    MODE = 'testing'

class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    MODE = 'production'


config = {
    "development": "victims.config.DevelopmentConfig",
    "testing": "victims.config.TestingConfig",
    "default": "victims.config.DevelopmentConfig",
    "production": "victims.config.ProductionConfig"
}


def configure_flask(app):
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])
    app.config.from_pyfile('flask.cfg', silent=True)

def configure_logging(app):
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

def configure_app(app):
    configure_flask(app)
    configure_logging(app)