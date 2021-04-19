#!/usr/bin/env python3

class Config(object):
    MONGODB_HOST = 'http://127.0.0.1:80'
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    MONGODB_HOST = 'http://127.0.0.1:80'
    #DEBUG = True
    #TESTING = True

