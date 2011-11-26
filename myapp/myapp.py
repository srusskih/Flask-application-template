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

def create_manager(app):
    from flaskext.script import Manager
    manager = Manager(app)

    # add commands for DB management
    import database
    manager.add_command("initdb", database.InitDB())
    manager.add_command("dropdb", database.DropDB())

    # TODO:
    # Init commands from installed modules
    #
    # module/
    # module/__init__.py
    # module/commands/
    # module/commands/__init__.py
    # models/commands/mycommand.py

    return manager

app = create_app()
manager = create_manager(app)
connect_db(app)
initial_login_manager(app)
reg_blueprints(app)

if __name__ == '__main__':
    manager.run()
