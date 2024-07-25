import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///image_processing.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

   
