# -*- coding: utf-8 -*-
#import sys
from flask import Flask, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager


app = Flask(__name__)
app.config.from_object('settings.Config')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


def reg_blueprints(app):
    apps = app.config.get('INSTALLED_APPS')
    for a in apps:
        module = __import__(a)
        bp = getattr(module, 'bp', getattr(module, 'blueprint', None))
        if bp:
            app.register_blueprint(bp)

reg_blueprints(app)


@app.route('/')
def index():
    return redirect(url_for('accounts.login'))
