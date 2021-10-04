from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
import email_validator


from shop.models import User


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_paswword = PasswordField('Потвердите пароль', validators=[
                                     DataRequired, EqualTo(password)])
    submit = SubmitField('Регистрация')
