#!/usr/bin/env python3
from flask import Flask
from app import create_app
#app = Flask(__name__)
app = create_app('db_config.DevelopmentConfig')
app.secret_key = 'secret123'
if __name__ == '__main__':
    
    app.run(host='127.0.0.1', port=8080, debug=True)
