from datetime import timedelta

class Config(object):
    SUPER_ADMIN_KEY='sachin'
    SUPER_ADMIN_PASSWORD='sachin1234'
    ADMIN_CODE='Admin@9969'
    SECRET_KEY='Akdojao978380ws'
    SESSION_COOKIE_SECURE=True
    SESSION_PERMANENT = True
    # PERMANENT_SESSION_LIFETIME = timedelta(minutes=86400)
    SESSION_TYPE = "filesystem"
    DB_NAME='member'
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:ams_12345@localhost/member'


class Production(Config):
    ENV='production'
    SECRET_KEY=False
    DEBUG=False

class Developement(Config):
    ENV='developement'
    DEBUG=True