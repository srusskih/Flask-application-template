# -*- coding: utf-8 -*-
from flaskext import wtf as forms
from wtforms import validators
from accounts.models import Account


class AuthForm(forms.Form):
    username = forms.TextField("Username", [validators.required()])
    password = forms.PasswordField("Password", [validators.required()])

    def validate(self):
        is_valid = super(AuthForm, self).validate()
        if is_valid:
            account = Account.query.filter_by(username=self.username.data).first()
            if account and account.check_password(self.password.data):
                self._account = account
                is_valid = True
            else:
                self.errors['auth'] = 'Login incorrect. Check your login or password.'
                is_valid = False

        return is_valid

    def get_account(self):
        return getattr(self, '_account', None)
  