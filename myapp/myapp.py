# -*- coding: utf-8 -*-
import sys
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.Config')
    return app

def connect_db(app):
    import database
    database.db.init_app(app)
    return database.db

def initial_login_manager(app):
    import login_manager
    login_manager.login_manager.setup_app(app)
    return login_manager.login_manager

def reg_blueprints(app):
    apps = app.config.get('INSTALLED_APPS')
    for a in apps:
        module = __import__(a)
        bp = getattr(module, 'bp', getattr(module, 'blueprint', None))
        if bp:
            app.register_blueprint(bp)

app = create_app()
db = connect_db(app)
initial_login_manager(app)
reg_blueprints(app)

if __name__ == '__main__':
    if sys.argv[-1] == 'init_db':
        print ">>> DB initialise"
        db.create_all(app=app)
    else:
        app.run()
