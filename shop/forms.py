from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, PasswordField, SubmitField,TextAreaField
from wtforms.fields.simple import FileField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
import email_validator
from flask import url_for,request

from shop.models import User


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired('Это поле обьязательно!'), Email('Не правильный email')])
    password = PasswordField('Пароль', validators=[DataRequired('Это поле обьязательно!')])
    confirm_password = PasswordField('Потвердите пароль', validators=[
                                     DataRequired('Это поле обьязательно!'), EqualTo('password', message="Не правильный повторный пароль!")])
    submit = SubmitField('Регистрация')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('email существует')
class PostForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField('Контент', validators=[DataRequired()])
    image = FileField('Картинка', validators=[DataRequired()])
    submit = SubmitField('Создать пост')    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired('Это поле обьязательно!'), Email('Не правильный email')])
    password = PasswordField('Пароль', validators=[DataRequired('Это поле обьязательно!')])
    
    submit = SubmitField('Регистрация')     

    

