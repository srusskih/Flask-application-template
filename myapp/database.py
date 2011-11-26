# -*- coding: utf-8 -*
from flaskext.sqlalchemy import SQLAlchemy
from flaskext.script import Command, prompt_bool

db = SQLAlchemy()


class InitDB(Command):
    def handle(self, app, *args, **kwargs):
        with app.test_request_context():
            self.run(app)

    def run(self, app):
        db.create_all(app=app)


class DropDB(Command):
    def run(self):
        if prompt_bool("Are you sure you want to lose all your data"):
            db.drop_all()

