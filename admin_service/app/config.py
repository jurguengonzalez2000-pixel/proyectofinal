import os 

class config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///admin.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = 'super-secret-key'