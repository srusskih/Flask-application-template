# -*- coding: utf-8 -*-
from werkzeug import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

from myapp import db, login_manager


class Account(db.Model, UserMixin):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    hash_password = db.Column(db.String(255))

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "<Entry %r>" % self.username[:20]

    def __unicode__(self):
        return self.username

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()

    def get_id(self):
        return unicode(self.id)

    def set_password(self, new_password):
        self.hash_password = generate_password_hash(new_password)

    def check_password(self, password):
        return check_password_hash(self.hash_password, password)


@login_manager.user_loader
def load_user(userid):
    return Account.query.filter_by(id=userid).first()
