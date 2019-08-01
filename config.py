import os

class Comfig:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://smoucha:mumo@localhost/pitch'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(config):
    pass

