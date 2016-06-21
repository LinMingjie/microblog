from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from .models import User


class LoginForm(Form):
    # openid = StringField('openid', validators=[DataRequired()])
    email = StringField('Email', validators=[InputRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('remember_me', default=False)
    submit = SubmitField('Log In')


class RegistrationForm(Form):
    email = StringField('Email', validators=[InputRequired(), Length(1, 64), Email()])
    nickname = StringField('Nickname', validators=[
        InputRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                               'Nicknames must have only letters, '
                                               'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[
        InputRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[InputRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('Nickname already in use.')


class EditForm(Form):
    nickname = StringField('nickname', validators=[InputRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])


class PostForm(Form):
    post = StringField('post', validators=[DataRequired()])

