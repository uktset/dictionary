from os import getenv
import os

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'gewjhiogwehng'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    

class TestingConfig(Config):
    TESTING = True