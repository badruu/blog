import os

class Config:
    SECRET_KEY='1234567890'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://salaaxnoor:123@localhost/badru_pitches'

    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME='badruuu.n.97@gmail.com'
    MAIL_PASSWORD='Noorbadar79'

class DevConfig(Config):

    pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

config_options={
    'Development' :DevConfig,
    'Production' :ProdConfig
}