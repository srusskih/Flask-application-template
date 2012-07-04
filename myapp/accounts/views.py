# -*- coding: utf-8 -*-
from flask import render_template, request, url_for, redirect
from flask.blueprints import Blueprint
from flask.ext.login import login_user, logout_user

from forms import AuthForm

blueprint = Blueprint('accounts', 'accounts')


@blueprint.route('/login/', methods=['POST', 'GET'])
def login():
    form = AuthForm(request.form)
    if request.method == 'POST' and form.validate():
        login_user(form.get_account())
    return render_template('accounts/login.html', form=form)


@blueprint.route('/logout/', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('.login'))
