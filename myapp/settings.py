# -*- coding: utf-8 -*-
class Applications(object):
    INSTALLED_APPS = (
        'accounts',
        # ...
    )

class Config(Applications):
    DEBUG = True
    SECRET_KEY = 'some_secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'

