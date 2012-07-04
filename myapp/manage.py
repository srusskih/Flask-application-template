from myapp import app, db
from flask.ext.script import Manager, prompt_bool

manager = Manager(app)


@manager.command
def initdb():
    db.create_all()


@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to lose all your data"):
        db.drop_all()


if __name__ == '__main__':
    manager.run()
