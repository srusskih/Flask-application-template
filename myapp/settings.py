# -*- coding: utf-8 -*-
DEBUG = True

SECRET_KEY = 'some_secret'

DATABASE = {
    'name': '/db.sqlite3'
    'engine' = 'sqlite://'
}

SQLALCHEMY_DATABASE_URI = DATABASE['engine']+DATABASE['name']

INSTALLED_APPS = (
    'accounts'
    # ...
)
