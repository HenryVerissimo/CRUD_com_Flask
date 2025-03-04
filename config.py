import os, random, string

class Config(object):
    CSRF_ENABLE = True
    SECRET = "e3c7b4591194b6eab2ad9028db8193828370c3e9416ab7bc67017a56b8629500"
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = "localhost"
    PORT_HOST = 8000
    URL_MAIN = f"http://{IP_HOST}:{PORT_HOST}" #http://localhost:8000
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://User:senha123@localhost:3306/BancoAplicacaoFlask"

app_config = {
    "development": DevelopmentConfig(),
    "testing": None,
    "production": None
}

app_active = os.getenv("FLASK_ENV")

if app_active is None:
    app_active = "development"
