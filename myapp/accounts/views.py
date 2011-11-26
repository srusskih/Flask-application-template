# -*- coding: utf-8 -*-
from flask import render_template, session, request, url_for, redirect, current_app
from flask.blueprints import Blueprint
from flaskext.login import login_user, logout_user

from accounts import forms

blueprint = Blueprint('accounts', 'accounts')

@blueprint.route('/login/', methods=['POST', 'GET'])
def login():
    form = forms.AuthForm(request.form)
    if request.method == 'POST' and form.validate():
        login_user(form.get_account())
    return render_template('accounts/login.html', form=form)

@blueprint.route('/logout/', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('.login'))
