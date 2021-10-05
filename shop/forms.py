from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
import email_validator
from flask import url_for

from shop.models import User


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired('Это поле обьязательно!'), Email('Не правильный email')])
    password = PasswordField('Пароль', validators=[DataRequired('Это поле обьязательно!')])
    confirm_password = PasswordField('Потвердите пароль', validators=[
                                     DataRequired('Это поле обьязательно!'), EqualTo('password')])
    submit = SubmitField('Регистрация')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('email существует')
    def validate_login(self,email):
        u = User.query.filter_by(email=email.data).first()
        if u is None:
            raise ValidationError('email существует')

